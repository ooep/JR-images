#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""batch_fetch.py — JR-images 可复用抓取流水线（目标站清单为可替换输入，不写死数量）。

对每个目标站：
  1. 在 Wikimedia Commons 找候选（站分类 → 日文站名搜索 → Wikidata P373 分类兜底）；
  2. 许可硬过滤：只收 CC0 / CC BY * / CC BY-SA * / Public domain（含 No restrictions），
     其余（NC/ND/GFDL/不明/缺失）一律拒收并记原因；CC BY* 必须带作者，否则拒收；
  3. 规格硬过滤：原图长边 ≥1600px、文件 ≤25MB、mime ∈ jpeg/png/webp（不放大、不压缩抵赖）；
  4. 下载原图到临时目录 → 数值质检（Pillow+numpy：拉普拉斯方差/色彩丰富度/纯白占比/
     边缘密度/天空占比 + 文件名与来源关键词）→ 选最优一张；
  5. 落盘 stations/<slug>/photo.<ext>（原始字节，不重压缩）+ licenses/<slug>.txt，
     合并 index.json，逐站更新 state.json（断点续跑）。

纪律：单域名并发 ≤2、请求间隔 ≥1.05s、明确 UA、尊重 robots；令牌不涉入本脚本。

用法：
  python batch_fetch.py --stations data/stations_stamp1089.json \
      --batch-index 0 --batch-size 500 --workdir . [--probe]
"""
import argparse
import datetime
import hashlib
import io
import json
import os
import re
import sys
import threading
import time

import numpy
import requests
from PIL import Image

UA = 'JR-images-bot/1.0 (https://github.com/ooep/JR-images; station photo archive; contact: github.com/ooep)'
API = 'https://commons.wikimedia.org/w/api.php'
WIKIDATA = 'https://www.wikidata.org/w/api.php'
MIN_INTERVAL = 1.05          # 每域名最小请求间隔（秒）
MAX_CONCURRENT_PER_DOMAIN = 2
MIN_SIDE = 1600              # 原图长边下限（px）
MAX_BYTES = 25 * 1024 * 1024  # 单文件上限 25MB（超限直接选次优，不压缩抵赖）
OK_MIME = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp'}

# 数值质检阈值（在长边缩到 1024 的副本上计算）
REJECT_LAP, REVIEW_LAP = 45.0, 75.0        # 拉普拉斯方差：清晰度
REJECT_COLOR, REVIEW_COLOR = 18.0, 25.0    # Hasler-Süsstrunk 色彩丰富度（低于→地图/文字/灰度图嫌疑）
REJECT_WHITE, REVIEW_WHITE = 0.55, 0.42    # >245 灰度像素占比（高于→文字/截图嫌疑）
MAP_EDGE, MAP_COLOR = 0.03, 90.0           # 低边缘密度+高饱和 → 地图/图形嫌疑

GOOD_KW = re.compile(r'駅|station|eki|駅舎|プラットホーム|改札|駅前|ホーム|platform', re.I)
BAD_KW = re.compile(r'車内|车内|interior|運転台|driver.?s?\s*cab|inside\s+(the\s+)?train|rolling\s*stock|車両基地', re.I)

ALLOWED_LICENSE_RE = re.compile(
    r'^(cc0|cc\s*by(-sa)?\s*[0-9.]+|public\s*domain|no\s*restrictions|pd[-\s])', re.I)
FORBIDDEN_LICENSE_RE = re.compile(r'nc|nd|gfdl|share\s*alike\s*only', re.I)


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


class DomainLimiter:
    """每域名：并发 ≤2 且相邻请求间隔 ≥ MIN_INTERVAL。"""

    def __init__(self):
        self._lock = threading.Lock()
        self._last = {}
        self._sem = {}

    def acquire(self, domain):
        with self._lock:
            if domain not in self._sem:
                self._sem[domain] = threading.BoundedSemaphore(MAX_CONCURRENT_PER_DOMAIN)
                self._last[domain] = 0.0
            sem = self._sem[domain]
        sem.acquire()
        with self._lock:
            wait = self._last[domain] + MIN_INTERVAL - time.time()
        if wait > 0:
            time.sleep(wait)
        with self._lock:
            self._last[domain] = time.time()

    def release(self, domain):
        with self._lock:
            sem = self._sem[domain]
        sem.release()


LIMITER = DomainLimiter()
SESSION = requests.Session()
SESSION.headers['User-Agent'] = UA


def http_get(url, params=None, domain=None, tries=4, timeout=60, stream=False):
    domain = domain or re.sub(r'^https?://([^/]+)/.*$', r'\1', url + '/')
    last = None
    for i in range(tries):
        LIMITER.acquire(domain)
        try:
            r = SESSION.get(url, params=params, timeout=timeout, stream=stream)
            if r.status_code == 429:
                retry_after = int(r.headers.get('Retry-After', '5') or 5)
                r.close()
                time.sleep(min(retry_after, 30) * (i + 1))
                continue
            r.raise_for_status()
            return r
        except Exception as e:  # noqa: BLE001 - 网络重试
            last = e
            time.sleep(2 * (i + 1))
        finally:
            LIMITER.release(domain)
    raise RuntimeError('GET failed after retries: %s (%s)' % (url, last))


def api_json(url, params, domain=None):
    params = dict(params)
    params['format'] = 'json'
    r = http_get(url, params=params, domain=domain)
    with r:
        return r.json()


# ---------------------------------------------------------------- Commons 候选


def category_files(cat_title):
    d = api_json(API, {'action': 'query', 'list': 'categorymembers',
                       'cmtitle': cat_title, 'cmtype': 'file', 'cmlimit': '100'})
    return [m['title'] for m in d.get('query', {}).get('categorymembers', [])]


def search_files(query, limit=30):
    d = api_json(API, {'action': 'query', 'generator': 'search', 'gsrsearch': query,
                       'gsrnamespace': '6', 'gsrlimit': str(limit),
                       'prop': 'info'})
    pages = d.get('query', {}).get('pages', {})
    return [p['title'] for p in pages.values()]


def wikidata_category(name):
    """日文站名 → (Commons 分类 P373, 英文 label)。找不到返回 (None, None)。"""
    try:
        d = api_json(WIKIDATA, {'action': 'wbsearchentities', 'search': name,
                                'language': 'ja', 'uselang': 'en', 'type': 'item',
                                'limit': '5'}, domain='www.wikidata.org')
        items = d.get('search', [])
        if not items:
            return None, None
        qid = None
        for it in items:
            label = (it.get('label') or '')
            if name.rstrip('駅') in label or label in name:
                qid = it['id']
                break
        qid = qid or items[0]['id']
        d2 = api_json(WIKIDATA, {'action': 'wbgetentities', 'ids': qid,
                                 'props': 'claims|labels', 'languages': 'en'},
                      domain='www.wikidata.org')
        ent = d2.get('entities', {}).get(qid, {})
        en_label = (ent.get('labels', {}).get('en') or {}).get('value')
        for c in ent.get('claims', {}).get('P373', []):
            v = c.get('mainsnak', {}).get('datavalue', {}).get('value')
            if v:
                return 'Category:' + v, en_label
        return None, en_label
    except Exception:  # noqa: BLE001 - Wikidata 只是兜底
        return None, None


def imageinfo_batch(titles):
    """title -> {url, size, width, height, mime, extmetadata}（≤25/批）。"""
    out = {}
    for i in range(0, len(titles), 25):
        chunk = titles[i:i + 25]
        d = api_json(API, {'action': 'query', 'titles': '|'.join(chunk),
                           'prop': 'imageinfo',
                           'iiprop': 'url|size|mime|extmetadata'})
        for p in d.get('query', {}).get('pages', {}).values():
            ii = (p.get('imageinfo') or [None])[0]
            if ii:
                out[p['title']] = ii
    return out


# ---------------------------------------------------------------- 许可判定


def license_verdict(extmeta):
    """返回 (ok, license_name, license_url, author, reason)。"""
    em = extmeta or {}

    def val(k):
        v = em.get(k) or {}
        return (v.get('value') or '').strip()

    lic_raw = val('LicenseShortName') or val('License')
    lic = re.sub(r'\s+', ' ', lic_raw)
    lic_url = val('LicenseUrl')
    author = re.sub(r'<[^>]+>', '', val('Artist')).strip()
    if not lic:
        return False, None, None, author, 'license_missing'
    if FORBIDDEN_LICENSE_RE.search(lic):
        return False, lic, lic_url, author, 'license_forbidden'
    if not ALLOWED_LICENSE_RE.match(lic):
        return False, lic, lic_url, author, 'license_unclear'
    if lic.lower().startswith('cc by') and not author:
        return False, lic, lic_url, author, 'no_author_metadata'
    return True, lic, lic_url, author, None


# ---------------------------------------------------------------- 数值质检


def analyze_pixels(data):
    """在长边 1024 的副本上算数值指标（全部数值判定，不用任何图片类工具）。"""
    im = Image.open(io.BytesIO(data))
    im.load()
    w, h = im.size
    rgb = im.convert('RGB')
    scale = 1024.0 / max(w, h)
    if scale < 1:
        rgb = rgb.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    a = numpy.asarray(rgb, dtype=numpy.float32)
    gray = a.mean(axis=2)
    lap = (gray[1:-1, :-2] + gray[1:-1, 2:] + gray[:-2, 1:-1] + gray[2:, 1:-1]
           - 4 * gray[1:-1, 1:-1])
    lap_var = float(lap.var())
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    rg = R - G
    yb = 0.5 * (R + G) - B
    colorfulness = float(numpy.sqrt(rg.std() ** 2 + yb.std() ** 2)
                         + 0.3 * numpy.sqrt(rg.mean() ** 2 + yb.mean() ** 2))
    white_frac = float((gray > 245).mean())
    gx = numpy.abs(numpy.diff(gray, axis=1))
    gy = numpy.abs(numpy.diff(gray, axis=0))
    edge_density = float(((gx > 24).mean() + (gy > 24).mean()) / 2)
    hh = gray.shape[0] // 3
    top = a[:hh, :, :]
    sat = top.max(axis=2) - top.min(axis=2)
    bright = top.mean(axis=2)
    sky_frac = float(((bright > 150) & (sat < 60)).mean())
    return {
        'width': w, 'height': h,
        'lap_var': round(lap_var, 1),
        'colorfulness': round(colorfulness, 1),
        'white_frac': round(white_frac, 3),
        'edge_density': round(edge_density, 4),
        'sky_frac': round(sky_frac, 3),
    }


def quality_verdict(m, title, from_category):
    """返回 (verdict, reasons)：verdict ∈ done/review/reject。
    车站本体判定：分类来源=主题证据；搜索来源要求文件名含车站关键词；
    车厢内部/地图/文字截图特征 → 拒收或存疑（教训：旧批「広島港・宇品」配车厢内部照）。"""
    reasons = []
    if m['lap_var'] < REJECT_LAP:
        return 'reject', ['blurry(lap=%.0f<%.0f)' % (m['lap_var'], REJECT_LAP)]
    if m['colorfulness'] < REJECT_COLOR:
        return 'reject', ['low_color(map/text?)']
    if m['white_frac'] > REJECT_WHITE:
        return 'reject', ['white_screenshot']
    if m['edge_density'] < MAP_EDGE and m['colorfulness'] > MAP_COLOR:
        reasons.append('map_like')
    if m['lap_var'] < REVIEW_LAP:
        reasons.append('soft_focus')
    if m['colorfulness'] < REVIEW_COLOR:
        reasons.append('low_color')
    if m['white_frac'] > REVIEW_WHITE:
        reasons.append('mostly_white')
    bad = bool(BAD_KW.search(title))
    good = bool(GOOD_KW.search(title))
    if bad and not good:
        reasons.append('subject_doubtful(interior_kw)')
    if not from_category and not good:
        reasons.append('subject_unverified(no_station_kw)')
    return ('review' if reasons else 'done'), reasons


# ---------------------------------------------------------------- 单站流水线


def gather_candidates(st):
    """返回 (candidates:[{title, from_category}], en_label_or_None)。"""
    name = (st.get('name') or '').strip()
    key = name[:-1] if name.endswith('駅') else name
    en = (st.get('name_en') or '').strip()
    titles, seen, en_label = [], set(), None

    def add(ts, from_category):
        for t in ts:
            if t not in seen:
                seen.add(t)
                titles.append((t, from_category))

    cat_guesses = ['Category:%s駅' % key]
    if en:
        cat_guesses.append('Category:%s Station' % en)
    cat_guesses += ['Category:%s Station' % key, 'Category:%s' % key]
    for cat in cat_guesses:
        try:
            add(category_files(cat), True)
        except Exception:  # noqa: BLE001
            pass
        if len(titles) >= 8:
            break
    if len(titles) < 8:
        try:
            add(search_files('%s駅' % key), False)
        except Exception:  # noqa: BLE001
            pass
    if not titles:
        cat, en_label = wikidata_category(name)
        if cat:
            try:
                add(category_files(cat), True)
            except Exception:  # noqa: BLE001
                pass
    return [{'title': t, 'from_category': fc} for t, fc in titles], en_label


def score_candidate(info, title, from_category):
    s = 2.0 if from_category else 0.0
    if GOOD_KW.search(title):
        s += 2.0
    if BAD_KW.search(title):
        s -= 3.0
    long_side = max(info.get('width') or 0, info.get('height') or 0)
    s += min(long_side / 2000.0, 3.0)
    if info.get('mime') == 'image/jpeg':
        s += 0.5
    return s


def process_station(st, args, tmpdir):
    """返回该站结果 dict（含 status/file/metrics/reasons 等）。"""
    slug = st['slug']
    name = st.get('name') or ''
    cands, en_label = gather_candidates(st)
    if not cands:
        return {'status': 'missing', 'reasons': ['no_candidates']}, None

    infos = imageinfo_batch([c['title'] for c in cands])
    merged = []
    for c in cands:
        info = infos.get(c['title'])
        if not info:
            continue
        merged.append(dict(c, info=info))

    # 硬过滤：许可 / 尺寸 / 体积 / mime
    kept, reject_dist = [], {}
    for c in merged:
        info = c['info']
        ok, lic, lic_url, author, reason = license_verdict(info.get('extmetadata'))
        if not ok:
            reject_dist[reason] = reject_dist.get(reason, 0) + 1
            continue
        w, h = info.get('width') or 0, info.get('height') or 0
        if max(w, h) < MIN_SIDE:
            reject_dist['resolution_low'] = reject_dist.get('resolution_low', 0) + 1
            continue
        if (info.get('size') or 0) > MAX_BYTES:
            reject_dist['oversize_gt_25mb'] = reject_dist.get('oversize_gt_25mb', 0) + 1
            continue
        if info.get('mime') not in OK_MIME:
            reject_dist['mime_unsupported'] = reject_dist.get('mime_unsupported', 0) + 1
            continue
        c.update(lic=lic, lic_url=lic_url, author=author,
                 score=score_candidate(info, c['title'], c['from_category']))
        kept.append(c)

    if not kept:
        return {'status': 'missing', 'reasons': reject_dist}, None

    kept.sort(key=lambda c: -c['score'])
    if args.probe:
        top = kept[0]
        return {'status': 'probe', 'reasons': reject_dist,
                'probe_pick': top['title'], 'probe_license': top['lic']}, None

    # 逐张下载验证 + 数值质检，选最优
    best, best_metrics, best_reasons, downloads = None, None, None, 0
    for c in kept[:args.max_download]:
        downloads += 1
        try:
            r = http_get(c['info']['url'], domain='upload.wikimedia.org',
                         stream=True, timeout=180)
            with r:
                data = r.content
        except Exception:  # noqa: BLE001
            reject_dist['fetch_error'] = reject_dist.get('fetch_error', 0) + 1
            continue
        if len(data) > MAX_BYTES:
            reject_dist['oversize_gt_25mb'] = reject_dist.get('oversize_gt_25mb', 0) + 1
            continue
        try:
            m = analyze_pixels(data)
        except Exception:  # noqa: BLE001
            reject_dist['undecodable'] = reject_dist.get('undecodable', 0) + 1
            continue
        if m['width'] != c['info'].get('width') or m['height'] != c['info'].get('height'):
            m['width'], m['height'] = c['info'].get('width'), c['info'].get('height')
        if max(m['width'] or 0, m['height'] or 0) < MIN_SIDE:
            reject_dist['resolution_low'] = reject_dist.get('resolution_low', 0) + 1
            continue
        verdict, reasons = quality_verdict(m, c['title'], c['from_category'])
        if verdict == 'reject':
            for x in reasons:
                reject_dist[x] = reject_dist.get(x, 0) + 1
            continue
        c['_data'] = data
        c['_metrics'] = m
        c['_verdict_reasons'] = reasons
        best = c
        best_metrics, best_reasons = m, reasons
        if verdict == 'done':
            break  # 已经有干净的最优解

    if best is None:
        return {'status': 'missing', 'reasons': reject_dist}, None

    # 落盘：原始字节，不重压缩
    ext = OK_MIME[best['info']['mime']]
    photo_dir = os.path.join(args.workdir, 'stations', slug)
    os.makedirs(photo_dir, exist_ok=True)
    photo_path = os.path.join(photo_dir, 'photo' + ext)
    with open(photo_path, 'wb') as f:
        f.write(best['_data'])
    sha = hashlib.sha256(best['_data']).hexdigest()
    rel_file = 'stations/%s/photo%s' % (slug, ext)

    em = best['info'].get('extmetadata') or {}
    page_url = (em.get('DescriptionPage') or {}).get('value') or \
        'https://commons.wikimedia.org/wiki/File:' + best['title'].replace('File:', '').replace(' ', '_')
    lic_txt = (
        'station: %s (%s)\n'
        'file: %s\n'
        'sha256: %s\n'
        'source_page: %s\n'
        'image_url: %s\n'
        'author: %s\n'
        'license: %s\n'
        'license_url: %s\n'
        'retrieved_at: %s\n'
        'attribution: %s / %s / %s / %s\n'
    ) % (name, slug, rel_file, sha, page_url, best['info'].get('url'),
         best['author'] or '(unknown)', best['lic'], best['lic_url'] or '(none)',
         now_iso(), best['author'] or '(unknown)', best['title'], best['lic'],
         best['lic_url'] or '(none)')
    lic_dir = os.path.join(args.workdir, 'licenses')
    os.makedirs(lic_dir, exist_ok=True)
    with open(os.path.join(lic_dir, slug + '.txt'), 'w', encoding='utf-8') as f:
        f.write(lic_txt)

    status = 'done' if not best_reasons else 'review'
    entry = {
        'status': status,
        'file': rel_file,
        'sha256': sha,
        'bytes': len(best['_data']),
        'width': best_metrics['width'],
        'height': best_metrics['height'],
        'source_title': best['title'],
        'source_page': page_url,
        'author': best['author'],
        'license': best['lic'],
        'license_url': best['lic_url'],
        'metrics': best_metrics,
        'reasons': best_reasons,
        'reject_dist': reject_dist,
        'downloads': downloads,
    }
    return entry, en_label


# ---------------------------------------------------------------- 批处理主流程


def load_state(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {'schema': 1, 'entries': {}}


def save_state(path, state):
    state['updated_at'] = now_iso()
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def merge_index(path, updates, list_meta):
    idx = {'meta': {'schema': 2}, 'stations': {}}
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            idx = json.load(f)
    idx.setdefault('stations', {}).update(updates)
    idx['meta'].update({
        'schema': 2,
        'updated_at': now_iso(),
        'stations_list': list_meta,
        'total_indexed': len(idx['stations']),
    })
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(idx, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, path)
    return idx


def append_progress(path, block):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(block + '\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stations', required=True, help='make_station_list.py 生成的清单 JSON')
    ap.add_argument('--batch-index', type=int, required=True)
    ap.add_argument('--batch-size', type=int, default=500)
    ap.add_argument('--workdir', default='.', help='仓库根（写 stations/ licenses/ index.json）')
    ap.add_argument('--state', default=None, help='state.json 路径（默认 <workdir>/state.json）')
    ap.add_argument('--max-download', type=int, default=5, help='每站最多下载验证的候选数')
    ap.add_argument('--probe', action='store_true', help='只选候选不下载（本地冒烟用）')
    ap.add_argument('--limit', type=int, default=0, help='本批最多处理多少站（0=全部）')
    args = ap.parse_args()

    with open(args.stations, encoding='utf-8') as f:
        doc = json.load(f)
    # 清单顺序即执行顺序（排序责任在 make_station_list，如 C 优先）
    stations = doc['stations']
    lo = args.batch_index * args.batch_size
    batch = stations[lo:lo + args.batch_size]
    if args.limit:
        batch = batch[:args.limit]
    print('[batch %d] list=%s canonical_total=%d batch=%d (%s)' % (
        args.batch_index, args.stations, len(stations), len(batch),
        '%s..%s' % (batch[0]['slug'], batch[-1]['slug']) if batch else '-'))

    state_path = args.state or os.path.join(args.workdir, 'state.json')
    state = load_state(state_path)
    state.update({'stations_path': args.stations, 'batch_index': args.batch_index,
                  'batch_size': args.batch_size})

    tmpdir = os.path.join(args.workdir, '.tmp_fetch')
    os.makedirs(tmpdir, exist_ok=True)

    stats = {'attempted': 0, 'done': 0, 'review': 0, 'missing': 0, 'failed': 0,
             'skipped_resume': 0, 'bytes': 0, 'reject_dist': {}, 'dead': []}
    index_updates = {}
    t0 = time.time()

    for i, st in enumerate(batch):
        slug = st['slug']
        prev = state['entries'].get(slug, {})
        if prev.get('status') in ('done', 'review') and not args.probe:
            stats['skipped_resume'] += 1
            continue
        stats['attempted'] += 1
        try:
            entry, en_label = process_station(st, args, tmpdir)
        except Exception as e:  # noqa: BLE001
            entry, en_label = {'status': 'failed', 'reasons': ['exception:%s' % str(e)[:120]]}, None
        entry['ts'] = now_iso()
        entry['attempts'] = prev.get('attempts', 0) + 1
        state['entries'][slug] = entry
        save_state(state_path, state)

        status = entry['status']
        stats[status if status in stats else 'failed'] += 1
        for k, v in (entry.get('reject_dist') or {}).items():
            stats['reject_dist'][k] = stats['reject_dist'].get(k, 0) + v
        if status in ('done', 'review'):
            stats['bytes'] += entry['bytes']
            index_updates[slug] = {
                'station_id': st['id'], 'name': st['name'],
                'name_en': en_label or st.get('name_en'),
                'lat': st.get('lat'), 'lon': st.get('lon'),
                'pref': st.get('pref'), 'scene': st.get('scene'),
                'lines': st.get('lines') or [], 'same_as': st.get('same_as') or [],
                'status': status, 'file': entry['file'],
                'width': entry['width'], 'height': entry['height'],
                'bytes': entry['bytes'], 'sha256': entry['sha256'],
                'source': entry['source_page'], 'license': entry['license'],
                'license_url': entry['license_url'], 'author': entry['author'],
                'page_url': entry['source_page'],
                'retrieved_at': entry['ts'], 'metrics': entry.get('metrics'),
                'review_reasons': entry.get('reasons') or [],
            }
        elif status == 'missing':
            stats['dead'].append({'slug': slug, 'name': st['name'],
                                  'reasons': entry.get('reasons')})
        if (i + 1) % 10 == 0:
            elapsed = time.time() - t0
            print('[%d/%d] done=%d review=%d missing=%d failed=%d skip=%d %.1fs/station' % (
                i + 1, len(batch), stats['done'], stats['review'], stats['missing'],
                stats['failed'], stats['skipped_resume'], elapsed / (i + 1)))
            sys.stdout.flush()

    if not args.probe and index_updates:
        merge_index(os.path.join(args.workdir, 'index.json'), index_updates, args.stations)

    elapsed = time.time() - t0
    stats['elapsed_sec'] = round(elapsed)
    stats['batch_index'] = args.batch_index
    stats['generated_at'] = now_iso()
    stats_path = os.path.join(args.workdir, 'batch_stats_%d.json' % args.batch_index)
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)

    # PROGRESS.md 追加（随批提交进仓库）
    idx_total = 0
    idx_path = os.path.join(args.workdir, 'index.json')
    if os.path.exists(idx_path):
        with open(idx_path, encoding='utf-8') as f:
            idx_total = len(json.load(f).get('stations', {}))
    block = (
        '\n## batch %d — %s\n'
        '- list: `%s` (canonical %d)\n'
        '- attempted=%d done=%d review=%d missing=%d failed=%d skipped_resume=%d\n'
        '- bytes_this_batch=%d avg=%d\n'
        '- reject_dist=%s\n'
        '- cumulative_indexed=%d/%d\n'
        '- elapsed=%ds\n'
    ) % (args.batch_index, stats['generated_at'], args.stations, len(stations),
         stats['attempted'], stats['done'], stats['review'], stats['missing'],
         stats['failed'], stats['skipped_resume'], stats['bytes'],
         stats['bytes'] // max(1, stats['done'] + stats['review']),
         json.dumps(stats['reject_dist'], ensure_ascii=False),
         idx_total, len(stations), stats['elapsed_sec'])
    if not args.probe:
        append_progress(os.path.join(args.workdir, 'PROGRESS.md'), block)

    print(json.dumps({k: stats[k] for k in
                      ('attempted', 'done', 'review', 'missing', 'failed',
                       'skipped_resume', 'bytes', 'elapsed_sec')}, ensure_ascii=False))
    print('reject_dist:', json.dumps(stats['reject_dist'], ensure_ascii=False))
    print('dead stations:', len(stats['dead']))
    return 0


if __name__ == '__main__':
    sys.exit(main())

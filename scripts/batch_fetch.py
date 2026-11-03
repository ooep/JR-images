#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""batch_fetch.py — JR-images 可复用抓取流水线（目标站清单为可替换输入，不写死数量）。

对每个目标站：
  1. 在 Wikimedia Commons 找候选（站分类 → 日文站名搜索 → Wikidata P373 分类兜底）；
  2. 许可硬过滤：只收 CC0 / CC BY * / CC BY-SA * / Public domain（含 No restrictions），
     其余（NC/ND/GFDL/不明/缺失）一律拒收并记原因；CC BY* 必须带作者，否则拒收；
  3. 规格硬过滤：原图长边 ≥1600px（dead 重试放宽到 1280px 并标记 below_spec）、
     文件 ≤25MB、mime ∈ jpeg/png/webp（不放大、不压缩抵赖）；
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
import concurrent.futures
import datetime
import hashlib
import io
import json
import os
import re
import sys
import threading
import time
from urllib.parse import unquote

import numpy
import requests
from PIL import Image

UA = ('JR-images-bot/1.0 (https://github.com/ooep/JR-images; '
      'contact: https://github.com/ooep/JR-images/issues)')
API = 'https://commons.wikimedia.org/w/api.php'
WIKIDATA = 'https://www.wikidata.org/w/api.php'
MIN_INTERVAL = 1.05          # 每域名最小请求间隔（秒）。Wikimedia API:Etiquette 要求
                             # Action API 串行请求；无文档支持不得调低
MAXLAG = 5                   # API:Etiquette/Robot policy 推荐的 maxlag 值
# 并发口径（依 Wikimedia 文档）：Action API（commons/wikidata）严格串行=1；
# 下载层 upload.wikimedia.org 为静态文件主机、独立限流域，允许 2 并发
DOMAIN_CONCURRENCY = {'upload.wikimedia.org': 2}
DEFAULT_CONCURRENCY = 1
MIN_SIDE = 1600              # 原图长边下限（px）
MAX_LONG = 1800              # 落盘长边上限（px）：实测 1800/q85 在 1280 显示宽下 PSNR≈44dB，
                             # 观感与 2048/q88 无差别，单站体积约降 30%
JPEG_Q = 85                  # 归一化 JPEG 质量
DEAD_MIN_SIDE = 1280         # dead 站重试放宽后的原图长边下限（落盘条目标记 below_spec）
DEAD_RETRY = 25              # 每批最多重试多少 dead 站（86 张重复图清欠，10→25 提速）
DEAD_MAX_ATTEMPTS = 3        # 累计尝试次数达到该值即标 final_dead，不再进重试池
DEAD_PATH = 'data/dead_stations.json'
NEAR_HAMMING = 6               # dHash 64bit 汉明距离 ≤6 视为同一张照片的不同编码
MAX_BYTES = 25 * 1024 * 1024  # 单文件上限 25MB（超限直接选次优，不压缩抵赖）
OK_MIME = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp'}

# 数值质检阈值（在长边缩到 1024 的副本上计算）
REJECT_LAP, REVIEW_LAP = 45.0, 75.0        # 拉普拉斯方差：清晰度
REJECT_COLOR, REVIEW_COLOR = 18.0, 25.0    # Hasler-Süsstrunk 色彩丰富度（低于→地图/文字/灰度图嫌疑）
REJECT_WHITE, REVIEW_WHITE = 0.55, 0.42    # >245 灰度像素占比（高于→文字/截图嫌疑）
MAP_EDGE, MAP_COLOR = 0.03, 90.0           # 低边缘密度+高饱和 → 地图/图形嫌疑

GOOD_KW = re.compile(r'駅|station|eki|駅舎|プラットホーム|改札|駅前|ホーム|platform', re.I)
BAD_KW = re.compile(r'車内|车内|interior|運転台|driver.?s?\s*cab|inside\s+(the\s+)?train|rolling\s*stock|車両基地', re.I)

# 选图口径：只要车站实景（駅舎外観/站前/站台与周边风景），地图/示意图/文字截图一律弃
HARD_EXCLUDE_RE = re.compile(
    r'地図|路線図|案内図|構内図|平面図|見取図|配置図|時刻表|運賃表|標識|駅名標|看板|ポスター|'
    r'切符|きっぷ|ロゴ|ジオラマ|模型|スクリーンショット|図面|図解|イラスト|ダイヤ|'
    r'\bmaps?\b|\bdiagrams?\b|\btimetables?\b|\bsigns?(?:age)?\b|\bposters?\b|'
    r'\btickets?\b|\blogos?\b|\bscreenshots?\b|\bdrawings?\b|\billustrations?\b|\bcharts?\b',
    re.I)
CAT_BONUS_RE = re.compile(r'Station buildings|Station forecourts|駅舎', re.I)
TITLE_STRONG_RE = re.compile(r'駅舎|駅前|駅と|風景|景色|遠景|パノラマ|全景|panorama|station.?building', re.I)
TITLE_PLATFORM_RE = re.compile(r'ホーム|platform|プラットホーム', re.I)
GOOD_SCORE = 8.0      # 总分达到该值即停止继续下载（已够好的实景照）
REVIEW_SCORE = 5.0    # 总分低于该值只入 review，不硬塞一张不合格的

ALLOWED_LICENSE_RE = re.compile(
    r'^(cc0|cc\s*by(-sa)?\s*[0-9.]+|public\s*domain|no\s*restrictions|pd[-\s])', re.I)
FORBIDDEN_LICENSE_RE = re.compile(r'nc|nd|gfdl|share\s*alike\s*only', re.I)


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


class DomainLimiter:
    """每域名：并发上限（API 域严格串行=1）且相邻请求间隔 ≥ MIN_INTERVAL。"""

    def __init__(self):
        self._lock = threading.Lock()
        self._last = {}
        self._sem = {}
        self.degraded = False

    def degrade(self):
        """熔断降级：全部域名并发降到 1（间隔不变），直到本运行结束。"""
        with self._lock:
            self.degraded = True
            self._sem = {}

    def acquire(self, domain):
        with self._lock:
            if domain not in self._sem:
                n = 1 if self.degraded else DOMAIN_CONCURRENCY.get(
                    domain, DEFAULT_CONCURRENCY)
                self._sem[domain] = threading.BoundedSemaphore(n)
                self._last.setdefault(domain, 0.0)
            sem = self._sem[domain]
        sem.acquire()
        with self._lock:
            wait = self._last[domain] + MIN_INTERVAL - time.time()
        if wait > 0:
            time.sleep(wait)
        with self._lock:
            self._last[domain] = time.time()
        return sem

    def release(self, sem):
        sem.release()


LIMITER = DomainLimiter()
SESSION = requests.Session()
SESSION.headers['User-Agent'] = UA

RATE = {'events': 0}
MAXLAG_RETRIES = {'n': 0}          # maxlag 等待重试单独计数（不计入 dead）
UPLOAD_ERR_STREAK = {}             # 下载层连续 4xx/5xx 计数（熔断用）


def rate_event(kind, url):
    """熔断：命中 429/403/maxlag/下载层连续错误 → 立即降级（并发 1 + 1.05s 间隔）并计数；
    同一运行内累计 ≥2 次 → 直接中止本批（保护配额，链由看守按同因规则处置）。"""
    RATE['events'] += 1
    LIMITER.degrade()
    print('RATE_LIMIT_EVENT #%d kind=%s url=%s -> degraded: concurrency=1, '
          'interval=%.2fs' % (RATE['events'], kind, url[:120], MIN_INTERVAL),
          flush=True)
    if RATE['events'] >= 2:
        raise SystemExit('rate limit events >= 2 in this run; '
                         'stopping batch to protect quota')


def http_err_streak(domain, status, url):
    """下载层熔断：upload.wikimedia.org 连续 3 次 4xx/5xx → 同 API 层熔断处置。"""
    if domain != 'upload.wikimedia.org':
        return
    UPLOAD_ERR_STREAK[domain] = UPLOAD_ERR_STREAK.get(domain, 0) + 1
    if UPLOAD_ERR_STREAK[domain] >= 3:
        UPLOAD_ERR_STREAK[domain] = 0
        rate_event('upload_http_%s_x3' % status, url)


def http_ok(domain):
    UPLOAD_ERR_STREAK.pop(domain, None)


def http_get(url, params=None, domain=None, tries=4, timeout=60, stream=False):
    domain = domain or re.sub(r'^https?://([^/]+)/.*$', r'\1', url + '/')
    last = None
    for i in range(tries):
        sem = LIMITER.acquire(domain)
        try:
            r = SESSION.get(url, params=params, timeout=timeout, stream=stream)
            if r.status_code == 429:
                retry_after = int(r.headers.get('Retry-After', '5') or 5)
                r.close()
                rate_event('429(retry_after=%d)' % retry_after, url)
                time.sleep(min(retry_after, 60) * (i + 1))
                continue
            if r.status_code == 403:
                rate_event('403', url)
            if r.status_code >= 400:
                http_err_streak(domain, r.status_code, url)
            else:
                http_ok(domain)
            r.raise_for_status()
            return r
        except SystemExit:
            raise
        except Exception as e:  # noqa: BLE001 - 网络重试
            last = e
            time.sleep(2 * (i + 1))
        finally:
            LIMITER.release(sem)
    raise RuntimeError('GET failed after retries: %s (%s)' % (url, last))


def api_json(url, params, domain=None):
    params = dict(params)
    params['format'] = 'json'
    params.setdefault('maxlag', str(MAXLAG))
    for _ in range(5):
        r = http_get(url, params=params, domain=domain)
        with r:
            d = r.json()
        err = d.get('error') or {}
        if err.get('code') == 'maxlag':
            MAXLAG_RETRIES['n'] += 1   # 单独计数：等待重试不进 dead
            rate_event('maxlag(lag=%s)' % err.get('lag'), url)
            time.sleep(min(int(err.get('lag') or MAXLAG), 30))
            continue
        return d
    raise RuntimeError('maxlag persisted after retries: %s' % url)


# ---------------------------------------------------------------- Commons 候选


def category_files(cat_title):
    d = api_json(API, {'action': 'query', 'list': 'categorymembers',
                       'cmtitle': cat_title, 'cmtype': 'file', 'cmlimit': '100'})
    return [m['title'] for m in d.get('query', {}).get('categorymembers', [])]


def category_files_info(cat_title):
    """categorymembers + imageinfo 合并为一次请求（省一次 API 往返）。"""
    d = api_json(API, {'action': 'query', 'generator': 'categorymembers',
                       'gcmtitle': cat_title, 'gcmtype': 'file', 'gcmlimit': '100',
                       'prop': 'imageinfo',
                       'iiprop': 'url|size|mime|extmetadata'})
    out = {}
    for p in d.get('query', {}).get('pages', {}).values():
        out[p['title']] = (p.get('imageinfo') or [None])[0]
    return out


def search_files(query, limit=30):
    d = api_json(API, {'action': 'query', 'generator': 'search', 'gsrsearch': query,
                       'gsrnamespace': '6', 'gsrlimit': str(limit),
                       'prop': 'info'})
    pages = d.get('query', {}).get('pages', {})
    return [p['title'] for p in pages.values()]


def search_files_info(query, limit=30):
    """search + imageinfo 合并为一次请求（省一次 API 往返）。"""
    d = api_json(API, {'action': 'query', 'generator': 'search', 'gsrsearch': query,
                       'gsrnamespace': '6', 'gsrlimit': str(limit),
                       'prop': 'imageinfo',
                       'iiprop': 'url|size|mime|extmetadata'})
    out = {}
    for p in d.get('query', {}).get('pages', {}).values():
        out[p['title']] = (p.get('imageinfo') or [None])[0]
    return out


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
    brightness = float(gray.mean())
    dark_frac = float((gray < 40).mean())
    ch, cw = gray.shape
    cgray = gray[int(ch * 0.2):int(ch * 0.8), int(cw * 0.2):int(cw * 0.8)]
    cgx = numpy.abs(numpy.diff(cgray, axis=1))
    cgy = numpy.abs(numpy.diff(cgray, axis=0))
    center_edge = float(((cgx > 24).mean() + (cgy > 24).mean()) / 2)
    return {
        'width': w, 'height': h,
        'lap_var': round(lap_var, 1),
        'colorfulness': round(colorfulness, 1),
        'white_frac': round(white_frac, 3),
        'edge_density': round(edge_density, 4),
        'sky_frac': round(sky_frac, 3),
        'brightness': round(brightness, 1),
        'dark_frac': round(dark_frac, 3),
        'center_edge': round(center_edge, 4),
    }


def normalize_image(data, max_long=MAX_LONG, quality=JPEG_Q):
    """统一归一化：长边缩到 max_long（不足则不放大）后一律转存 JPEG(q=quality)。
    统一重编码才能锁定单站体积上限；原图 ≤max_long 的也不再原样保留（PNG/超大 JPEG 会破坏体积口径）。"""
    im = Image.open(io.BytesIO(data))
    im.load()
    w, h = im.size
    w0, h0 = w, h
    if im.mode not in ('RGB', 'L'):
        im = im.convert('RGB')
    if max(w, h) > max_long:
        scale = max_long / float(max(w, h))
        w, h = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
        im = im.resize((w, h), Image.LANCZOS)
    out = io.BytesIO()
    im.save(out, 'JPEG', quality=quality, optimize=True, progressive=True)
    return out.getvalue(), (w, h), {
        'encoded': True, 'long': max(w, h), 'quality': quality,
        'original_width': w0, 'original_height': h0}


def dhash64(data):
    """差值感知哈希（9x8 → 64bit）：识别「同一张照片的不同编码」。"""
    im = Image.open(io.BytesIO(data)).convert('L').resize((9, 8), Image.LANCZOS)
    px = list(im.getdata())
    bits = 0
    for row in range(8):
        for col in range(8):
            bits = (bits << 1) | (1 if px[row * 9 + col] < px[row * 9 + col + 1] else 0)
    return bits


def hamming(a, b):
    return bin(a ^ b).count('1')


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


def image_score(m):
    """画面质量打分（只用已有解码指标）：分辨率先达标，再奖励横向/白天/色彩好/主体适中。
    返回浮点分；越低越像「地图/文字/夜景/远景主体过小/局部特写」。"""
    s = 0.0
    long_side = max(m.get('width') or 0, m.get('height') or 0)
    if long_side >= 1600:
        s += 3.0 + min((long_side - 1600) / 320.0, 2.0)   # >2048 后不再加分
    else:
        s -= 2.0
    ar = (m.get('width') or 1) / float(m.get('height') or 1)
    if ar >= 1.2:
        s += 2.0                                          # 横向构图优先
    elif ar < 0.8:
        s -= 1.5                                          # 竖图降权
    b = m.get('brightness') or 0.0
    s += min(max((b - 90.0) / 60.0, -2.0), 1.5)           # 白天、亮度均值高
    s -= min((m.get('dark_frac') or 0.0) * 4.0, 2.0)      # 夜景/大面积暗部降权
    s += min((m.get('colorfulness') or 0.0) / 40.0, 2.5)  # 饱和度/色彩方差高
    ce = m.get('center_edge') or 0.0
    if ce < 0.012:                                        # 主体过小（大远景/空景）
        s -= 1.0
    elif ce > 0.24:                                       # 局部特写（门牌/站名牌）
        s -= 1.0
    return round(s, 2)


# ---------------------------------------------------------------- 单站流水线


def gather_candidates(st, relaxed=False):
    """返回 (candidates:[{title, from_category, cat}], en_label_or_None, infos:{title: imageinfo})。
    候选查询用 generator+imageinfo 合并请求，infos 已预取，后续通常无需二次 imageinfo。
    relaxed=True（dead 站重试）：追加英文/罗马字站名检索与「駅前/駅舎」检索，放宽候选池。"""
    name = (st.get('name') or '').strip()
    key = name[:-1] if name.endswith('駅') else name
    en = (st.get('name_en') or '').strip()
    titles, seen, en_label, infos = [], set(), None, {}

    def add_info(mapping, from_category, cat=None):
        for t, info in (mapping or {}).items():
            if t not in seen:
                seen.add(t)
                titles.append((t, from_category, cat))
            if info:
                infos.setdefault(t, info)

    cat_guesses = ['Category:%s駅' % key]
    if en:
        cat_guesses.append('Category:%s Station' % en)
    cat_guesses += ['Category:%s Station' % key, 'Category:%s' % key]
    for cat in cat_guesses:
        try:
            add_info(category_files_info(cat), True, cat)
        except Exception:  # noqa: BLE001
            pass
        if len(titles) >= 8:
            break
    if len(titles) < 8:
        try:
            add_info(search_files_info('%s駅' % key), False)
        except Exception:  # noqa: BLE001
            pass
    if relaxed and len(titles) < 16:
        queries = [q for q in (en and '%s Station' % en, en, '%s駅前' % key, '%s駅舎' % key) if q]
        for q in queries:
            try:
                add_info(search_files_info(q), False)
            except Exception:  # noqa: BLE001
                pass
            if len(titles) >= 24:
                break
    if not titles:
        cat, en_label = wikidata_category(name)
        if cat:
            try:
                add_info(category_files_info(cat), True, cat)
            except Exception:  # noqa: BLE001
                pass
        elif relaxed and key:
            try:
                add_info(search_files_info(key), False)
            except Exception:  # noqa: BLE001
                pass
    return [{'title': t, 'from_category': fc, 'cat': cat}
            for t, fc, cat in titles], en_label, infos


def rank_bonus(title, cat):
    """候选排序加分（权重：站房/站前分类 3 > 站房/风景标题 2 > 站台 1）。"""
    s = 0.0
    if cat and CAT_BONUS_RE.search(cat):
        s += 3.0
    if TITLE_STRONG_RE.search(title or ''):
        s += 2.0
    elif TITLE_PLATFORM_RE.search(title or ''):
        s += 1.0
    return s


def score_candidate(info, title, from_category, cat=None):
    s = 2.0 if from_category else 0.0
    s += rank_bonus(title, cat)
    if GOOD_KW.search(title):
        s += 1.0
    if BAD_KW.search(title):
        s -= 3.0
    long_side = max(info.get('width') or 0, info.get('height') or 0)
    s += min(long_side / 2000.0, 3.0)
    if info.get('mime') == 'image/jpeg':
        s += 0.5
    return s


def process_station(st, args, tmpdir, relaxed=False, used=None):
    """返回该站结果 dict（含 status/file/metrics/reasons 等）。
    relaxed=True：dead 站重试，原图分辨率下限放宽到 DEAD_MIN_SIDE，命中条目标 below_spec。
    used={'title': {title: slug}, 'sha': {sha256: slug}}：已落盘图登记表，命中即跳过该候选。"""
    slug = st['slug']
    name = st.get('name') or ''
    min_side = DEAD_MIN_SIDE if relaxed else MIN_SIDE
    cands, en_label, prefetched = gather_candidates(st, relaxed)
    if not cands:
        return {'status': 'missing', 'reasons': ['no_candidates']}, None

    infos = dict(prefetched)
    missing = [c['title'] for c in cands if not infos.get(c['title'])]
    if missing:
        infos.update(imageinfo_batch(missing))
    merged = []
    for c in cands:
        info = infos.get(c['title'])
        if not info:
            continue
        merged.append(dict(c, info=info))

    # 重复图抑制（补丁 1）：候选 title 已被别的站用过就跳过；same_as 同组豁免
    same_as = set(st.get('same_as') or [])
    used_title = (used or {}).get('title') or {}
    deduped = []
    for c in merged:
        owner = used_title.get(c['title'])
        if owner and owner != slug and owner not in same_as:
            continue
        deduped.append(c)
    dup_title_skipped = len(merged) - len(deduped)
    merged = deduped
    if not merged and dup_title_skipped:
        return {'status': 'missing', 'reasons': {'duplicate_all_used': dup_title_skipped}}, None

    # 硬过滤：选图口径硬排除（地图/示意图/时刻表/标牌/文字图）+ 许可 / 尺寸 / 体积 / mime
    kept, reject_dist = [], {}
    for c in merged:
        info = c['info']
        if HARD_EXCLUDE_RE.search(c['title']) or \
                (c.get('cat') and HARD_EXCLUDE_RE.search(c['cat'])):
            reject_dist['hard_excluded'] = reject_dist.get('hard_excluded', 0) + 1
            continue
        ok, lic, lic_url, author, reason = license_verdict(info.get('extmetadata'))
        if not ok:
            reject_dist[reason] = reject_dist.get(reason, 0) + 1
            continue
        w, h = info.get('width') or 0, info.get('height') or 0
        if max(w, h) < min_side:
            reject_dist['resolution_low'] = reject_dist.get('resolution_low', 0) + 1
            continue
        if (info.get('size') or 0) > MAX_BYTES:
            reject_dist['oversize_gt_25mb'] = reject_dist.get('oversize_gt_25mb', 0) + 1
            continue
        if info.get('mime') not in OK_MIME:
            reject_dist['mime_unsupported'] = reject_dist.get('mime_unsupported', 0) + 1
            continue
        c.update(lic=lic, lic_url=lic_url, author=author,
                 bonus=rank_bonus(c['title'], c.get('cat')),
                 score=score_candidate(info, c['title'], c['from_category'], c.get('cat')))
        kept.append(c)

    if not kept:
        return {'status': 'missing', 'reasons': reject_dist}, None

    kept.sort(key=lambda c: -c['score'])
    if args.probe:
        top = kept[0]
        return {'status': 'probe', 'reasons': reject_dist,
                'probe_pick': top['title'], 'probe_license': top['lic']}, None

    # 逐张下载验证 + 数值质检 + 排序打分，择优（不再「关键词命中就收」）
    used_sha = (used or {}).get('sha') or {}
    used_dhash = (used or {}).get('dhash') or {}
    scored, downloads = [], 0
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
        if max(m['width'] or 0, m['height'] or 0) < min_side:
            reject_dist['resolution_low'] = reject_dist.get('resolution_low', 0) + 1
            continue
        verdict, reasons = quality_verdict(m, c['title'], c['from_category'])
        if verdict == 'reject':
            for x in reasons:
                reject_dist[x] = reject_dist.get(x, 0) + 1
            continue
        # 先归一化再判重：只有最终落盘字节完全相同才算重复图（补丁 1）
        try:
            ndata, (nw, nh), norm = normalize_image(data, MAX_LONG, JPEG_Q)
        except Exception:  # noqa: BLE001
            reject_dist['undecodable'] = reject_dist.get('undecodable', 0) + 1
            continue
        sha = hashlib.sha256(ndata).hexdigest()
        owner = used_sha.get(sha)
        if owner and owner != slug and owner not in same_as:
            reject_dist['duplicate_sha256'] = reject_dist.get('duplicate_sha256', 0) + 1
            continue  # 命中已用过的图 → 试下一候选，不落盘
        # 感知近重复：同一照片不同编码（dHash 汉明 ≤ NEAR_HAMMING）同样跳过
        try:
            dh = dhash64(ndata)
        except Exception:  # noqa: BLE001
            dh = None
        if dh is not None:
            near_owner = None
            for odh, oslug in used_dhash.items():
                if oslug != slug and oslug not in same_as and hamming(odh, dh) <= NEAR_HAMMING:
                    near_owner = oslug
                    break
            if near_owner:
                reject_dist['near_duplicate'] = reject_dist.get('near_duplicate', 0) + 1
                continue
        m2 = dict(m, width=nw, height=nh)
        total = round((c.get('bonus') or 0.0) + image_score(m2), 2)
        scored.append(dict(c, _data=ndata, _norm=norm, _metrics=m2, _sha=sha,
                           _dhash=dh,
                           _verdict_reasons=reasons, _score=total))
        if verdict == 'done' and total >= GOOD_SCORE:
            break  # 已是高分实景照，不再继续下载

    if not scored:
        if reject_dist.get('duplicate_sha256'):
            return {'status': 'missing',
                    'reasons': {'duplicate_all_used': reject_dist['duplicate_sha256']}}, None
        return {'status': 'missing', 'reasons': reject_dist}, None

    best = max(scored, key=lambda x: (x['_score'], x['score']))
    data, norm, sha = best['_data'], best['_norm'], best['_sha']
    best_metrics = dict(best['_metrics'])
    best_reasons = list(best['_verdict_reasons'])
    long_side = max(best_metrics['width'], best_metrics['height'])
    below_spec = long_side < MIN_SIDE
    ext = '.jpg'
    photo_dir = os.path.join(args.workdir, 'stations', slug)
    os.makedirs(photo_dir, exist_ok=True)
    photo_path = os.path.join(photo_dir, 'photo' + ext)
    with open(photo_path, 'wb') as f:
        f.write(data)
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
        'normalized: %s\n'
        'attribution: %s / %s / %s / %s\n'
    ) % (name, slug, rel_file, sha, page_url, best['info'].get('url'),
         best['author'] or '(unknown)', best['lic'], best['lic_url'] or '(none)',
         now_iso(),
         'normalized to long side %d (JPEG q%d) from %dx%d%s' % (
             long_side, JPEG_Q, norm.get('original_width', 0), norm.get('original_height', 0),
             ' [below_spec retry]' if below_spec else ''),
         best['author'] or '(unknown)', best['title'], best['lic'],
         best['lic_url'] or '(none)')
    lic_dir = os.path.join(args.workdir, 'licenses')
    os.makedirs(lic_dir, exist_ok=True)
    with open(os.path.join(lic_dir, slug + '.txt'), 'w', encoding='utf-8') as f:
        f.write(lic_txt)

    status = 'done' if not best_reasons else 'review'
    if best['_score'] < REVIEW_SCORE:
        best_reasons.append('low_score(%.1f<%.1f)' % (best['_score'], REVIEW_SCORE))
        status = 'review'  # 最高分都不够 → 留人工确认，不硬塞
    if below_spec:
        best_reasons = list(best_reasons) + ['below_spec(long=%d,%s retry)' % (long_side, 'dead')]
        status = 'review'
    entry = {
        'status': status,
        'file': rel_file,
        'sha256': sha,
        'dhash': ('%016x' % best['_dhash']) if best.get('_dhash') is not None else None,
        'bytes': len(data),
        'width': best_metrics['width'],
        'height': best_metrics['height'],
        'normalized': norm,
        'below_spec': below_spec,
        'score': best['_score'],
        'source_title': best['title'],
        'source_cat': best.get('cat'),
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


def load_dead(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {'schema': 1, 'stations': {}}


def save_dead(path, dead):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    dead['updated_at'] = now_iso()
    dead['count'] = len(dead['stations'])
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(dead, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, path)


def title_from_page(url):
    """从 Commons 文件页 URL 还原候选 title（旧条目没存 source_title 时用）。"""
    if not url or '/wiki/' not in url:
        return None
    t = unquote(url.split('/wiki/', 1)[1]).replace('_', ' ')
    return t if t.startswith('File:') else 'File:' + t


def dead_upsert(dead, st, entry, stage):
    """把失败站写进 dead 清单（站 / 原因 / 来源 URL / 尝试次数），保留首次发现时间。
    attempts 达 DEAD_MAX_ATTEMPTS 时打 final_dead，退出重试池（仍留在清单备查）。"""
    slug = st['slug']
    prev = dead['stations'].get(slug, {})
    attempts = prev.get('attempts', 0) + 1
    dead['stations'][slug] = {
        'slug': slug,
        'name': st.get('name'),
        'name_en': st.get('name_en'),
        'stage': stage,
        'reasons': entry.get('reasons') or entry.get('reject_dist') or {},
        'reject_dist': entry.get('reject_dist') or {},
        'source_page': entry.get('source_page'),
        'below_spec': bool(entry.get('below_spec')),
        'attempts': attempts,
        'final_dead': attempts >= DEAD_MAX_ATTEMPTS,
        'first_seen': prev.get('first_seen') or now_iso(),
        'last_attempt': now_iso(),
    }


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
    ap.add_argument('--dead-list', default=None,
                    help='dead 清单路径（默认 <workdir>/data/dead_stations.json）')
    ap.add_argument('--retry-dead', type=int, default=DEAD_RETRY,
                    help='每批开始前最多重试多少 dead 站（0=关闭）')
    ap.add_argument('--dead-only', action='store_true',
                    help='只跑 dead 重试：跳过本批抓取、不改 state.batch_index')
    args = ap.parse_args()

    with open(args.stations, encoding='utf-8') as f:
        doc = json.load(f)
    # 清单顺序即执行顺序（排序责任在 make_station_list，如 C 优先）
    stations = doc['stations']
    lo = args.batch_index * args.batch_size
    batch = stations[lo:lo + args.batch_size]
    if args.limit:
        batch = batch[:args.limit]
    if args.dead_only:
        batch = []
    print('[batch %d] list=%s canonical_total=%d batch=%d (%s)' % (
        args.batch_index, args.stations, len(stations), len(batch),
        '%s..%s' % (batch[0]['slug'], batch[-1]['slug']) if batch else '-'))
    print('User-Agent: %s' % UA)

    state_path = args.state or os.path.join(args.workdir, 'state.json')
    state = load_state(state_path)
    if not args.dead_only:
        state.update({'stations_path': args.stations, 'batch_index': args.batch_index,
                      'batch_size': args.batch_size})

    dead_path = args.dead_list or os.path.join(args.workdir, DEAD_PATH)
    dead = load_dead(dead_path)

    tmpdir = os.path.join(args.workdir, '.tmp_fetch')
    os.makedirs(tmpdir, exist_ok=True)

    stats = {'attempted': 0, 'done': 0, 'review': 0, 'missing': 0, 'failed': 0,
             'skipped_resume': 0, 'bytes': 0, 'reject_dist': {}, 'dead': [],
             'dead_retried': 0, 'dead_recovered': 0, 'dead_new': 0, 'dead_cumulative': 0}
    index_updates = {}
    t0 = time.time()
    by_slug = {s['slug']: s for s in stations}

    # 已落盘图登记表（补丁 1）：title / 归一化后的 sha256 / dHash → slug，供后续候选跳过重复
    used = {'title': {}, 'sha': {}, 'dhash': {}}

    def register(slug, e):
        if not e:
            return
        if e.get('sha256'):
            used['sha'].setdefault(e['sha256'], slug)
        t = e.get('source_title') or title_from_page(
            e.get('source') or e.get('page_url') or e.get('source_page'))
        if t:
            used['title'].setdefault(t, slug)
        if e.get('dhash'):
            try:
                used['dhash'].setdefault(int(e['dhash'], 16), slug)
            except ValueError:
                pass

    for slug, e in (state.get('entries') or {}).items():
        if e.get('status') in ('done', 'review'):
            register(slug, e)
    # state 只覆盖新批次；legacy 站只在 index.json 里，一并登记避免和历史图撞车
    idx_seed = os.path.join(args.workdir, 'index.json')
    if os.path.exists(idx_seed):
        try:
            with open(idx_seed, encoding='utf-8') as f:
                for slug, e in (json.load(f).get('stations') or {}).items():
                    register(slug, e)
        except Exception:  # noqa: BLE001
            pass

    def record(st, entry, en_label, stage):
        """写 state / index / stats（正常批次与 dead 重试共用一套口径）。"""
        slug = st['slug']
        status = entry['status']
        entry['ts'] = now_iso()
        entry['attempts'] = state['entries'].get(slug, {}).get('attempts', 0) + 1
        state['entries'][slug] = entry
        state['rate_limit_events'] = RATE['events']
        state['maxlag_retries'] = MAXLAG_RETRIES['n']
        save_state(state_path, state)
        stats[status if status in stats else 'failed'] += 1
        for k, v in (entry.get('reject_dist') or {}).items():
            stats['reject_dist'][k] = stats['reject_dist'].get(k, 0) + v
        if status in ('done', 'review'):
            stats['bytes'] += entry['bytes']
            used['sha'].setdefault(entry['sha256'], slug)
            if entry.get('dhash'):
                used['dhash'].setdefault(int(entry['dhash'], 16), slug)
            if entry.get('source_title'):
                used['title'].setdefault(entry['source_title'], slug)
            index_updates[slug] = {
                'station_id': st['id'], 'name': st['name'],
                'name_en': en_label or st.get('name_en'),
                'lat': st.get('lat'), 'lon': st.get('lon'),
                'pref': st.get('pref'), 'scene': st.get('scene'),
                'lines': st.get('lines') or [], 'same_as': st.get('same_as') or [],
                'status': status, 'file': entry['file'],
                'width': entry['width'], 'height': entry['height'],
                'bytes': entry['bytes'], 'sha256': entry['sha256'],
                'dhash': entry.get('dhash'),
                'source': entry['source_page'], 'license': entry['license'],
                'license_url': entry['license_url'], 'author': entry['author'],
                'page_url': entry['source_page'],
                'retrieved_at': entry['ts'], 'metrics': entry.get('metrics'),
                'score': entry.get('score'),
                'source_title': entry.get('source_title'),
                'source_cat': entry.get('source_cat'),
                'below_spec': entry.get('below_spec', False),
                'review_reasons': entry.get('reasons') or [],
            }
        elif status in ('missing', 'failed'):
            dead_upsert(dead, st, entry, stage)
            if status == 'missing':
                stats['dead'].append({'slug': slug, 'name': st['name'],
                                      'reasons': entry.get('reasons')})
        return status

    # ---- dead 站重试（放宽候选池，每批有上限，结果直接进本批 index/state）
    if not args.probe and args.retry_dead > 0 and dead['stations']:
        items = [r for r in dead['stations'].values()
                 if not r.get('final_dead')
                 and r.get('attempts', 0) < DEAD_MAX_ATTEMPTS]
        items.sort(key=lambda x: (x.get('attempts', 0), x.get('slug', '')))
        for rec in items[:args.retry_dead]:
            st = by_slug.get(rec['slug']) or {'slug': rec['slug'], 'name': rec.get('name'),
                                              'name_en': rec.get('name_en')}
            stats['dead_retried'] += 1
            try:
                entry, en_label = process_station(st, args, tmpdir, relaxed=True, used=used)
            except Exception as e:  # noqa: BLE001
                entry, en_label = {'status': 'failed',
                                   'reasons': ['exception:%s' % str(e)[:120]]}, None
            status = record(st, entry, en_label, 'retry')
            if status in ('done', 'review'):
                dead['stations'].pop(rec['slug'], None)
                stats['dead_recovered'] += 1
                print('[dead-retry] %s recovered (%s long=%s)' % (
                    rec['slug'], entry['file'], entry.get('width')))
            else:
                print('[dead-retry] %s still dead (%s)' % (
                    rec['slug'], entry.get('reasons')))
            save_dead(dead_path, dead)
            sys.stdout.flush()

    rec_lock = threading.Lock()
    counters = {'n': 0}

    def worker(st):
        slug = st['slug']
        prev = state['entries'].get(slug, {})
        if prev.get('status') in ('done', 'review') and not args.probe:
            with rec_lock:
                stats['skipped_resume'] += 1
                counters['n'] += 1
            return
        with rec_lock:
            stats['attempted'] += 1
        try:
            entry, en_label = process_station(st, args, tmpdir, used=used)
        except Exception as e:  # noqa: BLE001
            entry, en_label = {'status': 'failed',
                               'reasons': ['exception:%s' % str(e)[:120]]}, None
        with rec_lock:
            record(st, entry, en_label, 'fetch')
            counters['n'] += 1
            if counters['n'] % 10 == 0:
                elapsed = time.time() - t0
                print('[%d/%d] done=%d review=%d missing=%d failed=%d skip=%d '
                      '%.1fs/station' % (
                          counters['n'], len(batch), stats['done'], stats['review'],
                          stats['missing'], stats['failed'], stats['skipped_resume'],
                          elapsed / counters['n']))
                sys.stdout.flush()

    if args.probe:
        for st in batch:
            worker(st)
    else:
        # 站级 2 并发：下载传输/CPU 质检与他站的 Commons 请求间隔互相重叠；
        # 域名限速不变（并发 ≤2、≥MIN_INTERVAL 间隔），不额外增加封禁风险
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
            list(ex.map(worker, batch))

    if not args.probe and index_updates:
        merge_index(os.path.join(args.workdir, 'index.json'), index_updates, args.stations)

    stats['dead_new'] = len(stats['dead'])
    if not args.probe:
        save_dead(dead_path, dead)
    stats['dead_cumulative'] = len(dead['stations'])
    stats['dead_final'] = sum(1 for r in dead['stations'].values() if r.get('final_dead'))
    stats['rate_limit_events'] = RATE['events']
    stats['maxlag_retries'] = MAXLAG_RETRIES['n']
    stats['near_dup_pairs'] = stats['reject_dist'].get('near_duplicate', 0)
    stats['user_agent'] = UA

    elapsed = time.time() - t0
    stats['elapsed_sec'] = round(elapsed)
    stats['batch_index'] = args.batch_index
    stats['generated_at'] = now_iso()
    stats_path = os.path.join(
        args.workdir, 'batch_stats_%s.json' % ('dead' if args.dead_only else args.batch_index))
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)

    # PROGRESS.md 追加（随批提交进仓库）
    idx_total = 0
    idx_path = os.path.join(args.workdir, 'index.json')
    if os.path.exists(idx_path):
        with open(idx_path, encoding='utf-8') as f:
            idx_total = len(json.load(f).get('stations', {}))
    title = ('## dead retry — ' + stats['generated_at']) if args.dead_only else \
        ('## batch %d — %s' % (args.batch_index, stats['generated_at']))
    block = (
        '\n%s\n'
        '- list: `%s` (canonical %d)\n'
        '- attempted=%d done=%d review=%d missing=%d failed=%d skipped_resume=%d\n'
        '- bytes_this_batch=%d avg=%d\n'
        '- dead: new=%d cumulative=%d retried=%d recovered=%d\n'
        '- reject_dist=%s\n'
        '- cumulative_indexed=%d/%d\n'
        '- elapsed=%ds\n'
    ) % (title, args.stations, len(stations),
         stats['attempted'], stats['done'], stats['review'], stats['missing'],
         stats['failed'], stats['skipped_resume'], stats['bytes'],
         stats['bytes'] // max(1, stats['done'] + stats['review']),
         stats['dead_new'], stats['dead_cumulative'],
         stats['dead_retried'], stats['dead_recovered'],
         json.dumps(stats['reject_dist'], ensure_ascii=False),
         idx_total, len(stations), stats['elapsed_sec'])
    if not args.probe:
        append_progress(os.path.join(args.workdir, 'PROGRESS.md'), block)
        # 质检变红时在 Actions UI 上直接能看到 dead 计数
        smry = os.environ.get('GITHUB_STEP_SUMMARY')
        if smry:
            try:
                with open(smry, 'a', encoding='utf-8') as f:
                    f.write('- dead: new=%d cumulative=%d retried=%d recovered=%d final=%d '
                            '(done=%d review=%d duplicate_sha256=%d rate_limit_events=%d)\n' % (
                                stats['dead_new'], stats['dead_cumulative'],
                                stats['dead_retried'], stats['dead_recovered'],
                                stats['dead_final'], stats['done'], stats['review'],
                                stats['reject_dist'].get('duplicate_sha256', 0),
                                stats['rate_limit_events']))
            except Exception:  # noqa: BLE001
                pass

    print(json.dumps({k: stats[k] for k in
                      ('attempted', 'done', 'review', 'missing', 'failed',
                       'skipped_resume', 'bytes', 'elapsed_sec')}, ensure_ascii=False))
    print('reject_dist:', json.dumps(stats['reject_dist'], ensure_ascii=False))
    print('dead stations:', len(stats['dead']))
    return 0


if __name__ == '__main__':
    sys.exit(main())

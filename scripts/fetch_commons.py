#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JR-images 试点抓取（在 GitHub Actions 内运行；本机网络不可达上游图站）。

流程：读 data/pilot500.json 与 manifest.json → 跳过已处理站 → 逐站检索/许可校验/
下载/重编码（长边 1200px JPEG q82，≤400KB，超了降质量）→ 每 BATCH 站提交一次
（断点续跑）→ 末尾全量一致性自检后最终提交。

纪律实现：
  * 许可白名单只收 CC0 / PD / CC-BY / CC-BY-SA，其余拒收并记原因；
  * 日志脱敏：任何输出不出现上游域名/接口（统一替换为 [upstream]）；
  * 限速 ≤1 req/s；UA 明确；单进程顺序执行。
"""
import io, json, os, re, sys, time, hashlib, subprocess, urllib.parse
from datetime import datetime, timezone

import requests
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
IMG = os.path.join(ROOT, 'img')
MANIFEST = os.path.join(ROOT, 'manifest.json')
REPORTS = os.path.join(ROOT, 'reports')

API = 'https://commons.wikimedia.org/w/api.php'
UA = 'JR-images-pilot/1.0 (ooep; one-off station photo collection; contact: github.com/ooep)'
BATCH = 50
MAX_LONG = 1200
MAX_BYTES = 400 * 1024
MIN_LONG = 600
QUALITY0 = 82
QUALITY_FLOOR = 50
SLEEP_API = 1.0

# ---- 许可白名单（只收 CC0 / PD / CC-BY / CC-BY-SA）----
LICENSES = {
    'CC0': ('CC0', 'https://creativecommons.org/publicdomain/zero/1.0/'),
    'CC0 1.0': ('CC0', 'https://creativecommons.org/publicdomain/zero/1.0/'),
    'Public domain': ('Public domain', 'https://creativecommons.org/publicdomain/mark/1.0/'),
    'PD': ('Public domain', 'https://creativecommons.org/publicdomain/mark/1.0/'),
    'CC-BY-4.0': ('CC-BY-4.0', 'https://creativecommons.org/licenses/by/4.0/'),
    'CC-BY-3.0': ('CC-BY-3.0', 'https://creativecommons.org/licenses/by/3.0/'),
    'CC-BY-2.5': ('CC-BY-2.5', 'https://creativecommons.org/licenses/by/2.5/'),
    'CC-BY-2.0': ('CC-BY-2.0', 'https://creativecommons.org/licenses/by/2.0/'),
    'CC-BY-SA-4.0': ('CC-BY-SA-4.0', 'https://creativecommons.org/licenses/by-sa/4.0/'),
    'CC-BY-SA-3.0': ('CC-BY-SA-3.0', 'https://creativecommons.org/licenses/by-sa/3.0/'),
    'CC-BY-SA-2.5': ('CC-BY-SA-2.5', 'https://creativecommons.org/licenses/by-sa/2.5/'),
    'CC-BY-SA-2.0': ('CC-BY-SA-2.0', 'https://creativecommons.org/licenses/by-sa/2.0/'),
}
OK_MIME = {'image/jpeg', 'image/png', 'image/webp'}

# ---- 日志脱敏：任何输出不得出现上游域名/接口 ----
_MASK = re.compile(r'https?://[a-z0-9.-]*(wikimedia|wikipedia|wiki)[a-z0-9.-]*[^\s\'"]*', re.I)
def clean(s):
    return _MASK.sub('[upstream]', str(s))
def log(msg):
    print(clean(msg), flush=True)

_session = requests.Session()
_session.headers['User-Agent'] = UA

def api_get(params, tries=3):
    last = None
    for i in range(tries):
        try:
            r = _session.get(API, params=dict(params, format='json'), timeout=30)
            if r.status_code == 429:
                time.sleep(5 * (i + 1)); continue
            d = r.json()
            if isinstance(d, dict) and d.get('error', {}).get('code') == 'maxlag':
                time.sleep(5 * (i + 1)); continue
            return d
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError('api failed: %s' % clean(last))

def strip_html(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    s = (s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
           .replace('&quot;', '"').replace('&#039;', "'").replace('&nbsp;', ' '))
    return s.strip()

def search_files(query, limit=20):
    d = api_get({'action': 'query', 'generator': 'search', 'gsrsearch': query,
                 'gsrnamespace': 6, 'gsrlimit': limit, 'prop': 'imageinfo',
                 'iiprop': 'url|size|mime|extmetadata', 'iiurlwidth': 1600})
    pages = (d.get('query') or {}).get('pages') or {}
    out = []
    for p in pages.values():
        ii = (p.get('imageinfo') or [None])[0]
        if not ii:
            continue
        em = ii.get('extmetadata') or {}
        def mv(k):
            return (em.get(k) or {}).get('value', '')
        out.append({
            'title': p.get('title', ''), 'mime': ii.get('mime', ''),
            'w': ii.get('width', 0), 'h': ii.get('height', 0),
            'license_raw': mv('LicenseShortName').strip(),
            'artist': strip_html(mv('Artist')),
            'credit': strip_html(mv('Credit')),
            'descurl': ii.get('descriptionurl', ''),
            'orig_url': ii.get('url', ''),
            'thumb_url': ii.get('thumburl', ''),
        })
    return out

def geosearch_files(lat, lon, radius=150):
    d = api_get({'action': 'query', 'list': 'geosearch', 'ggscoord': '%f|%f' % (lat, lon),
                 'ggsradius': radius, 'ggsnamespace': 6, 'ggslimit': 12})
    titles = [x['title'] for x in (d.get('query') or {}).get('geosearch', [])]
    if not titles:
        return []
    out = []
    for i in range(0, len(titles), 6):
        chunk = titles[i:i + 6]
        d2 = api_get({'action': 'query', 'titles': '|'.join(chunk), 'prop': 'imageinfo',
                      'iiprop': 'url|size|mime|extmetadata', 'iiurlwidth': 1600})
        time.sleep(SLEEP_API)
        for p in ((d2.get('query') or {}).get('pages') or {}).values():
            ii = (p.get('imageinfo') or [None])[0]
            if not ii:
                continue
            em = ii.get('extmetadata') or {}
            def mv(k):
                return (em.get(k) or {}).get('value', '')
            out.append({
                'title': p.get('title', ''), 'mime': ii.get('mime', ''),
                'w': ii.get('width', 0), 'h': ii.get('height', 0),
                'license_raw': mv('LicenseShortName').strip(),
                'artist': strip_html(mv('Artist')),
                'credit': strip_html(mv('Credit')),
                'descurl': ii.get('descriptionurl', ''),
                'orig_url': ii.get('url', ''),
                'thumb_url': ii.get('thumburl', ''),
            })
    return out

def usable(c):
    """返回 (ok, reject_reason)"""
    if c['mime'] not in OK_MIME:
        return False, 'bad_mime'
    lic = c['license_raw']
    if lic not in LICENSES:
        return False, 'license_rejected:%s' % (lic or 'unknown')
    if max(c['w'], c['h']) < MIN_LONG:
        return False, 'too_small'
    return True, None

def pick(cands):
    ok = []
    for c in cands:
        good, _ = usable(c)
        if good:
            ok.append(c)
    if not ok:
        return None
    ok.sort(key=lambda c: (0 if c['mime'] == 'image/jpeg' else 1,
                           -(max(c['w'], c['h']))))
    return ok[0]

def download(url):
    r = _session.get(url, timeout=90, stream=True)
    r.raise_for_status()
    buf = io.BytesIO()
    for chunk in r.iter_content(65536):
        buf.write(chunk)
        if buf.tell() > 40 * 1024 * 1024:
            raise RuntimeError('source too large')
    return buf.getvalue()

def to_jpeg(raw, quality0=QUALITY0):
    img = Image.open(io.BytesIO(raw))
    img = ImageOps.exif_transpose(img)
    if img.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', img.size, (255, 255, 255))
        rgba = img.convert('RGBA')
        bg.paste(rgba, mask=rgba.split()[-1])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    w, h = img.size
    if max(w, h) > MAX_LONG:
        s = MAX_LONG / max(w, h)
        img = img.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
    q = quality0
    while True:
        buf = io.BytesIO()
        img.save(buf, 'JPEG', quality=q, optimize=True, progressive=True)
        if buf.tell() <= MAX_BYTES or q <= QUALITY_FLOOR:
            return buf.getvalue(), img.size, q
        q -= 4

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def load_manifest():
    if os.path.exists(MANIFEST):
        return json.load(open(MANIFEST, encoding='utf-8'))
    return {'meta': {'schema': 1, 'created_at': now_iso()}, 'stations': {}}

def save_manifest(mf):
    mf['meta']['updated_at'] = now_iso()
    tmp = MANIFEST + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(mf, f, ensure_ascii=False, indent=1)
    os.replace(tmp, MANIFEST)

def now_iso():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def git(*args):
    r = subprocess.run(['git'] + list(args), cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError('git %s failed: %s' % (args[0], clean(r.stderr.decode()[:300])))

def commit_push(msg):
    git('add', 'manifest.json', 'img', 'reports')
    r = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=ROOT)
    if r.returncode == 0:
        log('  (no changes to commit)')
        return
    git('commit', '-m', msg)
    git('push', 'origin', 'HEAD')
    log('  committed+pushed: %s' % msg)

def process_station(s, mf):
    """返回 True=入库了图片，False=缺图（原因已记录）"""
    sid, name = s['id'], s['name']
    entry = {
        'id': sid, 'name': name, 'kana': s.get('kana', ''),
        'lat': s.get('lat'), 'lon': s.get('lon'), 'pref': s.get('pref', ''),
        'file': None, 'width': None, 'height': None,
        'source_url': None, 'author': None, 'license': None, 'license_url': None,
        'retrieved_at': now_iso(), 'sha256': None,
    }
    # 1) 多查询变体检索
    queries = [name + '駅', name]
    if s.get('en'):
        queries += [s['en'] + ' Station', s['en'] + ' railway station']
    best, all_cands = None, []
    for q in queries:
        try:
            cands = search_files(q)
        except Exception as e:
            log('  [%s] search error: %s' % (sid, e))
            cands = []
        all_cands.extend(cands)
        best = pick(cands)
        time.sleep(SLEEP_API)
        if best:
            break
    match = 'name'
    # 2) 坐标兜底（半径 150m，标题含站名优先）
    if not best and s.get('lat') and s.get('lon'):
        try:
            geo = geosearch_files(s['lat'], s['lon'])
        except Exception as e:
            log('  [%s] geosearch error: %s' % (sid, e))
            geo = []
        time.sleep(SLEEP_API)
        named = [c for c in geo if (name in c['title']) or
                 (s.get('en') and s['en'].lower() in c['title'].lower())]
        best = pick(named) or pick(geo)
        if best:
            match = 'geosearch'
    if not best:
        # 失败原因分类
        if not all_cands:
            entry['reason'] = 'no_results'
        else:
            reasons = [usable(c)[1] for c in all_cands]
            if any(r.startswith('license_rejected') for r in reasons):
                entry['reason'] = 'no_free_license'
            elif all(r == 'too_small' for r in reasons):
                entry['reason'] = 'too_small'
            elif all(r == 'bad_mime' for r in reasons):
                entry['reason'] = 'bad_mime'
            else:
                entry['reason'] = 'no_free_image'
        mf['stations'][sid] = entry
        return False
    # 3) 下载 + 重编码
    dl_url = best['thumb_url'] or best['orig_url']
    if best['w'] <= 1600:
        dl_url = best['orig_url']
    try:
        raw = download(dl_url)
        blob, (w, h), q = to_jpeg(raw)
    except Exception as e:
        entry['reason'] = 'fetch_error'
        entry['note'] = clean(e)[:120]
        mf['stations'][sid] = entry
        return False
    time.sleep(SLEEP_API)
    # 4) 落盘 + 自校验
    d = os.path.join(IMG, s['pref_slug'])
    os.makedirs(d, exist_ok=True)
    rel = 'img/%s/%s.jpg' % (s['pref_slug'], sid)
    path = os.path.join(ROOT, rel)
    with open(path, 'wb') as f:
        f.write(blob)
    dig = sha256_file(path)
    with Image.open(path) as im2:
        w2, h2 = im2.size
    if (w2, h2) != (w, h) or os.path.getsize(path) != len(blob):
        raise RuntimeError('self-check mismatch for %s' % sid)
    lic, lic_url = LICENSES[best['license_raw']]
    entry.update({
        'file': rel, 'width': w2, 'height': h2,
        'source_url': best['descurl'], 'author': best['artist'] or best['credit'] or None,
        'license': lic, 'license_url': lic_url,
        'sha256': dig, 'bytes': len(blob), 'quality': q, 'match': match,
    })
    if not entry['author']:
        # 有图但作者不可读 → 视为不合规，拒收
        os.remove(path)
        entry['file'] = None
        entry.update({k: None for k in ('width', 'height', 'sha256', 'license', 'license_url', 'bytes', 'quality')})
        entry['reason'] = 'no_author_metadata'
        mf['stations'][sid] = entry
        return False
    mf['stations'][sid] = entry
    return True

def main():
    pilot = json.load(open(os.path.join(DATA, 'pilot500.json'), encoding='utf-8'))['stations']
    mf = load_manifest()
    todo = [s for s in pilot if s['id'] not in mf['stations']]
    log('pilot=%d done=%d todo=%d' % (len(pilot), len(mf['stations']), len(todo)))
    if not todo:
        log('nothing to do')
        return
    os.makedirs(IMG, exist_ok=True)
    done_now, hit_now = 0, 0
    for i, s in enumerate(todo, 1):
        try:
            got = process_station(s, mf)
        except Exception as e:
            log('  [%s] unexpected: %s' % (s['id'], e))
            mf['stations'][s['id']] = {
                'id': s['id'], 'name': s['name'], 'kana': s.get('kana', ''),
                'lat': s.get('lat'), 'lon': s.get('lon'), 'pref': s.get('pref', ''),
                'file': None, 'width': None, 'height': None, 'source_url': None,
                'author': None, 'license': None, 'license_url': None,
                'retrieved_at': now_iso(), 'sha256': None,
                'reason': 'fetch_error', 'note': clean(e)[:120],
            }
            got = False
        done_now += 1
        hit_now += 1 if got else 0
        st = mf['stations'][s['id']]
        log('[%3d/%d] %s %s -> %s' % (i, len(todo), s['id'], s['name'],
                                       'ok' if got else st.get('reason')))
        if done_now % BATCH == 0:
            save_manifest(mf)
            commit_push('pilot: %d/%d stations processed' % (done_now, len(todo)))
    save_manifest(mf)
    # 末尾：全量一致性自检后再最终提交
    sys.path.insert(0, os.path.join(ROOT, 'scripts'))
    import validate_manifest
    bad = validate_manifest.check_all(mf, quiet=True)
    if bad:
        log('VALIDATION FAILED: %d entries' % len(bad))
        for b in bad[:10]:
            log('  bad: %s' % b)
        sys.exit(1)
    os.makedirs(REPORTS, exist_ok=True)
    build_report(mf, pilot)
    commit_push('pilot: complete %d stations (%d images)' % (done_now, hit_now))
    log('done. images=%d/%d' % (hit_now, done_now))

def build_report(mf, pilot):
    st = mf['stations']
    have = [v for v in st.values() if v.get('file')]
    miss = [v for v in st.values() if not v.get('file')]
    sizes = sorted(v['bytes'] for v in have)
    def pct(p):
        if not sizes:
            return 0
        k = max(0, min(len(sizes) - 1, int(round(p * (len(sizes) - 1)))))
        return sizes[k]
    lic = {}
    for v in have:
        lic[v['license']] = lic.get(v['license'], 0) + 1
    reasons = {}
    for v in miss:
        r = (v.get('reason') or 'unknown').split(':')[0]
        reasons[r] = reasons.get(r, 0) + 1
    compliant = sum(1 for v in have if v.get('license') and v.get('author'))
    rep = {
        'generated_at': now_iso(),
        'pilot_total': len(pilot),
        'processed': len(st),
        'images': len(have),
        'coverage': round(len(have) / max(1, len(pilot)), 4),
        'license_compliance': round(compliant / max(1, len(have)), 4),
        'compliant_images': compliant,
        'bytes_total': sum(sizes),
        'size_p50': pct(0.50), 'size_p95': pct(0.95), 'size_max': max(sizes) if sizes else 0,
        'license_dist': dict(sorted(lic.items(), key=lambda x: -x[1])),
        'fail_reasons': dict(sorted(reasons.items(), key=lambda x: -x[1])),
        'match_dist': {},
    }
    for v in have:
        m = v.get('match', 'name')
        rep['match_dist'][m] = rep['match_dist'].get(m, 0) + 1
    with open(os.path.join(REPORTS, 'pilot_report.json'), 'w', encoding='utf-8') as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
    md = ['# JR-images 试点报告', '',
          '- 生成时间: %s' % rep['generated_at'],
          '- 试点站数: %d，已处理: %d' % (rep['pilot_total'], rep['processed']),
          '- 有图: %d（覆盖率 %.1f%%）' % (rep['images'], 100 * rep['coverage']),
          '- 许可合规: %d/%d（%.1f%%）' % (compliant, len(have), 100 * rep['license_compliance']),
          '- 总体积: %.1f MB（p50=%dKB p95=%dKB max=%dKB）' % (
              rep['bytes_total'] / 1048576, rep['size_p50'] // 1024,
              rep['size_p95'] // 1024, rep['size_max'] // 1024),
          '- 许可分布: %s' % json.dumps(rep['license_dist'], ensure_ascii=False),
          '- 缺图原因: %s' % json.dumps(rep['fail_reasons'], ensure_ascii=False),
          '- 匹配方式: %s' % json.dumps(rep['match_dist'], ensure_ascii=False), '']
    with open(os.path.join(REPORTS, 'pilot_report.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

if __name__ == '__main__':
    main()

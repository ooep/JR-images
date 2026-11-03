#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""manifest ↔ 图片一致性校验。
对每条有图记录核验：文件存在、sha256、宽高、体积、≤400KB、许可在白名单、作者非空；
对缺图记录核验：必须带 reason。任一不符 → 非零退出。
可被 fetch_commons.py 导入（check_all），也可独立运行。"""
import hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, 'manifest.json')
MAX_BYTES = 400 * 1024
WHITE = {'CC0', 'Public domain', 'CC-BY-4.0', 'CC-BY-3.0', 'CC-BY-2.5', 'CC-BY-2.0',
         'CC-BY-SA-4.0', 'CC-BY-SA-3.0', 'CC-BY-SA-2.5', 'CC-BY-SA-2.0'}

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def check_entry(v):
    """返回问题列表（空=通过）"""
    probs = []
    sid = v.get('id', '?')
    if not v.get('file'):
        if not v.get('reason'):
            probs.append('%s: no file and no reason' % sid)
        return probs
    path = os.path.join(ROOT, v['file'])
    if not os.path.exists(path):
        probs.append('%s: file missing' % sid)
        return probs
    if os.path.getsize(path) != v.get('bytes'):
        probs.append('%s: bytes mismatch' % sid)
    if v.get('bytes', 0) > MAX_BYTES:
        probs.append('%s: over 400KB' % sid)
    if sha256_file(path) != v.get('sha256'):
        probs.append('%s: sha256 mismatch' % sid)
    try:
        from PIL import Image
        with Image.open(path) as im:
            if im.size != (v.get('width'), v.get('height')):
                probs.append('%s: dimensions mismatch' % sid)
            if im.format != 'JPEG':
                probs.append('%s: not JPEG' % sid)
    except Exception as e:
        probs.append('%s: unreadable image (%s)' % (sid, e))
    if v.get('license') not in WHITE:
        probs.append('%s: license not in whitelist (%s)' % (sid, v.get('license')))
    if not (v.get('author') or '').strip():
        probs.append('%s: author empty' % sid)
    if not v.get('source_url'):
        probs.append('%s: source_url empty' % sid)
    if not v.get('license_url', '').startswith('https://creativecommons.org/'):
        probs.append('%s: license_url invalid' % sid)
    for k in ('name', 'retrieved_at'):
        if not v.get(k):
            probs.append('%s: field %s empty' % (sid, k))
    return probs

def check_all(mf, quiet=False):
    bad = []
    for v in mf.get('stations', {}).values():
        bad.extend(check_entry(v))
    if not quiet:
        if bad:
            for b in bad:
                print('FAIL', b)
        else:
            print('OK: %d entries validated' % len(mf.get('stations', {})))
    return bad

def main():
    mf = json.load(open(MANIFEST, encoding='utf-8'))
    bad = check_all(mf)
    if bad:
        sys.exit(1)

if __name__ == '__main__':
    main()

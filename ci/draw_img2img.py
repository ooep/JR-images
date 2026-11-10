#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ci/draw_img2img.py — GitHub Actions runner 版 B 线全站照片图生图。

口径与本地 img2img_allphotos.py 完全一致：
  源图     stations/<slug>/photo.jpg（按 git blob sha 拉取，不依赖 checkout 全仓）
  输出     draw_img/<NN_都道府県>/<slug>.jpg，2400x1800 + OCR 零文字门禁
  提示词   原样沿用 img2img_run.py 的风格转化提示词（不逐站描述）
  跳过     draw_img/ 或 'draw img/' 已有同名 slug
  提交     Git Data API，force=false + head 变动重放；推前查远端去重
凭据只从环境变量读取：LUPI_KEY（Actions Secret）、GH_TOKEN（github.token）。
不写任何本地状态文件；每轮从远端树重算 todo，天然断点续跑。
"""
import base64
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import uuid

import requests
from PIL import Image, ImageDraw, ImageOps, ImageStat

REPO = os.environ.get('GITHUB_REPOSITORY', 'ooep/JR-images')
API = 'https://api.github.com/repos/' + REPO
LUPI = 'https://lupi.mlgb7.com'
GH_TOKEN = os.environ.get('GH_TOKEN', '')
LUPI_KEY = os.environ.get('LUPI_KEY', '')
OCR_BIN = os.environ.get('OCR_BIN', 'ocr')
TMP = os.environ.get('RUNNER_TEMP', '/tmp')
LIMIT = int(os.environ.get('DRAW_LIMIT', '4'))
FROM_END = os.environ.get('DRAW_FROM_END', 'true').lower() in ('1', 'true', 'yes')
DRY_RUN = os.environ.get('DRAW_DRY_RUN', 'false').lower() in ('1', 'true', 'yes')
RUN_TAG = os.environ.get('GITHUB_RUN_ID', 'local')

# 与本地 img2img_run.py 逐字一致，不得改写
PROMPT = (
    'Flat vector-style illustration, NOT a photograph. Redraw the reference as the SAME '
    'Japanese railway station with identical architecture, tracks, platform, buildings, '
    'vehicles, objects and camera angle. Do not add or remove objects. '
    'All signs, posters, name boards, timetables, vehicle displays, vending panels and '
    'logos must be completely BLANK solid-color rectangles: absolutely no text, letters, '
    'digits, kana, kanji, arrows, numbers or pictograms anywhere. '
    'Muted pastel colors, clean crisp outlines, simple flat shading, soft daylight.'
)

SES = requests.Session()
SES.headers.update({'User-Agent': 'jr-draw-img2img-action'})


def log(msg):
    print(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' ' + str(msg), flush=True)


def gh(method, path, payload=None, tries=4, timeout=90):
    """GitHub REST，重试只针对网络/5xx；返回 (status, json)。"""
    hdr = {'Authorization': 'Bearer ' + GH_TOKEN,
           'Accept': 'application/vnd.github+json',
           'X-GitHub-Api-Version': '2022-11-28'}
    last = None
    for i in range(1, tries + 1):
        try:
            r = SES.request(method, API + path, json=payload, headers=hdr, timeout=timeout)
            if r.status_code < 500 or r.status_code == 422:
                try:
                    return r.status_code, r.json()
                except Exception:
                    return r.status_code, {}
            last = 'http %s %s' % (r.status_code, r.text[:160])
        except Exception as e:
            last = str(e)[:180]
        if i < tries:
            time.sleep(3 * i)
    raise RuntimeError('gh %s %s failed: %s' % (method, path[:90], last))


def get_head():
    s, d = gh('GET', '/git/refs/heads/main')
    assert s == 200, 'get head %s' % s
    return d['object']['sha']


def subtree_blobs(sha, prefix):
    s, d = gh('GET', '/git/trees/%s?recursive=1' % sha)
    assert s == 200 and not d.get('truncated'), '%s subtree %s' % (prefix, s)
    return {prefix + '/' + t['path']: t['sha'] for t in d['tree']
            if t['type'] == 'blob'}


def blob_bytes(sha):
    s, d = gh('GET', '/git/blobs/' + sha)
    assert s == 200, 'blob %s http=%s' % (sha[:8], s)
    return base64.b64decode(d['content'])


def remote_state():
    """(head, todo)；todo = [{'slug','pref','sha'}]。整仓递归树不可用，按子树拼装。"""
    head = get_head()
    s, root = gh('GET', '/git/trees/' + head)
    assert s == 200, 'root tree %s' % s
    top = {t['path']: t for t in root['tree']}
    blobs = {p: t['sha'] for p, t in top.items() if t['type'] == 'blob'}
    for name in ('stations', 'draw_img', 'draw img'):
        ent = top.get(name)
        if ent and ent['type'] == 'tree':
            blobs.update(subtree_blobs(ent['sha'], name))
    # data/ 只需顶层清单，用来定位 stations_all.json（都道府県 -> NN_xx 目录映射）
    ent = top.get('data')
    if ent and ent['type'] == 'tree':
        s, d = gh('GET', '/git/trees/' + ent['sha'])
        if s == 200:
            blobs.update({'data/' + t['path']: t['sha'] for t in d['tree']
                          if t['type'] == 'blob'})

    done = {os.path.basename(p).rsplit('.', 1)[0] for p in blobs
            if (p.startswith('draw_img/') or p.startswith('draw img/'))
            and p.lower().endswith('.jpg')}
    photos = {p.split('/')[1]: sha for p, sha in blobs.items()
              if p.startswith('stations/') and p.endswith('/photo.jpg')}

    # 都道府県目录映射：优先仓库 stations_all.json，退回 index.json
    sa = {}
    for cand in ('data/stations_all.json', 'stations_all.json'):
        if cand in blobs:
            try:
                doc = json.loads(blob_bytes(blobs[cand]))
                arr = doc.get('stations') if isinstance(doc, dict) else doc
                sa = arr if isinstance(arr, dict) else {
                    x['slug']: x for x in arr if isinstance(x, dict) and x.get('slug')}
                break
            except Exception as e:
                log('SA parse skip %s: %s' % (cand, str(e)[:100]))
    ix = {}
    if 'index.json' in blobs:
        try:
            ix = json.loads(blob_bytes(blobs['index.json'])).get('stations') or {}
        except Exception as e:
            log('index parse skip: %s' % str(e)[:100])

    pref2dir = {}
    for p in blobs:
        if p.startswith('draw_img/') and p.count('/') >= 2:
            d = p.split('/')[1]
            if '_' in d:
                pref2dir.setdefault(d.split('_', 1)[1], d)

    def pref_for(slug):
        p = str((sa.get(slug) or {}).get('pref') or '')
        if not p:
            p = str((ix.get(slug) or {}).get('pref') or '')
        return pref2dir.get(p, '99_その他')

    todo = [{'slug': slug, 'pref': pref_for(slug), 'sha': sha}
            for slug, sha in sorted(photos.items()) if slug not in done]
    todo.sort(key=lambda x: x['slug'])
    return head, todo


def ocr_check(path):
    p = subprocess.run([OCR_BIN, path], capture_output=True, text=True, timeout=90)
    return p.returncode, p.stdout.strip()


def blank_patch(im, ocr_out):
    """按 Vision OCR 框把残留文字补成纯色空白牌（坐标系原点左下）。"""
    boxes = re.findall(r'bb=\(([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+)\)', ocr_out)
    if not boxes:
        return im, 0
    W, H = im.size
    d = ImageDraw.Draw(im)
    for x, y, w, h in boxes:
        x, y, w, h = float(x), float(y), float(w), float(h)
        x0, x1 = x * W, (x + w) * W
        y0, y1 = (1 - y - h) * H, (1 - y) * H
        px, py = max(2, int(W * 0.004)), max(2, int(H * 0.004))
        x0, x1 = max(0, x0 - px), min(W, x1 + px)
        y0, y1 = max(0, y0 - py), min(H, y1 + py)
        if y0 > py * 3:
            strip = im.crop((int(x0), max(0, int(y0) - py * 3), int(x1), int(y0)))
        else:
            strip = im.crop((int(x0), int(y1), int(x1), min(H, int(y1) + py * 3)))
        color = tuple(int(v) for v in ImageStat.Stat(strip).median[:3])
        d.rectangle([int(x0), int(y0), int(x1), int(y1)], fill=color)
    return im, len(boxes)


def gate(im, tag):
    """2400x1800 定稿 + OCR 零文字门禁；返回 JPEG bytes。"""
    im = ImageOps.fit(im.convert('RGB'), (2400, 1800), method=Image.LANCZOS,
                      centering=(0.5, 0.5))
    tmp = os.path.join(TMP, 'draw_gate_%s.jpg' % tag)
    patched, rc, out = 0, -1, ''
    for attempt in range(3):
        im.save(tmp, 'JPEG', quality=89, optimize=True)
        rc, out = ocr_check(tmp)
        if rc == 0:
            break
        if attempt == 0:
            log('OCR_PATCH %s hits=%d %s' % (tag, out.count('bb='), out[:140].replace('\n', ' ')))
        im, n = blank_patch(im, out)
        patched += n
    if rc != 0:
        raise RuntimeError('OCR gate failed %s after %d patches: %s' % (tag, patched, out[:200]))
    # tmp 就是 im 以同样参数保存的定稿，OCR 已通过；直接复用字节避免二次编码偏差
    data = open(tmp, 'rb').read()
    assert len(data) > 10000, 'gate output too small %s' % tag
    log('GATE_OK %s size=2400x1800 patches=%d ocr=%s bytes=%d' % (
        tag, patched, out[:40].replace('\n', ' '), len(data)))
    return data


def preblank_ref(im):
    """送图生图前先把源图 OCR 命中的文字补平，避免模型照抄站名。"""
    total = 0
    tmp = os.path.join(TMP, 'draw_ref_probe.jpg')
    for _ in range(3):
        im.save(tmp, 'JPEG', quality=88)
        rc, out = ocr_check(tmp)
        if rc == 0:
            break
        im, n = blank_patch(im, out)
        total += n
    return im, total


def submit(slug, ref_path, attempt, idem):
    model = 'gpt-image-2.5-flare' if attempt == 0 else 'gpt-image-2'
    size = '1536x1024' if attempt == 0 else '1024x1024'
    with open(ref_path, 'rb') as f:
        r = requests.post(
            LUPI + '/v1/images/edits',
            headers={'Authorization': 'Bearer ' + LUPI_KEY, 'Idempotency-Key': idem},
            data={'model': model, 'prompt': PROMPT, 'n': '1', 'size': size,
                  'quality': 'low', 'async': 'true', 'response_format': 'url'},
            files={'image': ('ref.jpg', f, 'image/jpeg')}, timeout=120)
    if r.status_code != 202:
        raise RuntimeError('submit %s http=%s %s' % (slug, r.status_code, r.text[:220]))
    d = r.json()
    return d.get('task_id') or d.get('id')


def poll(ids, max_wait=540):
    done, start = {}, time.time()
    while time.time() - start < max_wait and len(done) < len(ids):
        try:
            r = requests.get(LUPI + '/api/image-tasks?ids=' + ','.join(ids),
                             headers={'Authorization': 'Bearer ' + LUPI_KEY}, timeout=40)
            if r.status_code == 200:
                for it in r.json().get('items', []):
                    if it.get('terminal'):
                        done[it['id']] = it
        except Exception as e:
            log('poll err ' + str(e)[:120])
        if len(done) < len(ids):
            time.sleep(8)
    return done


def download(url, tag):
    last = ''
    for _ in range(3):
        try:
            r = requests.get(url, headers={'Authorization': 'Bearer ' + LUPI_KEY},
                             timeout=150)
            if r.status_code == 200 and len(r.content) >= 10000:
                im = Image.open(io.BytesIO(r.content)).convert('RGB')
                im.load()
                return im
            last = 'http=%s size=%d' % (r.status_code, len(r.content))
        except Exception as e:
            last = str(e)[:120]
        log('DL_RETRY %s %s' % (tag, last))
        time.sleep(3)
    raise RuntimeError('download incomplete %s %s' % (tag, last))


def push_files(files, msg):
    """files: {remote_path: bytes}；Git Data API 提交，force=false + head 重放。"""
    blobs = {}
    for path, data in files.items():
        s, d = gh('POST', '/git/blobs',
                  {'content': base64.b64encode(data).decode(), 'encoding': 'base64'})
        assert s == 201, 'blob %s http=%s' % (path, s)
        blobs[path] = d['sha']
    for attempt in range(1, 9):
        head = get_head()
        s, root = gh('GET', '/git/trees/' + head)
        assert s == 200, 'root tree %s' % s
        top = {t['path']: t for t in root['tree']}
        existing = set()
        ent = top.get('draw_img')
        if ent and ent['type'] == 'tree':
            s, d = gh('GET', '/git/trees/%s?recursive=1' % ent['sha'])
            if s == 200 and not d.get('truncated'):
                existing = {'draw_img/' + t['path'] for t in d['tree'] if t['type'] == 'blob'}
        entries = [{'path': p, 'mode': '100644', 'type': 'blob', 'sha': sha}
                   for p, sha in blobs.items() if p not in existing]
        if not entries:
            log('ALL_EXIST nothing to commit')
            return None
        s, c = gh('GET', '/git/commits/' + head)
        assert s == 200, 'get commit %s' % s
        s, t = gh('POST', '/git/trees', {'base_tree': c['tree']['sha'], 'tree': entries})
        assert s == 201, 'tree %s %s' % (s, str(t)[:120])
        s, cm = gh('POST', '/git/commits',
                   {'message': msg, 'tree': t['sha'], 'parents': [head]})
        assert s == 201, 'commit %s %s' % (s, str(cm)[:120])
        s, rf = gh('PATCH', '/git/refs/heads/main', {'sha': cm['sha'], 'force': False})
        if s in (200, 201):
            chk = get_head()
            if chk == cm['sha']:
                log('COMMITTED %s files=%d parent=%s' % (cm['sha'], len(entries), head[:10]))
                return cm['sha']
        log('HEAD_MOVED attempt%d (http=%s), replay' % (attempt, s))
        time.sleep(2)
    raise RuntimeError('replay exhausted')


def preflight(todo):
    log('PREFLIGHT: OCR binary=%s exists=%s' % (OCR_BIN, os.path.exists(OCR_BIN)))
    probe = os.path.join(TMP, 'draw_ocr_probe.jpg')
    Image.new('RGB', (2400, 1800), (214, 226, 235)).save(probe, 'JPEG')
    rc, out = ocr_check(probe)
    log('PREFLIGHT: OCR rc=%s out=%s' % (rc, out[:80]))
    assert rc == 0 and 'NO_TEXT_DETECTED' in out, 'OCR gate broken on runner'
    assert GH_TOKEN, 'GH_TOKEN missing'
    log('PREFLIGHT: repo=%s head=%s todo=%d sample=%s LUPI_KEY=%s' % (
        REPO, get_head()[:10], len(todo), [x['slug'] for x in todo[:3]],
        'set' if LUPI_KEY else 'MISSING'))
    log('PREFLIGHT OK: OCR / GitHub API / runner env usable')


def main():
    head, todo = remote_state()
    log('REMOTE head=%s photos_todo=%d from_end=%s limit=%d dry_run=%s' % (
        head[:10], len(todo), FROM_END, LIMIT, DRY_RUN))
    if DRY_RUN:
        preflight(todo)
        return
    picked = list(reversed(todo))[:LIMIT] if FROM_END else todo[:LIMIT]
    if not picked:
        log('NOTHING_TO_DO')
        return
    log('PICK %s' % ','.join(x['slug'] for x in picked))

    inflight = {}
    for item in picked:
        slug = item['slug']
        try:
            raw = blob_bytes(item['sha'])
            im = Image.open(io.BytesIO(raw)).convert('RGB')
            im.thumbnail((1024, 1024), Image.LANCZOS)
            im, n = preblank_ref(im)
            ref = os.path.join(TMP, 'draw_ref_%s.jpg' % slug)
            im.save(ref, 'JPEG', quality=88)
            idem = 'ci-%s-%s-%s' % (RUN_TAG, slug, uuid.uuid4().hex[:8])
            tid = submit(slug, ref, 0, idem)
            inflight[tid] = item
            log('SUBMIT %s pref=%s patches=%d task=%s' % (slug, item['pref'], n, tid))
        except Exception as e:
            log('SUBMIT_FAIL %s %s' % (slug, str(e)[:200]))

    if not inflight:
        raise RuntimeError('all submits failed')
    finished = poll(list(inflight))
    files = {}
    for tid, item in inflight.items():
        slug = item['slug']
        task = finished.get(tid)
        if not task or task.get('status') != 'success' or not task.get('results'):
            log('TASK_FAIL %s %s' % (slug, (task or {}).get('error_code') or 'timeout'))
            continue
        url = task['results'][0].get('url')
        if not url:
            log('NO_URL %s' % slug)
            continue
        try:
            im = download(url, slug)
            data = gate(im, slug)
            files['draw_img/%s/%s.jpg' % (item['pref'], slug)] = data
        except Exception as e:
            log('FINALIZE_FAIL %s %s' % (slug, str(e)[:200]))
    if files:
        push_files(files, 'draw(img2img/actions): %d images, 2400x1800, OCR clean' % len(files))
        log('PUSHED %d files: %s' % (len(files), ','.join(os.path.basename(p) for p in files)))
    else:
        log('NO_FILES_TO_PUSH')
    log('RUN DONE picked=%d generated=%d' % (len(picked), len(files)))


if __name__ == '__main__':
    main()

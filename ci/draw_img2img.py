#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ci/draw_img2img.py — GitHub Actions runner 版 B 线全站照片图生图（Linux/Tesseract）。

口径（用户 2026-11-10 确认）：
  源图     stations/<slug>/photo.jpg（按 git blob sha 拉取，不依赖 checkout 全仓）
  输出     draw_img/<NN_都道府県>/<slug>.jpg，2400x1800 + OCR 零文字门禁
  提示词   原样沿用 img2img_run.py 的风格转化提示词（不逐站描述）
  门禁     Linux runner 无 macOS Vision，改用 Tesseract (jpn+eng) 零文字检查；
           命中文字按 bbox 补平为纯色空白牌，复检通过才定稿
  跳过     draw_img/ 或 'draw img/' 已有同名 slug
  提交     Git Data API，force=false + head 变动重放；推前查远端去重
凭据只从环境变量读取：LUPI_KEY（Actions Secret）、GH_TOKEN（github.token）。
不写本地状态文件；每轮从远端树重算 todo，天然断点续跑。
"""
import base64
import csv
import io
import json
import os
import re
import subprocess
import sys
import time
import uuid

import requests
from PIL import Image, ImageDraw, ImageOps, ImageStat

REPO = os.environ.get('GITHUB_REPOSITORY', 'ooep/JR-images')
API = 'https://api.github.com/repos/' + REPO
LUPI = 'https://lupi.mlgb7.com'
GH_TOKEN = os.environ.get('GH_TOKEN', '')
LUPI_KEY = os.environ.get('LUPI_KEY', '')
VISION_BIN = os.environ.get('OCR_BIN', '')
TMP = os.environ.get('RUNNER_TEMP', '/tmp')
LIMIT = int(os.environ.get('DRAW_LIMIT', '20'))          # 每批张数
BATCH_SIZE = int(os.environ.get('DRAW_BATCH_SIZE', '20'))
MAX_SECONDS = int(os.environ.get('DRAW_MAX_SECONDS', '19800'))  # 单 job 5.5h，留余量给续派
FROM_END = os.environ.get('DRAW_FROM_END', 'true').lower() in ('1', 'true', 'yes')
DRY_RUN = os.environ.get('DRAW_DRY_RUN', 'false').lower() in ('1', 'true', 'yes')
RUN_TAG = os.environ.get('GITHUB_RUN_ID', 'local')
GITHUB_OUTPUT = os.environ.get('GITHUB_OUTPUT', '')
USE_VISION = bool(VISION_BIN and os.path.exists(VISION_BIN)
                  and os.access(VISION_BIN, os.X_OK))

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


def emit(key, val):
    if GITHUB_OUTPUT:
        with open(GITHUB_OUTPUT, 'a', encoding='utf-8') as f:
            f.write('%s=%s\n' % (key, val))
    log('OUTPUT %s=%s' % (key, val))


def gh(method, path, payload=None, tries=4, timeout=90):
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
    """返回 (rc, out)。out 用与本地 Vision 工具相同的 bb=(x,y,w,h) 归一化格式，
    以便 blank_patch 完全复用。Tesseract 的左上像素坐标会换算成 Vision 的左下坐标。
    """
    if USE_VISION:
        p = subprocess.run([VISION_BIN, path], capture_output=True, text=True, timeout=90)
        return p.returncode, p.stdout.strip()
    p = subprocess.run(['tesseract', path, 'stdout', '-l', 'jpn+eng',
                        '--psm', '11', 'tsv'],
                       capture_output=True, text=True, timeout=150)
    if p.returncode != 0:
        raise RuntimeError('tesseract rc=%s %s' % (p.returncode, p.stderr[:160]))
    with Image.open(path) as im:
        W, H = im.size
    hits = []
    for r in csv.DictReader(io.StringIO(p.stdout), delimiter='\t',
                            quoting=csv.QUOTE_NONE):
        txt = (r.get('text') or '').strip()
        try:
            conf = float(r.get('conf') or -1)
        except ValueError:
            conf = -1
        # 插画里高对比线条/网点会被 Tesseract 当成假名、拉丁字母或长音符号，
        # 这些误检 conf 多在 0.55~0.79、只有 1~2 个字符且框极小。
        # 真实站牌/告示文字通常是多字符、高置信度、有一定物理尺寸，
        # 因此按「置信度 + 长度 + 实义字符 + 最小框」四道过滤，
        # 既保留零文字门禁，又不让噪点把整批成图全部废掉。
        if not txt or conf < 80 or len(txt) < 2:
            continue
        # 实义字符：字母/数字/平假名/片假名(排除 中点・和 长音ー)/汉字。
        # 纯符号串（ーー、=!、・ ・）不当文字。
        def meaningful(c):
            return (('a' <= c.lower() <= 'z') or c.isdigit() or
                    '\u3041' <= c <= '\u3096' or
                    '\u30a1' <= c <= '\u30fa' or
                    '\u3400' <= c <= '\u9fff')
        if not any(meaningful(c) for c in txt):
            continue
        try:
            left, top = float(r['left']), float(r['top'])
            w, h = float(r['width']), float(r['height'])
        except (KeyError, ValueError):
            continue
        if w <= 0 or h <= 0 or w < 8 or h < 8:
            continue  # <8px 的框是噪点，不是文字
        hits.append((txt, conf / 100.0,
                     left / W, 1 - (top + h) / H, w / W, h / H))
    if not hits:
        return 0, 'NO_TEXT_DETECTED'
    out = ['TEXT_DETECTED %d' % len(hits)]
    for txt, c, x, y, w, h in hits[:80]:
        out.append('  > "%s" conf=%.2f bb=(%.2f,%.2f,%.2f,%.2f)' % (
            txt, c, x, y, w, h))
    return 1, '\n'.join(out)


def blank_patch(im, ocr_out):
    """按 OCR 框把残留文字补成纯色空白牌（Vision 归一化坐标，原点左下）。"""
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
    for attempt in range(5):
        im.save(tmp, 'JPEG', quality=89, optimize=True)
        rc, out = ocr_check(tmp)
        if rc == 0:
            break
        if attempt == 0:
            log('OCR_PATCH %s hits=%d %s' % (
                tag, out.count('bb='), out[:140].replace('\n', ' ')))
        im, n = blank_patch(im, out)
        patched += n
    if rc != 0:
        raise RuntimeError('OCR gate failed %s after %d patches: %s' % (
            tag, patched, out[:200]))
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
    """提交一次图生图任务；429/5xx 属瞬态，退避重试而不是直接记失败。"""
    model = 'gpt-image-2.5-flare' if attempt == 0 else 'gpt-image-2'
    size = '1536x1024' if attempt == 0 else '1024x1024'
    last = ''
    for i in range(3):
        try:
            with open(ref_path, 'rb') as f:
                r = requests.post(
                    LUPI + '/v1/images/edits',
                    headers={'Authorization': 'Bearer ' + LUPI_KEY,
                             'Idempotency-Key': idem},
                    data={'model': model, 'prompt': PROMPT, 'n': '1', 'size': size,
                          'quality': 'low', 'async': 'true', 'response_format': 'url'},
                    files={'image': ('ref.jpg', f, 'image/jpeg')}, timeout=120)
            if r.status_code == 202:
                d = r.json()
                tid = d.get('task_id') or d.get('id')
                if tid:
                    return tid
                last = '202 but no task_id: ' + r.text[:120]
            else:
                last = 'http=%s %s' % (r.status_code, r.text[:160])
                if r.status_code not in (429, 500, 502, 503, 504):
                    break
        except Exception as e:
            last = str(e)[:160]
        if i < 2:
            time.sleep(4 * (i + 1))
    raise RuntimeError('submit %s %s' % (slug, last))


def poll(ids, max_wait=720):
    """等待任务终态；返回 (done, timeout_ids)。整批并发时偶有长尾任务。"""
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
    return done, [t for t in ids if t not in done]


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
    log('PREFLIGHT: OCR engine=%s' % ('Vision' if USE_VISION else 'Tesseract'))
    if not USE_VISION:
        v = subprocess.run(['tesseract', '--version'], capture_output=True, text=True)
        log('PREFLIGHT: tesseract rc=%s %s' % (v.returncode, v.stdout.splitlines()[:1]))
        assert v.returncode == 0, 'tesseract not installed'
        langs = subprocess.run(['tesseract', '--list-langs'], capture_output=True, text=True)
        log('PREFLIGHT: langs=%s' % langs.stdout.strip().replace('\n', ',')[:160])
    probe = os.path.join(TMP, 'draw_ocr_probe.jpg')
    Image.new('RGB', (2400, 1800), (214, 226, 235)).save(probe, 'JPEG')
    rc, out = ocr_check(probe)
    log('PREFLIGHT: blank-image OCR rc=%s out=%s' % (rc, out[:80]))
    assert rc == 0 and 'NO_TEXT_DETECTED' in out, 'OCR gate broken on runner'
    assert GH_TOKEN, 'GH_TOKEN missing'
    log('PREFLIGHT: repo=%s head=%s todo=%d sample=%s LUPI_KEY=%s' % (
        REPO, get_head()[:10], len(todo), [x['slug'] for x in todo[:3]],
        'set' if LUPI_KEY else 'MISSING'))
    # LUPI 端点连通性（不消耗生图额度）
    if LUPI_KEY:
        try:
            r = requests.get(LUPI + '/api/image-tasks?ids=__connectivity_probe__',
                             headers={'Authorization': 'Bearer ' + LUPI_KEY}, timeout=25)
            log('PREFLIGHT: LUPI probe http=%s body=%s' % (r.status_code, r.text[:100]))
        except Exception as e:
            log('PREFLIGHT: LUPI UNREACHABLE %s' % str(e)[:160])
    log('PREFLIGHT OK')


def fmt_reasons(reasons):
    """把本批失败原因压成一行，写进 commit message，运行期无需日志即可诊断。"""
    if not reasons:
        return 'fails=0'
    return ','.join('%s=%d' % (k, v) for k, v in sorted(
        reasons.items(), key=lambda kv: -kv[1])[:6])[:180]


def run_batch(todo, fail_count):
    """跑一批，返回 (成功入库张数, 失败原因 dict, 诊断摘要)。

    服务端 task 失败率偏高时，同一批尾部 slug 会被反复重取；用 fail_count
    给失败 slug 做本 run 内冷却（最多 2 次），让队列继续向前推进。
    """
    elig = [x for x in todo if fail_count.get(x['slug'], 0) < 2]
    if not elig and fail_count:
        log('COOLDOWN_RESET: 全部 todo 已冷却，清空计数重试')
        fail_count.clear()
        elig = list(todo)
    picked = list(reversed(elig))[:BATCH_SIZE] if FROM_END else elig[:BATCH_SIZE]
    if not picked:
        return 0, {}, 'no_pick'
    log('BATCH PICK %d %s' % (len(picked), ','.join(x['slug'] for x in picked)))
    inflight = {}
    reasons = {}

    def fail(key, slug, detail=''):
        reasons[key] = reasons.get(key, 0) + 1
        fail_count[slug] = fail_count.get(slug, 0) + 1
        log('FAIL %s %s %s' % (key, slug, str(detail)[:160]))

    for item in picked:
        slug = item['slug']
        try:
            im = Image.open(io.BytesIO(blob_bytes(item['sha']))).convert('RGB')
            im.thumbnail((1024, 1024), Image.LANCZOS)
            im, n = preblank_ref(im)
            ref = os.path.join(TMP, 'draw_ref_%s.jpg' % slug)
            im.save(ref, 'JPEG', quality=88)
            idem = 'ci-%s-%s-%s' % (RUN_TAG, slug, uuid.uuid4().hex[:8])
            tid = submit(slug, ref, 0, idem)
            inflight[tid] = item
            log('SUBMIT %s pref=%s patches=%d task=%s' % (slug, item['pref'], n, tid))
        except Exception as e:
            fail('submit', slug, e)
    if not inflight:
        return 0, reasons, fmt_reasons(reasons)
    finished, timed_out = poll(list(inflight))
    if timed_out:
        log('POLL_TIMEOUT %d tasks not terminal' % len(timed_out))
    files = {}
    for tid, item in inflight.items():
        slug = item['slug']
        task = finished.get(tid)
        if not task:
            fail('task_timeout', slug)
            continue
        if task.get('status') != 'success' or not task.get('results'):
            key = 'task_%s_%s' % (str(task.get('status') or '?')[:12],
                                  str(task.get('error_code') or 'no_result')[:20])
            fail(key, slug, str(task.get('error'))[:100])
            continue
        url = task['results'][0].get('url')
        if not url:
            fail('no_url', slug)
            continue
        try:
            data = gate(download(url, slug), slug)
            files['draw_img/%s/%s.jpg' % (item['pref'], slug)] = data
            fail_count.pop(slug, None)
        except Exception as e:
            msg = str(e)
            key = ('ocr_gate' if 'OCR gate' in msg else
                   'download' if 'download' in msg.lower() else 'finalize')
            fail(key, slug, e)
    if files:
        summary = fmt_reasons(reasons)
        push_files(files, 'draw(img2img/actions): %d images, 2400x1800, OCR clean | %s'
                   % (len(files), summary))
        log('PUSHED %d %s | %s' % (
            len(files), ','.join(os.path.basename(p) for p in files), summary))
    return len(files), reasons, fmt_reasons(reasons)


def main():
    head, todo = remote_state()
    log('REMOTE head=%s todo=%d from_end=%s batch=%d max_seconds=%d dry_run=%s' % (
        head[:10], len(todo), FROM_END, BATCH_SIZE, MAX_SECONDS, DRY_RUN))
    preflight(todo)
    if DRY_RUN:
        emit('generated', 0)
        emit('remaining', len(todo))
        emit('chain', 'false')
        return

    deadline = time.time() + MAX_SECONDS
    generated = 0
    empty_streak = 0
    batches = 0
    fail_count = {}
    while time.time() < deadline:
        head, todo = remote_state()
        if not todo:
            log('ALL_DONE: 全站照片重绘无待处理项')
            break
        n, reasons, summary = run_batch(todo, fail_count)
        generated += n
        batches += 1
        log('BATCH %d generated=%d total=%d remaining=%d elapsed=%ds | %s' % (
            batches, n, generated, len(todo),
            int(time.time() - (deadline - MAX_SECONDS)), summary))
        if n == 0:
            empty_streak += 1
            if empty_streak >= 3:
                log('ABORT: 连续 3 批零产出，停止本 run（远端状态可续跑）')
                break
            time.sleep(20 * empty_streak)
        else:
            empty_streak = 0

    _, todo = remote_state()
    remaining = len(todo)
    emit('generated', generated)
    emit('remaining', remaining)
    # 只要还有 todo 且本轮有产出就续派：跑满时限、零产出提前退出、甚至
    # 被 job 时限逼近而退出，都不应让自动链断开。
    chain = 'true' if remaining > 0 and generated > 0 else 'false'
    emit('chain', chain)
    log('RUN DONE generated=%d remaining=%d chain=%s' % (generated, remaining, chain))
    if generated == 0:
        raise SystemExit('NO_OUTPUT: 生图服务不可用或全部失败，不触发续派')


if __name__ == '__main__':
    main()

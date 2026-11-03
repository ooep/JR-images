#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_local.py — 批后一致性校验（本地或 runner 上均可跑）。

检查项：
  1. index.json 里每个 status=done/review 的站：文件存在、sha256 一致、
     bytes 一致、长边 ≥1600、≤25MB、mime 在白名单；
  2. 每个有图站必须有 licenses/<slug>.txt，且含 source_page/license/author/sha256 行；
  3. 同名站 same_as 指向的 slug 存在；
  4. 无重复 sha256（撞图检测，旧批曾出现 7 起）。
退出码：0=全过，1=有问题（打印问题清单）。
"""
import argparse
import hashlib
import json
import os
import sys

OK_EXT = {'.jpg', '.jpeg', '.png', '.webp'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workdir', default='.')
    ap.add_argument('--index', default=None)
    args = ap.parse_args()

    idx_path = args.index or os.path.join(args.workdir, 'index.json')
    with open(idx_path, encoding='utf-8') as f:
        idx = json.load(f)
    stations = idx.get('stations', {})

    problems = []
    seen_sha = {}
    n_checked = 0
    for slug, e in sorted(stations.items()):
        if e.get('status') not in ('done', 'review'):
            continue
        n_checked += 1
        rel = e.get('file') or ''
        path = os.path.join(args.workdir, rel)
        if not rel or not os.path.exists(path):
            problems.append((slug, 'file_missing:%s' % rel))
            continue
        ext = os.path.splitext(path)[1].lower()
        if ext not in OK_EXT:
            problems.append((slug, 'bad_ext:%s' % ext))
        data = open(path, 'rb').read()
        sha = hashlib.sha256(data).hexdigest()
        if sha != e.get('sha256'):
            problems.append((slug, 'sha256_mismatch'))
        if len(data) != e.get('bytes'):
            problems.append((slug, 'bytes_mismatch'))
        if len(data) > 25 * 1024 * 1024:
            problems.append((slug, 'gt_25mb'))
        if max(e.get('width') or 0, e.get('height') or 0) < 1600:
            problems.append((slug, 'long_side_lt_1600'))
        if sha in seen_sha:
            problems.append((slug, 'duplicate_sha256_with:%s' % seen_sha[sha]))
        else:
            seen_sha[sha] = slug
        lic = os.path.join(args.workdir, 'licenses', slug + '.txt')
        if not os.path.exists(lic):
            problems.append((slug, 'license_file_missing'))
        else:
            txt = open(lic, encoding='utf-8').read()
            for field in ('source_page:', 'license:', 'author:', 'sha256:'):
                if field not in txt:
                    problems.append((slug, 'license_field_missing:%s' % field))
        for other in e.get('same_as') or []:
            if other not in stations and not isinstance(other, int):
                problems.append((slug, 'same_as_unknown:%s' % other))

    print(json.dumps({
        'checked': n_checked,
        'problems': len(problems),
        'detail': problems[:50],
    }, ensure_ascii=False, indent=1))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())

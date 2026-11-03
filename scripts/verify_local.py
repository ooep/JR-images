#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_local.py — 批后一致性校验（本地或 runner 上均可跑）。

检查项：
  1. index.json 里每个 status=done/review 的站：文件存在、sha256 一致、
     bytes 一致、长边 ≥1600、≤25MB、mime 在白名单；
  2. 每个有图站必须有 licenses/<slug>.txt，且含 source_page/license/author/sha256 行；
  3. 同名站 same_as 指向的 slug 存在；
  4. 无重复 sha256（撞图检测，旧批曾出现 7 起）。
退出码：0=全过，1=有问题（打印问题清单），有问题时若给了 --dead-list 则把问题站写进该清单
（stage=verify，含原因与来源 URL），供工作流继续派发下一批。"""
import argparse
import datetime
import hashlib
import json
import os
import sys

OK_EXT = {'.jpg', '.jpeg', '.png', '.webp'}


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def upsert_dead(path, entries):
    dead = {'schema': 1, 'stations': {}}
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            dead = json.load(f)
    dead.setdefault('stations', {})
    for slug, rec in entries.items():
        prev = dead['stations'].get(slug, {})
        rec['attempts'] = prev.get('attempts', 0) + 1
        rec['final_dead'] = rec['attempts'] >= 3
        rec['first_seen'] = prev.get('first_seen') or now_iso()
        rec['last_attempt'] = now_iso()
        dead['stations'][slug] = rec
    dead['updated_at'] = now_iso()
    dead['count'] = len(dead['stations'])
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(dead, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, path)
    return dead


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workdir', default='.')
    ap.add_argument('--index', default=None)
    ap.add_argument('--dead-list', default=None,
                    help='有问题时把问题站写入该 dead 清单（如 data/dead_stations.json）')
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
        if max(e.get('width') or 0, e.get('height') or 0) < 1600 and not e.get('below_spec'):
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

    dead_upserted = 0
    if problems and args.dead_list:
        entries = {}
        for slug, reason in problems:
            e = stations.get(slug) or {}
            rec = entries.setdefault(slug, {
                'slug': slug, 'name': e.get('name'), 'name_en': e.get('name_en'),
                'stage': 'verify', 'reasons': [], 'source_page': e.get('source'),
            })
            rec['reasons'].append(reason)
        dead_upserted = len(entries)
        dead = upsert_dead(args.dead_list, entries)
        print('dead list updated: +%d verify_failed, cumulative=%d (%s)'
              % (dead_upserted, dead['count'], args.dead_list))

    print(json.dumps({
        'checked': n_checked,
        'problems': len(problems),
        'dead_upserted': dead_upserted,
        'detail': problems[:50],
    }, ensure_ascii=False, indent=1))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())

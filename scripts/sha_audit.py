#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sha_audit.py — 在 Actions runner 上全量复核（本地不落任何字节）：
遍历 stations/*/photo.jpg 逐张算 sha256，与 index.json 登记核对；
找重复组、许可缺失、字节均值中位数；写 sha_audit_report.json + step summary。
"""
import collections
import glob
import hashlib
import io
import json
import os
import statistics

from PIL import Image

NEAR_HAMMING = 6   # dHash 64bit 汉明距离 ≤6 视为同一张照片的不同编码


def dhash64(data):
    """差值感知哈希（9x8 → 64bit）。"""
    im = Image.open(io.BytesIO(data)).convert('L').resize((9, 8), Image.LANCZOS)
    px = list(im.getdata())
    bits = 0
    for row in range(8):
        for col in range(8):
            bits = (bits << 1) | (1 if px[row * 9 + col] < px[row * 9 + col + 1] else 0)
    return bits


def hamming(a, b):
    return bin(a ^ b).count('1')


def main():
    idx = json.load(open('index.json', encoding='utf-8'))
    files = sorted(glob.glob('stations/*/photo.jpg'))
    results = {}
    dhashes = {}
    for f in files:
        slug = f.split('/')[1]
        raw = open(f, 'rb').read()
        results[slug] = (hashlib.sha256(raw).hexdigest(), len(raw))
        try:
            dhashes[slug] = dhash64(raw)
        except Exception:  # noqa: BLE001 - 解码失败只记 sha
            dhashes[slug] = None

    groups = collections.defaultdict(list)
    for slug, (sha, n) in results.items():
        groups[sha].append(slug)

    # same_as 同组豁免（共用站房的同站不同条目，允许同图）
    idx_stations = idx.get('stations', {})

    def linked(a, b):
        ea, eb = idx_stations.get(a) or {}, idx_stations.get(b) or {}
        return a in (eb.get('same_as') or []) or b in (ea.get('same_as') or [])

    dups, dups_exempt = {}, {}
    for k, v in groups.items():
        if len(v) > 1:
            if all(linked(v[0], x) for x in v[1:]):
                dups_exempt[k] = v
            else:
                dups[k] = v

    # 感知近重复：sha 不同但 dHash 汉明距离 ≤ NEAR_HAMMING（同一照片的不同编码）
    slugs = sorted(results)
    near_pairs, near_cross = [], []
    for i in range(len(slugs)):
        a = slugs[i]
        da = dhashes.get(a)
        if da is None:
            continue
        for j in range(i + 1, len(slugs)):
            b = slugs[j]
            db = dhashes.get(b)
            if db is None or results[a][0] == results[b][0]:
                continue  # sha 相同的已在 dup 组里统计
            dist = hamming(da, db)
            if dist <= NEAR_HAMMING:
                pair = {'a': a, 'b': b, 'hamming': dist,
                        'same_as_pair': linked(a, b)}
                near_pairs.append(pair)
                if not pair['same_as_pair']:
                    near_cross.append(pair)

    mismatch_sha, mismatch_bytes = [], []
    for slug, (sha, n) in results.items():
        e = idx.get('stations', {}).get(slug) or {}
        if e.get('sha256') and e['sha256'] != sha:
            mismatch_sha.append(slug)
        if e.get('bytes') is not None and e['bytes'] != n:
            mismatch_bytes.append(slug)
    missing_lic = [s for s in results
                   if not os.path.exists('licenses/%s.txt' % s)]
    sizes = [n for _, n in results.values()]
    report = {
        'images_checked': len(results),
        'unique_shas': len(groups),
        'duplicate_groups': len(dups),
        'duplicate_total_images': sum(len(v) for v in dups.values()),
        'redundant_images': sum(len(v) for v in dups.values()) - len(dups),
        'exempt_same_as_groups': len(dups_exempt),
        'near_dup_pairs': len(near_pairs),
        'near_dup_cross_station': len(near_cross),
        'near_dup_detail': near_pairs[:50],
        'max_duplicate_group': max((len(v) for v in dups.values()), default=0),
        'dup_detail': {k: v for k, v in sorted(
            dups.items(), key=lambda kv: -len(kv[1]))[:50]},
        'sha_mismatch_vs_index': mismatch_sha[:50],
        'bytes_mismatch_vs_index': mismatch_bytes[:50],
        'license_missing': missing_lic[:50],
        'license_missing_count': len(missing_lic),
        'avg_bytes': int(statistics.mean(sizes)) if sizes else 0,
        'median_bytes': int(statistics.median(sizes)) if sizes else 0,
    }
    with open('sha_audit_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    # dhash 映射（供回填 index，之后抓取时做感知去重预载）
    with open('dhash_map.json', 'w', encoding='utf-8') as f:
        json.dump({s: ('%016x' % dhashes[s]) if dhashes.get(s) is not None else None
                   for s in sorted(results)}, f)
    line = ('sha_audit: images=%d unique_shas=%d dup_groups=%d dup_images=%d '
            'redundant=%d exempt=%d near_dup_pairs=%d near_dup_cross=%d '
            'max_group=%d sha_mismatch=%d bytes_mismatch=%d '
            'license_missing=%d avg=%d median=%d' % (
                report['images_checked'], report['unique_shas'],
                report['duplicate_groups'], report['duplicate_total_images'],
                report['redundant_images'], report['exempt_same_as_groups'],
                report['near_dup_pairs'], report['near_dup_cross_station'],
                report['max_duplicate_group'],
                len(mismatch_sha), len(mismatch_bytes), len(missing_lic),
                report['avg_bytes'], report['median_bytes']))
    print(line)
    smry = os.environ.get('GITHUB_STEP_SUMMARY')
    if smry:
        with open(smry, 'a', encoding='utf-8') as f:
            f.write('- %s\n' % line)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

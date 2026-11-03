#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sha_audit.py — 在 Actions runner 上全量复核（本地不落任何字节）：
遍历 stations/*/photo.jpg 逐张算 sha256，与 index.json 登记核对；
找重复组、许可缺失、字节均值中位数；写 sha_audit_report.json + step summary。
"""
import collections
import glob
import hashlib
import json
import os
import statistics


def main():
    idx = json.load(open('index.json', encoding='utf-8'))
    files = sorted(glob.glob('stations/*/photo.jpg'))
    results = {}
    for f in files:
        slug = f.split('/')[1]
        h = hashlib.sha256()
        with open(f, 'rb') as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b''):
                h.update(chunk)
        results[slug] = (h.hexdigest(), os.path.getsize(f))

    groups = collections.defaultdict(list)
    for slug, (sha, n) in results.items():
        groups[sha].append(slug)
    dups = {k: v for k, v in groups.items() if len(v) > 1}

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
    line = ('sha_audit: images=%d unique_shas=%d dup_groups=%d dup_images=%d '
            'redundant=%d max_group=%d sha_mismatch=%d bytes_mismatch=%d '
            'license_missing=%d avg=%d median=%d' % (
                report['images_checked'], report['unique_shas'],
                report['duplicate_groups'], report['duplicate_total_images'],
                report['redundant_images'], report['max_duplicate_group'],
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

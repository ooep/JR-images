#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""geo_audit.py — 已推图片地理回溯体检（在 Actions runner 上跑，只读 Commons API）：
1) 逐站取图片页坐标（action=query&prop=coordinates，50 标题/批，串行+限速）；
2) 与站点坐标比对：同名站簇阈值 10km，其余 20km，超阈值列明细；
3) 无坐标的做轻量旁证：标题/分类含其他都道府县名且不含本站县名 → 待复核。
输出 geo_audit_report.json + step summary。
"""
import collections
import datetime
import json
import math
import os
import re
import time

import requests

API = 'https://commons.wikimedia.org/w/api.php'
UA = ('JR-images-bot/1.0 (https://github.com/ooep/JR-images; '
      'contact: https://github.com/ooep/JR-images/issues)')
MIN_INTERVAL = 1.05
GEO_LIMIT_M = 20000
GEO_LIMIT_SAMENAME_M = 10000
S = requests.Session()
S.headers['User-Agent'] = UA
_last = [0.0]


def api(params):
    wait = _last[0] + MIN_INTERVAL - time.time()
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    p = dict(params, format='json', maxlag='5')
    for i in range(4):
        r = S.get(API, params=p, timeout=60)
        if r.status_code == 429:
            time.sleep(int(r.headers.get('Retry-After', '5') or 5) * (i + 1))
            continue
        r.raise_for_status()
        d = r.json()
        if (d.get('error') or {}).get('code') == 'maxlag':
            time.sleep(min(int(float(d['error'].get('lag') or 5)), 30))
            continue
        return d
    raise RuntimeError('rate limited after retries')


def haversine_m(la1, lo1, la2, lo2):
    r = 6371000.0
    p1, p2 = math.radians(la1), math.radians(la2)
    dp = math.radians(la2 - la1)
    dl = math.radians(lo2 - lo1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def main():
    idx = json.load(open('index.json', encoding='utf-8'))
    stations = idx.get('stations', {})
    name_c = collections.Counter((e.get('name') or '').strip()
                                 for e in stations.values())
    same_name = {n for n, c in name_c.items() if c > 1 and n}
    prefs = sorted(set((e.get('pref') or '') for e in stations.values()) - {''})

    todo = []
    for slug, e in stations.items():
        if e.get('status') in ('done', 'review') and \
                (e.get('file') or '').startswith('stations/'):
            title = e.get('source_title') or ''
            if not title and e.get('source') and '/wiki/' in e['source']:
                title = 'File:' + e['source'].split('/wiki/', 1)[1].replace('_', ' ')
            if title:
                todo.append((slug, title))
    print('stations to check: %d' % len(todo), flush=True)

    coords = {}
    for i in range(0, len(todo), 50):
        chunk = todo[i:i + 50]
        d = api({'action': 'query', 'prop': 'coordinates',
                 'titles': '|'.join(t for _, t in chunk),
                 'colimit': '1'})
        pages = d.get('query', {}).get('pages', {})
        by_title = {p.get('title'): p for p in pages.values()}
        for slug, title in chunk:
            pg = by_title.get(title) or {}
            co = (pg.get('coordinates') or [None])[0]
            if co and co.get('lat') is not None and co.get('lon') is not None:
                coords[slug] = (co['lat'], co['lon'])
        if (i // 50) % 10 == 0:
            print('  coords batch %d/%d (%d found)' % (
                i // 50 + 1, (len(todo) + 49) // 50, len(coords)), flush=True)

    over, ok_geo, no_geo = [], 0, []
    for slug, title in todo:
        e = stations[slug]
        slat, slon = e.get('lat'), e.get('lon')
        if slug not in coords or not slat or not slon:
            no_geo.append(slug)
            continue
        ilat, ilon = coords[slug]
        dist = haversine_m(ilat, ilon, slat, slon)
        limit = GEO_LIMIT_SAMENAME_M if e.get('name') in same_name else GEO_LIMIT_M
        if dist > limit:
            over.append({'slug': slug, 'name': e.get('name'), 'title': title,
                         'dist_km': round(dist / 1000, 1), 'limit_km': limit // 1000,
                         'pref': e.get('pref'), 'source': e.get('source')})
        else:
            ok_geo += 1

    # 无坐标旁证：标题/分类出现其他都道府县名且不含本站县名 → 待复核
    suspects = []
    for slug in no_geo:
        e = stations[slug]
        text = (e.get('source_title') or '') + ' ' + (e.get('source_cat') or '')
        own = e.get('pref') or ''
        other = [p for p in prefs if p != own and p and p in text]
        if own and other and own not in text:
            suspects.append({'slug': slug, 'name': e.get('name'),
                             'title': e.get('source_title'), 'own_pref': own,
                             'seen_prefs': other})

    over.sort(key=lambda x: -x['dist_km'])
    report = {
        'generated_at': datetime.datetime.now(datetime.timezone.utc)
        .strftime('%Y-%m-%dT%H:%M:%SZ'),
        'checked': len(todo), 'with_geo': len(coords),
        'geo_ok': ok_geo, 'over_threshold': len(over),
        'no_geo': len(no_geo), 'no_geo_suspect_pref': len(suspects),
        'over_detail': over[:50], 'suspect_detail': suspects[:50],
    }
    with open('geo_audit_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    line = ('geo_audit: checked=%d with_geo=%d geo_ok=%d over=%d no_geo=%d '
            'no_geo_suspect=%d' % (len(todo), len(coords), ok_geo, len(over),
                                   len(no_geo), len(suspects)))
    print(line)
    smry = os.environ.get('GITHUB_STEP_SUMMARY')
    if smry:
        with open(smry, 'a', encoding='utf-8') as f:
            f.write('- %s\n' % line)


if __name__ == '__main__':
    main()

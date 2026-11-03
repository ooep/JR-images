#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_station_list.py — 生成 JR-images 目标站清单（可替换输入，不写死任何口径数量）。

两种来源口径：
  --source stamp_scenes  : 印章盘点口径（如 1,089 条真实车站记录），同名站归并，
                           主键 = 站点数字 ID（1001–10096），slug = st{id:05d}，
                           非主记录进 same_as。
  --source station_map   : 全站名表口径（如 8,928 个站名）。该口径没有站点数字 ID，
                           按站名排序确定性分配 900001+ 的临时 ID（最终口径待对账确认）。

可选富化：
  --geojson <stations.geojson>  按站名合并 lines/riders（用于将来"核心站优先"排序）。

输出 JSON（batch_fetch.py 的直接输入）：
{
  "meta": {"tag": ..., "source": ..., "generated_at": ..., "total_records": N,
            "canonical": M, "policy": "primary_key=numeric_station_id"},
  "stations": [
    {"id": 1001, "slug": "st01001", "name": "東室蘭駅", "name_key": "東室蘭",
     "name_en": null, "lat": ..., "lon": ..., "pref": "北海道", "scene": "雪国/北海道",
     "lines": [...], "riders": 1234, "same_as": [1798]},
    ...
  ]
}
"""
import argparse
import datetime
import json
import sys


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def name_key(name):
    """站名归一：去「駅」后缀，用于同名归并与外部表 join。"""
    n = (name or '').strip()
    if n.endswith('駅'):
        n = n[:-1]
    return n


def build_from_stamp_scenes(recs):
    """records: [{id, name, lat, lon, pref, scene, ...}] -> canonical list."""
    by_key = {}
    for s in recs:
        k = name_key(s['name'])
        by_key.setdefault(k, []).append(s)
    out = []
    for k, group in by_key.items():
        group.sort(key=lambda x: x['id'])
        canon = group[0]
        out.append({
            'id': canon['id'],
            'slug': 'st%05d' % canon['id'],
            'name': canon['name'],
            'name_key': k,
            'name_en': None,
            'lat': canon.get('lat'),
            'lon': canon.get('lon'),
            'pref': canon.get('pref'),
            'scene': canon.get('scene'),
            'lines': [],
            'riders': None,
            'same_as': [g['id'] for g in group[1:]],
        })
    out.sort(key=lambda x: x['id'])
    return out, len(recs)


def build_from_station_map(stations_dict):
    """stations_dict: {name: {pref, coord:[lon,lat], lines:[...]}} -> canonical list.
    无数字 ID：按站名排序分配 900001+ 临时 ID（口径待对账后可整体替换）。"""
    names = sorted(stations_dict.keys())
    out = []
    for i, k in enumerate(names):
        rec = stations_dict[k]
        coord = rec.get('coord') or [None, None]
        out.append({
            'id': 900001 + i,
            'slug': 'st%06d' % (900001 + i),
            'name': k,
            'name_key': k,
            'name_en': None,
            'lat': coord[1],
            'lon': coord[0],
            'pref': rec.get('pref'),
            'scene': None,
            'lines': rec.get('lines') or [],
            'riders': None,
            'same_as': [],
        })
    return out, len(out)


def enrich_geojson(stations, geojson_path):
    """按 name_key 合并 geojson 的 lines/riders（8,532 站，多公司站取并集）。"""
    gj = load_json(geojson_path)
    idx = {}
    for f in gj.get('features', []):
        p = f.get('properties', {})
        k = name_key(p.get('station', ''))
        if not k:
            continue
        e = idx.setdefault(k, {'lines': set(), 'riders': 0})
        if p.get('line'):
            e['lines'].add(p['line'])
        r = p.get('riders')
        if isinstance(r, (int, float)) and r > e['riders']:
            e['riders'] = r
    hit = 0
    for s in stations:
        e = idx.get(s['name_key'])
        if e:
            hit += 1
            if not s['lines']:
                s['lines'] = sorted(e['lines'])
            if s['riders'] is None and e['riders']:
                s['riders'] = e['riders']
    return hit


def build_from_universe(raw):
    """universe.json（全集对账产物）→ 目标清单。
    剔除 ghost（废站/停运），主键 = phys_id，slug = st{phys_id:05d}；
    顺序 = in_planC 优先（C 组），组内按 phys_id 升序。"""
    stations_in = raw['stations']
    out = []
    skipped_ghost = 0
    for s in stations_in:
        if s.get('ghost'):
            skipped_ghost += 1
            continue
        coord = s.get('coord') or [None, None]
        out.append({
            'id': s['phys_id'],
            'slug': 'st%05d' % s['phys_id'],
            'name': s['name'],
            'name_key': (s.get('keys') or [s['name']])[0],
            'name_en': None,
            'lat': coord[1],
            'lon': coord[0],
            'pref': s.get('pref'),
            'scene': None,
            'lines': s.get('lines') or [],
            'riders': s.get('riders'),
            'same_as': [],
            'keys': s.get('keys') or [],
            'flags': {'has_stamp': bool(s.get('has_stamp')),
                      'in_planC': bool(s.get('in_planC')),
                      'ghost': False},
        })
    out.sort(key=lambda x: (not x['flags']['in_planC'], x['id']))
    return out, len(stations_in), skipped_ghost


def enrich_i18n(stations, i18n_path):
    """names_i18n.json（主站多语站名）→ name_en。按 name_key 或裸名匹配。"""
    ni = load_json(i18n_path).get('stations', {})
    hit = 0
    for s in stations:
        rec = ni.get(s['name_key']) or ni.get(s['name'])
        if rec and rec.get('en'):
            s['name_en'] = rec['en']
            hit += 1
    return hit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source', required=True,
                    choices=['stamp_scenes', 'station_map', 'universe'])
    ap.add_argument('--input', required=True,
                    help='stamp_scenes.json / station_map.json / universe.json')
    ap.add_argument('--geojson', default=None, help='可选：stations.geojson 富化 lines/riders')
    ap.add_argument('--i18n', default=None, help='可选：names_i18n.json 富化 name_en')
    ap.add_argument('--tag', required=True, help='清单标签，如 stamp1089 / all8909')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    raw = load_json(args.input)
    if args.source == 'stamp_scenes':
        recs = raw if isinstance(raw, list) else raw.get('stations', [])
        stations, total = build_from_stamp_scenes(recs)
        policy = 'primary_key=numeric_station_id(1001-10096); same-name stations share one photo via same_as'
        skipped_ghost = 0
    elif args.source == 'universe':
        stations, total, skipped_ghost = build_from_universe(raw)
        policy = ('primary_key=phys_id; slug=st{phys_id:05d}; ghosts excluded; '
                  'order=in_planC(C-core) first then phys_id asc')
    else:
        sm = raw.get('stations', raw) if isinstance(raw, dict) else raw
        stations, total = build_from_station_map(sm)
        policy = 'primary_key=temp_id_900001+(sorted by name); pending final reconciliation'
        skipped_ghost = 0

    geo_hit = None
    if args.geojson:
        geo_hit = enrich_geojson(stations, args.geojson)
    i18n_hit = None
    if args.i18n:
        i18n_hit = enrich_i18n(stations, args.i18n)

    doc = {
        'meta': {
            'tag': args.tag,
            'source': args.source,
            'input': args.input,
            'generated_at': now_iso(),
            'total_records': total,
            'canonical': len(stations),
            'ghosts_excluded': skipped_ghost,
            'policy': policy,
            'geojson_enriched': geo_hit,
            'i18n_enriched': i18n_hit,
        },
        'stations': stations,
    }
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print('wrote %s: canonical=%d total_records=%d ghosts_excluded=%d geo_hit=%s i18n_hit=%s' % (
        args.out, len(stations), total, skipped_ghost, geo_hit, i18n_hit))
    return 0


if __name__ == '__main__':
    sys.exit(main())

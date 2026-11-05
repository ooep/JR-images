#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ws15_refetch.py — wrong_station 重抓队列（15 条，stage=mismatch_removal）严格重抓。

口径（比常规 dead retry 更严）：
  1. 检索词带线路名/公司名消歧，并按站排除已知错图源关键词；
  2. 图片自带 GPS 且距站点坐标 <=2000m → 接受（GPS 证据）；
  3. 图片自带 GPS 且 >2000m → 拒（geo_strict_2km）；
  4. 无 GPS 的候选不直接入 HEAD：归一化后存 ws15_stage/ 暂存并随 artifact 回传，
     由本地会话做站牌 OCR + 目检后再决定是否提交；
  5. 异国/同名异线/非站景：标题关键词排除 + 硬排除正则；
  6. 许可/尺寸/体积/mime/sha/dHash 查重沿用 batch_fetch 口径。

产物：stations/<slug>/photo.jpg、licenses/<slug>.txt、state.json、index.json、
      data/dead_stations.json、PROGRESS.md、batch_stats_dead.json、
      reports/ws15_refetch_evidence.json、ws15_stage/（artifact 回传）。
提交与推送由 workflow 步骤完成（never force）。
"""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import batch_fetch as bf  # noqa: E402

WORKDIR = os.environ.get('WORKDIR', '.')
GPS_ACCEPT_M = 2000.0
NOGPS_STAGE_MAX = 3      # 每站最多回传的无 GPS 候选数
MAX_DOWNLOADS = 8        # 每站最多下载数

# 非站景标题黑名单（round3 教训：列车过桥照/灾害照曾两度通过 GPS 闸门）
NON_SCENE_RE = re.compile(
    r'bridge|EMU\b|\btrain\b|depot|garage|車庫|検車区|frigate|navy|\bship\b|'
    r'flood|damage|disaster|震災|水害|土砂|dosya|車両基地|橋梁', re.I)

# 每站的附加排除词（防再次抓到已确认错图的同源/同族图片）
EXCLUDE_PAT = {
    'st02193': re.compile(r'水間|みずま|Mizuma\s*Railway|Mizuma\s*Kannon', re.I),
    'st02021': re.compile(r'篠ノ井|Shinonoi', re.I),
    'st01798': re.compile(r'NDL\d|国立国会図書館|\b583\b|EF6[0-9]|EF81|Ltd\s*Exp', re.I),
    'st07773': re.compile(r'Xiangfeng|象峰|福州|Fuzhou|三江口', re.I),
    'st00609': re.compile(r'布吉|Buji|深圳|Shenzhen', re.I),
}

# 公司/线路消歧前缀（用于追加检索词）
COMPANY_HINTS = {
    'st01798': ['近鉄'], 'st01802': ['近鉄'],
    'st02021': ['近江鉄道'], 'st02036': ['近江鉄道'],
    'st02044': ['上田電鉄', '別所線'],
    'st02193': ['西鉄'], 'st02201': ['西鉄'], 'st02227': ['西鉄'],
    'st02229': ['西鉄'], 'st02231': ['西鉄'], 'st02232': ['西鉄'],
    'st02236': ['西鉄'], 'st02239': ['西鉄'], 'st02242': ['西鉄'],
    'st02295': ['名鉄', 'JR東海'],
}


def disambig_queries(st):
    name = (st.get('name') or '').strip()
    key = name[:-1] if name.endswith('駅') else name
    en = (st.get('name_en') or '').strip()
    lines = st.get('lines') or []
    qs = []
    if en:
        qs += ['%s Station' % en]
    qs += ['%s駅' % key]
    for hint in COMPANY_HINTS.get(st['slug'], []):
        qs.append('%s%s駅' % (hint, key))
        if en:
            qs.append('%s %s Station' % (hint, en))
    for ln in lines[:2]:
        qs.append('%s駅 %s' % (key, ln))
        if en:
            qs.append('%s Station %s' % (en, ln))
    seen, out = set(), []
    for q in qs:
        if q and q not in seen:
            seen.add(q)
            out.append(q)
    return out


def gather(st):
    """候选收集：分类直取 + 消歧检索，返回 {title: info} 与 fromcat 映射。"""
    name = (st.get('name') or '').strip()
    key = name[:-1] if name.endswith('駅') else name
    en = (st.get('name_en') or '').strip()
    infos, fromcat = {}, {}

    def add(mapping, cat):
        for t, ii in (mapping or {}).items():
            if ii and t not in infos:
                infos[t] = ii
                if cat:
                    fromcat[t] = cat

    cat_guesses = ['Category:%s駅' % key]
    if en:
        cat_guesses.append('Category:%s Station' % en)
    cat_guesses += ['Category:%s Station' % key, 'Category:%s' % key]
    for cat in cat_guesses:
        try:
            add(bf.category_files_info(cat), cat)
        except Exception as e:  # noqa: BLE001
            print('   cat %s ERR %s' % (cat, str(e)[:80]), flush=True)
    for q in disambig_queries(st):
        try:
            add(bf.search_files_info(q, limit=30), None)
            print('   search %r done' % q, flush=True)
        except Exception as e:  # noqa: BLE001
            print('   search %r ERR %s' % (q, str(e)[:80]), flush=True)
    return infos, fromcat


def main():
    os.chdir(WORKDIR)
    dead = json.load(open('data/dead_stations.json', encoding='utf-8'))
    stations_doc = json.load(open('data/stations_all.json', encoding='utf-8'))
    stations = stations_doc['stations']
    by_slug = {s['slug']: s for s in stations}
    state = json.load(open('state.json', encoding='utf-8'))
    index = json.load(open('index.json', encoding='utf-8'))

    queue = [slug for slug, r in dead['stations'].items()
             if r.get('stage') == 'mismatch_removal' and not r.get('final_dead')]
    queue.sort()
    # 未覆盖站续抓（B2 策略：客流降序 top-N；同名簇由标题闸门+10km 地理闸加严）
    uncov_top = int(os.environ.get('UNCOVERED_TOP', '0') or 0)
    if uncov_top:
        cov = {s for s, e in state['entries'].items()
               if e.get('status') in ('done', 'review')}
        qset = set(queue)
        uncov = [s for s in stations
                 if s['slug'] not in cov
                 and not dead['stations'].get(s['slug'], {}).get('final_dead')
                 and s['slug'] not in qset]
        uncov.sort(key=lambda s: -(s.get('riders') or 0))
        queue = queue + [s['slug'] for s in uncov[:uncov_top]]
    print('ws15 queue: %d %s' % (len(queue), queue), flush=True)

    # 已用登记表
    used = {'title': {}, 'sha': {}, 'dhash': {}}

    def register(slug, e):
        if not e:
            return
        if e.get('sha256'):
            used['sha'].setdefault(e['sha256'], slug)
        if e.get('source_title'):
            used['title'].setdefault(e['source_title'], slug)
        if e.get('dhash'):
            try:
                used['dhash'].setdefault(int(e['dhash'], 16), slug)
            except ValueError:
                pass

    for slug, e in (state.get('entries') or {}).items():
        if e.get('status') in ('done', 'review'):
            register(slug, e)
    for slug, e in (index.get('stations') or {}).items():
        register(slug.replace('legacy_', ''), e)

    import collections
    _nc = collections.Counter((s.get('name') or '').strip() for s in stations)
    same_name_names = {n for n, c in _nc.items() if c > 1 and n}

    # 全站名索引：标题站名闸门（round1 教训：GPS<2km 但标题指名邻站的误收）
    kanji_idx, _romaji_idx, romaji_re = bf.build_name_index(stations)

    evidence = {'queue': queue, 'accepted': [], 'nogps_staged': [],
                'still_missing': [], 'rejected_notable': []}
    stats = {'attempted': 0, 'done': 0, 'review': 0, 'missing': 0, 'failed': 0,
             'skipped_resume': 0, 'bytes': 0, 'reject_dist': {},
             'dead_retried': len(queue), 'dead_recovered': 0, 'dead_new': 0,
             'dead_cumulative': len(dead['stations'])}

    for slug in queue:
        st = by_slug.get(slug)
        if not st:
            continue
        stats['attempted'] += 1
        drec = dead['stations'].get(slug, {})
        removed_title = drec.get('removed_source_title')
        expat = EXCLUDE_PAT.get(slug)
        print('=== %s %s (%s) removed=%s' % (slug, st['name'], st.get('pref'),
                                              (removed_title or '')[:60]), flush=True)
        infos, fromcat = gather(st)
        cands = []
        for title, info in infos.items():
            if removed_title and title == removed_title:
                continue
            if bf.HARD_EXCLUDE_RE.search(title) or (expat and expat.search(title)):
                stats['reject_dist']['hard_excluded'] = \
                    stats['reject_dist'].get('hard_excluded', 0) + 1
                continue
            # 标题站名闸门：标题命中其他站名且不含本站名 → 拒
            # （round1 教训：邻站照片 GPS 距离 <2km 但标题明确指名他站）
            hits = bf.station_names_in_title(title, kanji_idx, romaji_re)
            same_as_set = set(st.get('same_as') or [])
            self_hit = any(slug in h[2] or (h[2] & same_as_set) for h in hits)
            other_hit = [h for h in hits
                         if slug not in h[2] and not (h[2] & same_as_set)]
            if other_hit and not self_hit:
                stats['reject_dist']['title_names_other_station'] = \
                    stats['reject_dist'].get('title_names_other_station', 0) + 1
                evidence['rejected_notable'].append(
                    {'slug': slug, 'title': title,
                     'named': other_hit[0][1], 'gate': 'title_names_other_station'})
                continue
            if NON_SCENE_RE.search(title):
                stats['reject_dist']['title_non_station_scene'] = \
                    stats['reject_dist'].get('title_non_station_scene', 0) + 1
                evidence['rejected_notable'].append(
                    {'slug': slug, 'title': title,
                     'named': None, 'gate': 'title_non_station_scene'})
                continue
            ok, lic, lic_url, author, reason = bf.license_verdict(info.get('extmetadata'))
            if not ok:
                stats['reject_dist'][reason] = stats['reject_dist'].get(reason, 0) + 1
                continue
            if info.get('mime') not in bf.OK_MIME:
                stats['reject_dist']['mime_unsupported'] = \
                    stats['reject_dist'].get('mime_unsupported', 0) + 1
                continue
            if (info.get('size') or 0) > bf.MAX_BYTES:
                stats['reject_dist']['oversize_gt_25mb'] = \
                    stats['reject_dist'].get('oversize_gt_25mb', 0) + 1
                continue
            w, h = info.get('width') or 0, info.get('height') or 0
            if max(w, h) < bf.DEAD_MIN_SIDE:
                stats['reject_dist']['resolution_low'] = \
                    stats['reject_dist'].get('resolution_low', 0) + 1
                continue
            owner = used['title'].get(title)
            if owner and owner != slug and owner not in set(st.get('same_as') or []):
                stats['reject_dist']['duplicate_title'] = \
                    stats['reject_dist'].get('duplicate_title', 0) + 1
                continue
            em = info.get('extmetadata') or {}
            ilat, ilon = bf.parse_gps(em, 'GPSLatitude'), bf.parse_gps(em, 'GPSLongitude')
            dist = None
            if ilat is not None and ilon is not None and st.get('lat') and st.get('lon'):
                dist = bf.haversine_m(ilat, ilon, st['lat'], st['lon'])
            score = bf.score_candidate(info, title, title in fromcat, fromcat.get(title))
            cands.append({'title': title, 'info': info, 'cat': fromcat.get(title),
                          'lic': lic, 'lic_url': lic_url, 'author': author,
                          'dist': dist, 'score': score})

        # 排序：GPS<=2km 优先（分数次之），再次是无 GPS（分数），最后是超距（不采用）
        def rank(c):
            if c['dist'] is not None and c['dist'] <= GPS_ACCEPT_M:
                g = 0
            elif c['dist'] is None:
                g = 1
            else:
                g = 2
            return (g, -c['score'])
        cands.sort(key=rank)
        for c in cands[:6]:
            print('   cand %s dist=%s score=%.2f %s' % (
                'GPS' if (c['dist'] is not None and c['dist'] <= GPS_ACCEPT_M) else
                ('NOGPS' if c['dist'] is None else 'FAR%.0f' % c['dist']),
                ('%.0fm' % c['dist']) if c['dist'] is not None else '-',
                c['score'], c['title'][:80]), flush=True)

        accepted = None
        staged = []
        downloads = 0
        for c in cands:
            if accepted or downloads >= MAX_DOWNLOADS:
                break
            if c['dist'] is not None and c['dist'] > GPS_ACCEPT_M:
                break  # 之后全是超距
            downloads += 1
            info = c['info']
            try:
                r = bf.http_get(info['url'], domain='upload.wikimedia.org',
                                stream=True, timeout=180)
                with r:
                    data = r.content
            except Exception as e:  # noqa: BLE001
                stats['reject_dist']['fetch_error'] = \
                    stats['reject_dist'].get('fetch_error', 0) + 1
                print('   fetch_error %s' % str(e)[:80], flush=True)
                continue
            if len(data) > bf.MAX_BYTES:
                stats['reject_dist']['oversize_gt_25mb'] = \
                    stats['reject_dist'].get('oversize_gt_25mb', 0) + 1
                continue
            try:
                ndata, (nw, nh), norm = bf.normalize_image(data, bf.MAX_LONG, bf.JPEG_Q)
            except Exception:  # noqa: BLE001
                stats['reject_dist']['undecodable'] = \
                    stats['reject_dist'].get('undecodable', 0) + 1
                continue
            sha = hashlib.sha256(ndata).hexdigest()
            owner = used['sha'].get(sha)
            if owner and owner != slug:
                stats['reject_dist']['duplicate_sha256'] = \
                    stats['reject_dist'].get('duplicate_sha256', 0) + 1
                continue
            try:
                dh = bf.dhash64(ndata)
            except Exception:  # noqa: BLE001
                dh = None
            near = None
            if dh is not None:
                for odh, oslug in used['dhash'].items():
                    if oslug != slug and bf.hamming(odh, dh) <= bf.NEAR_HAMMING:
                        near = oslug
                        break
            if near:
                stats['reject_dist']['near_duplicate'] = \
                    stats['reject_dist'].get('near_duplicate', 0) + 1
                continue
            em = info.get('extmetadata') or {}
            page_url = (em.get('DescriptionPage') or {}).get('value') or \
                'https://commons.wikimedia.org/wiki/File:' + \
                c['title'].replace('File:', '').replace(' ', '_')
            rec = {'title': c['title'], 'page_url': page_url, 'image_url': info.get('url'),
                   'license': c['lic'], 'license_url': c['lic_url'], 'author': c['author'],
                   'sha256': sha, 'dhash': ('%016x' % dh) if dh is not None else None,
                   'bytes': len(ndata), 'width': nw, 'height': nh, 'normalized': norm,
                   'dist_m': round(c['dist'], 1) if c['dist'] is not None else None,
                   'score': round(c['score'], 2), 'data': ndata}
            if c['dist'] is not None and c['dist'] <= GPS_ACCEPT_M and c['dist'] > 200:
                # 新规则（审计回执要求）：标题无站名且 dist>200m → 不直接接受，转 staged 本地复核
                _hits = bf.station_names_in_title(c['title'], kanji_idx, romaji_re)
                _same = set(st.get('same_as') or [])
                _self = any(slug in h[2] or (h[2] & _same) for h in _hits)
                if not _self:
                    staged.append(rec)
                    if len(staged) >= NOGPS_STAGE_MAX:
                        break
                    continue
            if c['dist'] is not None and c['dist'] <= GPS_ACCEPT_M:
                accepted = rec
            else:
                staged.append(rec)
                if len(staged) >= NOGPS_STAGE_MAX:
                    break

        if accepted:
            photo_dir = os.path.join('stations', slug)
            os.makedirs(photo_dir, exist_ok=True)
            rel_file = 'stations/%s/photo.jpg' % slug
            with open(os.path.join(photo_dir, 'photo.jpg'), 'wb') as f:
                f.write(accepted['data'])
            lic_txt = (
                'station: %s (%s)\n'
                'file: %s\n'
                'sha256: %s\n'
                'source_page: %s\n'
                'image_url: %s\n'
                'author: %s\n'
                'license: %s\n'
                'license_url: %s\n'
                'retrieved_at: %s\n'
                'normalized: %s\n'
                'attribution: %s / %s / %s / %s\n'
                'evidence: gps_dist=%.1fm (<=%.0fm)\n'
            ) % (st['name'], slug, rel_file, accepted['sha256'], accepted['page_url'],
                 accepted['image_url'], accepted['author'] or '(unknown)',
                 accepted['license'], accepted['license_url'] or '(none)', bf.now_iso(),
                 'normalized to long side %d (JPEG q%d) from %dx%d%s' % (
                     max(accepted['width'], accepted['height']), bf.JPEG_Q,
                     accepted['normalized'].get('original_width', 0),
                     accepted['normalized'].get('original_height', 0),
                     ' [below_spec retry]' if max(accepted['width'], accepted['height']) < bf.MIN_SIDE else ''),
                 accepted['author'] or '(unknown)', accepted['title'], accepted['license'],
                 accepted['license_url'] or '(none)', accepted['dist_m'], GPS_ACCEPT_M)
            os.makedirs('licenses', exist_ok=True)
            with open(os.path.join('licenses', slug + '.txt'), 'w', encoding='utf-8') as f:
                f.write(lic_txt)
            below_spec = max(accepted['width'], accepted['height']) < bf.MIN_SIDE
            entry = {
                'status': 'done',
                'file': rel_file,
                'sha256': accepted['sha256'],
                'dhash': accepted['dhash'],
                'bytes': accepted['bytes'],
                'width': accepted['width'],
                'height': accepted['height'],
                'normalized': accepted['normalized'],
                'below_spec': below_spec,
                'score': accepted['score'],
                'source_title': accepted['title'],
                'source_cat': None,
                'source_page': accepted['page_url'],
                'author': accepted['author'],
                'license': accepted['license'],
                'license_url': accepted['license_url'],
                'reasons': ['ws15_gps_verified(%.0fm)' % accepted['dist_m']] +
                           (['below_spec(long=%d)' % max(accepted['width'], accepted['height'])]
                            if below_spec else []),
                'ts': bf.now_iso(),
                'attempts': state['entries'].get(slug, {}).get('attempts', 0) + 1,
            }
            state['entries'][slug] = entry
            index.setdefault('stations', {})[slug] = {
                'station_id': st['id'], 'name': st['name'],
                'name_en': st.get('name_en'),
                'lat': st.get('lat'), 'lon': st.get('lon'),
                'pref': st.get('pref'), 'scene': st.get('scene'),
                'lines': st.get('lines') or [], 'same_as': st.get('same_as') or [],
                'status': 'done', 'file': rel_file,
                'width': accepted['width'], 'height': accepted['height'],
                'bytes': accepted['bytes'], 'sha256': accepted['sha256'],
                'dhash': accepted['dhash'],
                'source': accepted['page_url'], 'license': accepted['license'],
                'license_url': accepted['license_url'], 'author': accepted['author'],
                'page_url': accepted['page_url'],
                'retrieved_at': entry['ts'], 'metrics': None,
                'score': accepted['score'],
                'source_title': accepted['title'],
                'source_cat': None,
                'below_spec': below_spec,
                'review_reasons': entry['reasons'],
            }
            register(slug, entry)
            dead['stations'].pop(slug, None)
            stats['done'] += 1
            stats['bytes'] += accepted['bytes']
            stats['dead_recovered'] += 1
            evidence['accepted'].append(
                dict(slug=slug, **{k: v for k, v in accepted.items() if k != 'data'}))
            print('   ACCEPT(GPS %.0fm) %s' % (accepted['dist_m'], accepted['title'][:70]),
                  flush=True)
        elif staged:
            st_dir = os.path.join('ws15_stage', slug)
            os.makedirs(st_dir, exist_ok=True)
            for i, rec in enumerate(staged, 1):
                with open(os.path.join(st_dir, '%d_photo.jpg' % i), 'wb') as f:
                    f.write(rec['data'])
                meta = {k: v for k, v in rec.items() if k != 'data'}
                meta['station'] = {'slug': slug, 'name': st['name'], 'pref': st.get('pref'),
                                   'name_en': st.get('name_en'), 'lat': st.get('lat'),
                                   'lon': st.get('lon'), 'lines': st.get('lines')}
                with open(os.path.join(st_dir, '%d_meta.json' % i), 'w', encoding='utf-8') as f:
                    json.dump(meta, f, ensure_ascii=False, indent=1)
                evidence['nogps_staged'].append(
                    dict(slug=slug, **{k: v for k, v in meta.items() if k != 'station'}))
            evidence['still_missing'].append({
                'slug': slug, 'name': st['name'], 'pref': st.get('pref'),
                'state': 'staged_for_local_ocr_visual', 'n_staged': len(staged)})
            stats['missing'] += 1
            print('   STAGED %d candidates for local OCR/visual' % len(staged), flush=True)
        else:
            reasons = dict(stats['reject_dist'])
            entry = state['entries'].get(slug) or {}
            state['entries'][slug] = {
                'status': 'missing', 'file': None, 'sha256': None, 'bytes': None,
                'reasons': ['ws15_refetch_no_candidate'],
                'ts': bf.now_iso(),
                'removed_source_title': removed_title,
                'attempts': entry.get('attempts', 0) + 1,
            }
            prev = dead['stations'].get(slug, {})
            attempts = prev.get('attempts', 0) + 1
            dead['stations'][slug] = dict(prev, **{
                'stage': 'ws15_refetch',
                'reasons': {'no_verifiable_candidate': 1},
                'attempts': attempts,
                'final_dead': attempts >= bf.DEAD_MAX_ATTEMPTS,
                'last_attempt': bf.now_iso(),
                'note': 'ws15 round1: 无 GPS<=2km 或可回传候选',
            })
            evidence['still_missing'].append({
                'slug': slug, 'name': st['name'], 'pref': st.get('pref'),
                'state': 'no_candidate', 'reject_dist': reasons})
            stats['dead_new'] += 1
            print('   NO_CANDIDATE', flush=True)
        sys.stdout.flush()

    # 汇总落盘
    state['updated_at'] = bf.now_iso()
    json.dump(state, open('state.json', 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(index, open('index.json', 'w', encoding='utf-8'), ensure_ascii=False)
    dead['count'] = len(dead['stations'])
    dead['updated_at'] = bf.now_iso()
    json.dump(dead, open('data/dead_stations.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    stats['generated_at'] = bf.now_iso()
    stats['dead_cumulative'] = len(dead['stations'])
    json.dump(stats, open('batch_stats_dead.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    os.makedirs('reports', exist_ok=True)
    json.dump(evidence, open('reports/ws15_refetch_evidence.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    with open('PROGRESS.md', 'a', encoding='utf-8') as f:
        f.write('\n\n## ws15 refetch round 1 — %s\n' % bf.now_iso())
        f.write('- queue: wrong_station 重抓队列 %d 站（stage=mismatch_removal）\n' % len(queue))
        f.write('- accepted(GPS<=2km)=%d staged_no_gps=%d still_missing=%d\n' % (
            len(evidence['accepted']),
            sum(1 for x in evidence['still_missing']
                if x['state'] == 'staged_for_local_ocr_visual'),
            sum(1 for x in evidence['still_missing'] if x['state'] == 'no_candidate')))
        f.write('- reject_dist=%s\n' % json.dumps(stats['reject_dist'], ensure_ascii=False))
        f.write('- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 '
                'reports/ws15_refetch_evidence.json\n')
    print('SUMMARY accepted=%d staged=%d missing=%d' % (
        len(evidence['accepted']),
        sum(1 for x in evidence['still_missing'] if x['state'] == 'staged_for_local_ocr_visual'),
        sum(1 for x in evidence['still_missing'] if x['state'] == 'no_candidate')), flush=True)


if __name__ == '__main__':
    main()

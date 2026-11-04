#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rules_audit.py — 对已推图片做县名/站名判据回溯体检（只读元数据）。
县名判据：只认标题证据硬拒（pref_mismatch）；Commons category 证据降为旁证
（pref_mismatch_review，只计数不拒）。罗马字词边界匹配 + 线路名/方位词/
指名本站豁免。输出各判据总数与前 50 明细，供人工核对误杀率（>2% 则调阈值）。
"""
import collections
import json
import os
import re
from urllib.parse import unquote


def title_from_source(url):
    """旧批条目没存 source_title 时，从 Commons 文件页 URL 还原。"""
    if not url or '/wiki/' not in url:
        return ''
    t = unquote(url.split('/wiki/', 1)[1]).replace('_', ' ')
    return t if t.startswith('File:') else 'File:' + t

PREFS = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
         '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
         '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県',
         '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県',
         '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県',
         '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県',
         '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']
PREF_ROMAJI = {'北海道': 'Hokkaido', '青森県': 'Aomori', '岩手県': 'Iwate',
               '宮城県': 'Miyagi', '秋田県': 'Akita', '山形県': 'Yamagata',
               '福島県': 'Fukushima', '茨城県': 'Ibaraki', '栃木県': 'Tochigi',
               '群馬県': 'Gunma', '埼玉県': 'Saitama', '千葉県': 'Chiba',
               '東京都': 'Tokyo', '神奈川県': 'Kanagawa', '新潟県': 'Niigata',
               '富山県': 'Toyama', '石川県': 'Ishikawa', '福井県': 'Fukui',
               '山梨県': 'Yamanashi', '長野県': 'Nagano', '岐阜県': 'Gifu',
               '静岡県': 'Shizuoka', '愛知県': 'Aichi', '三重県': 'Mie',
               '滋賀県': 'Shiga', '京都府': 'Kyoto', '大阪府': 'Osaka',
               '兵庫県': 'Hyogo', '奈良県': 'Nara', '和歌山県': 'Wakayama',
               '鳥取県': 'Tottori', '島根県': 'Shimane', '岡山県': 'Okayama',
               '広島県': 'Hiroshima', '山口県': 'Yamaguchi', '徳島県': 'Tokushima',
               '香川県': 'Kagawa', '愛媛県': 'Ehime', '高知県': 'Kochi',
               '福岡県': 'Fukuoka', '佐賀県': 'Saga', '長崎県': 'Nagasaki',
               '熊本県': 'Kumamoto', '大分県': 'Oita', '宮崎県': 'Miyazaki',
               '鹿児島県': 'Kagoshima', '沖縄県': 'Okinawa'}
LINE_NEXT_WORDS = {'main', 'line', 'lines'}
STATION_NEXT_WORDS = {'station', 'sta', 'stn', 'eki'}
GENERIC_KANJI = {'駅前', '市役所', 'ドーム前'}
GENERIC_ROMAJI = {'ekimae', 'city hall', 'dome-mae', 'dome mae'}
LOC_WORDS = ('pref', 'prefecture', 'city', 'town', 'village')


def _norm_romaji(s):
    for a, b in (('ā', 'a'), ('ī', 'i'), ('ū', 'u'), ('ē', 'e'), ('ō', 'o'),
                 ('Ā', 'a'), ('Ī', 'i'), ('Ū', 'u'), ('Ē', 'e'), ('Ō', 'o')):
        s = s.replace(a, b)
    return s.lower().replace('ou', 'o')


def _norm_loose(s):
    s = _norm_romaji(s)
    s = re.sub(r'[()\[\]/&.,:;\'"!\-]', '', s)
    s = re.sub(r'\s+', '', s)
    return s.replace('nm', 'mm')


def _romaji_boundary(text_low, rom):
    m = re.search(r'(?<![a-z0-9])' + re.escape(rom) + r'(?![a-z0-9])', text_low)
    return (m.start(), m.end()) if m else None


def _next_word(text_low, end):
    m = re.match(r'[^a-z]*([a-z]+)', text_low[end:])
    return m.group(1) if m else ''


def pref_forms(pref):
    forms = set()
    if not pref:
        return forms
    forms.add(pref)
    for suf in ('県', '府', '都'):
        if pref.endswith(suf):
            forms.add(pref[:-1])
    return forms


def pref_mismatch_hit(text, e):
    """县名判据：出现其他都道府县名且不含本站县名 → True。
    汉字子串；罗马字词边界；豁免：线路名（汉字在 lines / 罗马字后接 main|line）、
    方位词（大阪方面）、站名自带县名。"""
    own = (e.get('pref') or '').strip()
    name = e.get('name') or ''
    lines = ' '.join(e.get('lines') or [])
    if not own or not text:
        return False, None
    low = text.lower()
    for f in pref_forms(own):
        if f and f in text:
            return False, None
    rom_own = PREF_ROMAJI.get(own)
    if rom_own and _romaji_boundary(low, rom_own.lower()):
        return False, None
    for p in PREFS:
        if p == own:
            continue
        kanji_forms = {p}
        for suf in ('県', '府', '都'):
            if p.endswith(suf):
                kanji_forms.add(p[:-1])
        if any(f and f in name for f in kanji_forms):
            continue
        for f in kanji_forms:
            if f and f in text:
                if f in name or (lines and f in lines):
                    continue
                i = text.find(f)
                if text[i + len(f):i + len(f) + 2] == '方面':
                    continue
                return True, p
        rom = PREF_ROMAJI.get(p)
        if rom:
            span = _romaji_boundary(low, rom.lower())
            if span:
                if rom.lower() in _norm_romaji(name):
                    continue
                if _next_word(low, span[1]) in LINE_NEXT_WORDS:
                    continue
                return True, p
    return False, None


def name_tokens(e):
    toks = set()
    name = (e.get('name') or '').strip()
    if name:
        toks.add(name)
        toks.add(name + '駅')
        if name.endswith('駅'):
            toks.add(name[:-1])
    t = (e.get('name_en') or '').strip()
    if t:
        t = t.split('(')[0].strip()
        variants = {t}
        if t.upper().startswith('JR '):
            variants.add(t[3:])
        for v in list(variants):
            toks.update({v, v + ' Station', v + ' station', v + '-station'})
    return toks


def name_mismatch_hit(text, e):
    toks = name_tokens(e)
    if not toks or not text:
        return False
    low = _norm_loose(text)
    return not any(_norm_loose(t) in low for t in toks if t)


def build_name_index(stations):
    kanji = collections.defaultdict(set)
    romaji = collections.defaultdict(set)
    for s in stations:
        slug = s.get('slug')
        nm = (s.get('name') or '').strip()
        if nm:
            kanji[nm].add(slug)
        for k in (s.get('keys') or []):
            k = (k or '').strip()
            if k:
                kanji[k].add(slug)
        en = (s.get('name_en') or '').strip()
        if en:
            romaji[_norm_romaji(en)].add(slug)
            if en.upper().startswith('JR '):
                romaji[_norm_romaji(en[3:])].add(slug)
    romaji_re = []
    for rom, slugs in romaji.items():
        if len(rom) < 3 or rom in GENERIC_ROMAJI:
            continue
        pat = re.compile(r'(?<![a-z0-9])' + re.escape(rom.replace('-', ' '))
                         + r'(?![a-z0-9])')
        romaji_re.append((len(rom), pat, rom, slugs))
    romaji_re.sort(key=lambda x: -x[0])
    return kanji, romaji, romaji_re


def station_names_in_title(title, kanji, romaji_re):
    if not title:
        return []
    low = _norm_romaji(title).replace('-', ' ')
    hits = []
    for nm, slugs in kanji.items():
        if len(nm) >= 2 and nm not in GENERIC_KANJI and nm in title:
            hits.append((len(nm), nm, slugs, title.find(nm)))
    for ln, pat, rom, slugs in romaji_re:
        m = pat.search(low)
        if m and _next_word(low, m.end()) in STATION_NEXT_WORDS:
            hits.append((m.end() - m.start(), rom, slugs, m.start()))
    hits.sort(key=lambda h: (-h[0], h[3]))
    kept, taken = [], []
    for ln, nm, slugs, start in hits:
        if any(start < e and start + ln > s for s, e in taken):
            continue
        taken.append((start, start + ln))
        kept.append((ln, nm, slugs))
    return kept


def named_own_station(e, hits):
    slug = e.get('slug') or ''
    for _ln, _nm, slugs in hits:
        if slug in slugs and len(slugs) == 1:
            return True
    return False


def has_location_marker(title):
    low = title.lower()
    for w in LOC_WORDS:
        if re.search(r'(?<![a-z])' + w + r'(?![a-z])', low):
            return True
    for p in PREFS:
        forms = {p}
        for suf in ('県', '府', '都'):
            if p.endswith(suf):
                forms.add(p[:-1])
        if any(f in title for f in forms):
            return True
    return False


def main():
    idx = json.load(open('index.json', encoding='utf-8'))
    doc = json.load(open('data/stations_all.json', encoding='utf-8'))
    stations = doc['stations'] if isinstance(doc, dict) else doc
    kanji, _romaji, romaji_re = build_name_index(stations)
    by_slug = {s['slug']: s for s in stations}

    pref_hits, pref_review, name_hits, checked = [], [], [], 0
    for slug, e in sorted(idx.get('stations', {}).items()):
        if e.get('status') not in ('done', 'review'):
            continue
        if not (e.get('file') or '').startswith('stations/'):
            continue
        checked += 1
        full = dict(by_slug.get(slug, {}))
        full.update({k: v for k, v in e.items() if v is not None})
        full['slug'] = slug
        title = e.get('source_title') or title_from_source(e.get('source'))
        cat = e.get('source_cat') or ''
        hit_t, other = pref_mismatch_hit(title, full)
        if hit_t and not has_location_marker(title) and \
                named_own_station(full, station_names_in_title(title, kanji, romaji_re)):
            hit_t = False
        if hit_t:
            pref_hits.append({'slug': slug, 'name': full.get('name'),
                              'pref': full.get('pref'), 'other_pref': other,
                              'title': title, 'source': e.get('source')})
            continue  # 与抓取管道口径一致：硬拒后不再计后续判据
        if cat and pref_mismatch_hit(cat, full)[0]:
            pref_review.append({'slug': slug, 'name': full.get('name'),
                                'pref': full.get('pref'),
                                'other_pref': pref_mismatch_hit(cat, full)[1],
                                'title': title, 'cat': cat[:120],
                                'source': e.get('source')})
        if name_mismatch_hit(title + ' ' + cat, full):
            name_hits.append({'slug': slug, 'name': full.get('name'),
                              'name_en': full.get('name_en'),
                              'title': title, 'cat': e.get('source_cat'),
                              'source': e.get('source')})
    report = {
        'checked': checked,
        'pref_mismatch_total': len(pref_hits),
        'pref_review_total': len(pref_review),
        'name_mismatch_total': len(name_hits),
        'pref_mismatch_detail': pref_hits[:50],
        'pref_review_detail': pref_review[:50],
        'name_mismatch_detail': name_hits[:50],
    }
    with open('rules_audit_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    line = ('rules_audit: checked=%d pref_mismatch=%d pref_review=%d '
            'name_mismatch=%d' % (checked, len(pref_hits), len(pref_review),
                                  len(name_hits)))
    print(line)
    smry = os.environ.get('GITHUB_STEP_SUMMARY')
    if smry:
        with open(smry, 'a', encoding='utf-8') as f:
            f.write('- %s\n' % line)


if __name__ == '__main__':
    main()

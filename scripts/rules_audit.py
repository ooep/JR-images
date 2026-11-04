#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rules_audit.py — 对已推图片做县名/站名判据回溯体检（只读 index 元数据）：
输出各判据判掉的总数与前 50 明细，供人工核对误杀率（>2% 则调阈值）。
"""
import collections
import json
import os
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


def pref_forms(pref):
    forms = set()
    if not pref:
        return forms
    forms.add(pref)
    for suf in ('県', '府', '都'):
        if pref.endswith(suf):
            forms.add(pref[:-1])
    rom = PREF_ROMAJI.get(pref)
    if rom:
        forms.add(rom.lower())
    return forms


def pref_mismatch_hit(text, e):
    own = (e.get('pref') or '').strip()
    name = e.get('name') or ''
    if not own or not text:
        return False, None
    own_forms = pref_forms(own)
    if any(f.lower() in text.lower() for f in own_forms if f):
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
        if any(f.lower() in text.lower() for f in pref_forms(p) if f):
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
        toks.update({t, t + ' Station', t + ' station', t + '-station'})
    return toks


def name_mismatch_hit(text, e):
    toks = name_tokens(e)
    if not toks or not text:
        return False
    low = text.lower()
    return not any(t.lower() in low for t in toks if t)


def main():
    idx = json.load(open('index.json', encoding='utf-8'))
    pref_hits, name_hits, checked = [], [], 0
    for slug, e in sorted(idx.get('stations', {}).items()):
        if e.get('status') not in ('done', 'review'):
            continue
        if not (e.get('file') or '').startswith('stations/'):
            continue
        checked += 1
        title = e.get('source_title') or title_from_source(e.get('source'))
        text = title + ' ' + (e.get('source_cat') or '')
        hit_p, other = pref_mismatch_hit(text, e)
        if hit_p:
            pref_hits.append({'slug': slug, 'name': e.get('name'),
                              'pref': e.get('pref'), 'other_pref': other,
                              'title': title,
                              'source': e.get('source')})
        if name_mismatch_hit(text, e):
            name_hits.append({'slug': slug, 'name': e.get('name'),
                              'name_en': e.get('name_en'),
                              'title': title,
                              'cat': e.get('source_cat'),
                              'source': e.get('source')})
    report = {
        'checked': checked,
        'pref_mismatch_total': len(pref_hits),
        'name_mismatch_total': len(name_hits),
        'pref_mismatch_detail': pref_hits[:50],
        'name_mismatch_detail': name_hits[:50],
    }
    with open('rules_audit_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    line = ('rules_audit: checked=%d pref_mismatch=%d name_mismatch=%d'
            % (checked, len(pref_hits), len(name_hits)))
    print(line)
    smry = os.environ.get('GITHUB_STEP_SUMMARY')
    if smry:
        with open(smry, 'a', encoding='utf-8') as f:
            f.write('- %s\n' % line)


if __name__ == '__main__':
    main()

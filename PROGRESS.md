# JR-images 进度

- 口径与规则见 `ASSETS.md`；目标站清单为 `data/stations_<tag>.json`（可替换输入）。
- 旧 500 张 1200px 试点图保留在 `img/` 历史路径，`index.json` 中以 `legacy_*` 键标记 `legacy: true`，
  重建按站覆盖后将在 README 注明替换情况。


## batch 0 — 2026-11-03T10:43:22Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=500 done=485 review=11 missing=4 failed=0 skipped_resume=0
- bytes_this_batch=283876635 avg=572331
- reject_dist={"resolution_low": 1872, "no_author_metadata": 104, "oversize_gt_25mb": 117, "license_unclear": 134, "mime_unsupported": 71, "low_color(map/text?)": 69, "license_forbidden": 2, "blurry(lap=38<45)": 1}
- cumulative_indexed=996/8909
- elapsed=3098s


## batch 1 — 2026-11-03T11:35:54Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=500 done=482 review=10 missing=8 failed=0 skipped_resume=0
- bytes_this_batch=293905211 avg=597368
- reject_dist={"resolution_low": 1723, "license_unclear": 69, "no_author_metadata": 80, "low_color(map/text?)": 93, "oversize_gt_25mb": 159, "mime_unsupported": 94, "license_forbidden": 24, "blurry(lap=43<45)": 1}
- cumulative_indexed=1488/8909
- elapsed=3057s


## batch 2 — 2026-11-03T12:32:53Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=500 done=450 review=42 missing=12 failed=0 skipped_resume=0
- bytes_this_batch=211184790 avg=429237
- dead: new=12 cumulative=12 retried=4 recovered=3
- reject_dist={"resolution_low": 1424, "mime_unsupported": 204, "oversize_gt_25mb": 379, "low_color(map/text?)": 64, "no_author_metadata": 58, "license_unclear": 30, "license_forbidden": 5}
- cumulative_indexed=1980/8909
- elapsed=3296s


## batch 3 — 2026-11-03T14:39:55Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=500 done=396 review=95 missing=19 failed=0 skipped_resume=0
- bytes_this_batch=206330586 avg=420225
- dead: new=19 cumulative=107 retried=10 recovered=10
- reject_dist={"oversize_gt_25mb": 232, "resolution_low": 1652, "hard_excluded": 674, "low_color(map/text?)": 185, "mime_unsupported": 115, "no_author_metadata": 72, "license_unclear": 67, "license_forbidden": 4, "blurry(lap=42<45)": 1, "blurry(lap=29<45)": 1}
- cumulative_indexed=2461/8909
- elapsed=4204s


## batch 4 — 2026-11-03T15:52:15Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=500 done=390 review=105 missing=15 failed=0 skipped_resume=0
- bytes_this_batch=209538600 avg=423310
- dead: new=15 cumulative=112 retried=10 recovered=5
- reject_dist={"resolution_low": 1888, "mime_unsupported": 85, "oversize_gt_25mb": 129, "low_color(map/text?)": 206, "no_author_metadata": 177, "license_unclear": 61, "hard_excluded": 693, "white_screenshot": 1, "blurry(lap=34<45)": 1}
- cumulative_indexed=2956/8909
- elapsed=4191s


## batch 5 — 2026-11-04T01:09:45Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=500 done=414 review=92 missing=19 failed=0 skipped_resume=0
- bytes_this_batch=214726454 avg=424360
- dead: new=19 cumulative=133 retried=25 recovered=25
- reject_dist={"geo_mismatch": 904, "hard_excluded": 602, "resolution_low": 1961, "pref_mismatch": 457, "name_mismatch_review": 1934, "mime_unsupported": 109, "license_unclear": 45, "low_color(map/text?)": 168, "oversize_gt_25mb": 158, "no_author_metadata": 95, "duplicate_sha256": 7}
- cumulative_indexed=3437/8909
- elapsed=2521s


## dead retry — 2026-11-04T04:17:07Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=18 review=6 missing=1 failed=0 skipped_resume=0
- bytes_this_batch=9207143 avg=383630
- dead: new=1 cumulative=125 retried=25 recovered=24
- reject_dist={"name_mismatch_review": 75, "hard_excluded": 30, "license_unclear": 2, "low_color(map/text?)": 10, "wrong_station": 22, "geo_mismatch": 111, "pref_mismatch": 65, "resolution_low": 77, "white_screenshot": 1, "oversize_gt_25mb": 10, "mime_unsupported": 4, "blurry(lap=40<45)": 1}
- cumulative_indexed=3437/8909
- elapsed=226s


## dead retry — 2026-11-04T04:29:28Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=10 review=14 missing=1 failed=0 skipped_resume=0
- bytes_this_batch=10428256 avg=434510
- dead: new=1 cumulative=208 retried=25 recovered=24
- reject_dist={"name_mismatch_review": 147, "resolution_low": 45, "pref_mismatch": 48, "mime_unsupported": 14, "geo_mismatch": 147, "hard_excluded": 15, "low_color(map/text?)": 7, "oversize_gt_25mb": 34, "wrong_station": 74, "no_author_metadata": 6, "white_screenshot": 1, "license_unclear": 2}
- cumulative_indexed=3437/8909
- elapsed=268s


## dead retry — 2026-11-04T04:41:29Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=11 review=3 missing=11 failed=0 skipped_resume=0
- bytes_this_batch=6325608 avg=451829
- dead: new=11 cumulative=194 retried=25 recovered=14
- reject_dist={"resolution_low": 4, "no_station_evidence": 132, "pref_mismatch": 17, "hard_excluded": 24, "low_color(map/text?)": 4, "name_mismatch_review": 78, "wrong_station": 51, "oversize_gt_25mb": 1, "geo_mismatch": 37}
- cumulative_indexed=3437/8909
- elapsed=209s


## dead retry — 2026-11-04T04:47:47Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=7 review=3 missing=15 failed=0 skipped_resume=0
- bytes_this_batch=4072592 avg=407259
- dead: new=15 cumulative=184 retried=25 recovered=10
- reject_dist={"no_station_evidence": 89, "wrong_station": 39, "hard_excluded": 12, "pref_mismatch": 25, "geo_mismatch": 43, "name_mismatch_review": 34, "resolution_low": 3, "low_color(map/text?)": 2}
- cumulative_indexed=3437/8909
- elapsed=167s


## dead retry — 2026-11-04T04:55:04Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=7 review=8 missing=10 failed=0 skipped_resume=0
- bytes_this_batch=6305701 avg=420380
- dead: new=10 cumulative=169 retried=25 recovered=15
- reject_dist={"no_station_evidence": 180, "pref_mismatch": 33, "geo_mismatch": 31, "name_mismatch_review": 104, "hard_excluded": 24, "wrong_station": 48, "resolution_low": 21, "low_color(map/text?)": 7}
- cumulative_indexed=3437/8909
- elapsed=176s


## dead retry — 2026-11-04T05:02:22Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=6 review=2 missing=17 failed=0 skipped_resume=0
- bytes_this_batch=3111047 avg=388880
- dead: new=17 cumulative=161 retried=25 recovered=8
- reject_dist={"hard_excluded": 6, "resolution_low": 5, "name_mismatch_review": 34, "no_station_evidence": 66, "geo_mismatch": 15, "low_color(map/text?)": 8, "wrong_station": 25, "pref_mismatch": 3}
- cumulative_indexed=3437/8909
- elapsed=157s


## dead retry — 2026-11-04T05:09:24Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=7 review=5 missing=13 failed=0 skipped_resume=0
- bytes_this_batch=4905120 avg=408760
- dead: new=13 cumulative=170 retried=25 recovered=12
- reject_dist={"geo_mismatch": 72, "no_station_evidence": 118, "name_mismatch_review": 71, "wrong_station": 61, "pref_mismatch": 24, "hard_excluded": 19, "resolution_low": 13, "low_color(map/text?)": 5}
- cumulative_indexed=3437/8909
- elapsed=154s


## dead retry — 2026-11-04T16:47:02Z
- list: `data/stations_all.json` (canonical 8909)
- attempted=0 done=3 review=2 missing=20 failed=0 skipped_resume=0
- bytes_this_batch=2457288 avg=491457
- dead: new=20 cumulative=168 retried=25 recovered=5
- reject_dist={"resolution_low": 2, "no_station_evidence": 62, "name_mismatch_review": 36, "geo_mismatch": 42, "wrong_station": 1, "pref_mismatch": 2, "hard_excluded": 3, "low_color(map/text?)": 3}
- cumulative_indexed=3437/8909
- elapsed=144s



## ws15 refetch round 1 — 2026-11-05T16:41:29Z
- queue: wrong_station 重抓队列 20 站（stage=mismatch_removal）
- accepted(GPS<=2km)=14 staged_no_gps=5 still_missing=1
- reject_dist={"duplicate_title": 19, "hard_excluded": 58, "resolution_low": 58, "mime_unsupported": 139, "no_author_metadata": 3, "license_unclear": 1}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 revert — 2026-11-05T17:04:52Z
- round1 中 7 站 GPS<=2km 通过但标题明确指名邻站（大善寺/北野/開 x2/西鉄柳河/三国ヶ丘/薬院），判定图与站名不符，撤出 HEAD 并重置重抓队列。
- 撤站: st02193 st02201 st02227 st02229 st02232 st02236 st02242
- round2 补丁：标题站名闸门（标题命中他站名即拒）+ 象峰/布吉等异国关键词排除。


## ws15 local accept — 2026-11-05T17:07:13Z
- st00609 市布(長崎県) ← File:JRKyushu Ichinuno Station 1.jpg：站牌目检「市布駅/ICHIUNO」通过（round1 artifact 回传候选），below_spec(long=1280) 入 review。
- 同批暂存其余 12 候选目检/OCR 拒收：深圳布吉x2、福州象峰x3（异国）、明星号列车x3（非站景）、彦根駅闸口（他站）、福井(福井県)x3（同名异县）。


## ws15 refetch round 1 — 2026-11-05T17:15:00Z
- queue: wrong_station 重抓队列 11 站（stage=mismatch_removal）
- accepted(GPS<=2km)=2 staged_no_gps=7 still_missing=2
- reject_dist={"duplicate_title": 1, "title_names_other_station": 38, "mime_unsupported": 22, "hard_excluded": 47, "resolution_low": 24, "no_author_metadata": 2}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 revert-n — 2026-11-05T17:21:35Z
- 撤站 st02229；原因：非站景：列车过矢部川桥照片(Nishitetsu EMU 8061F at Yabegawa Bridge)


## ws15 local accept batch2 — 2026-11-05T17:23:32Z
- st02227 西鉄渡瀬 ← File:Nishitetsu Wataze Station 2021.JPG (done, 西鉄渡瀬駅 / Nishitetsu Wataze Sta. / 自動販売機コーナー)
- st02236 津古 ← File:Nishitetsu Tsuko Station01.jpg (review, 津古駅 / Tsuko Sta.（双牌）)
- 证据：round2 artifact 回传候选，Vision OCR 站牌命中 + 目检通过。
- st02193 三潴候选「Mizuma Station.JPG」目检为水间铁道水间观音駅（塔式站房+水間観音駅牌），拒收；st02232 徳益候选无站名牌证据，拒收留 round3。

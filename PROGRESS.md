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


## ws16 foreign purge — 2026-11-05T17:34:12Z
- 撤异国错配图 10 站（审计 P0，来源实证：上海/天津/北京/首尔/大邱地铁与 Korail）：st02517 st02777 st04016 st04955 st05323 st06754 st07109 st07703 st07983 st08679
- 重置 stage=mismatch_removal 入重抓队列，round3 严格闸门重抓。
- 旧编号 img/ 两张异国源图（st00214 澳门、st05802 韩国）属海报线辖，登记不移除，交审计线/海报线裁决。


## ws15 refetch round 1 — 2026-11-05T17:43:29Z
- queue: wrong_station 重抓队列 16 站（stage=mismatch_removal）
- accepted(GPS<=2km)=4 staged_no_gps=12 still_missing=0
- reject_dist={"duplicate_title": 6, "title_names_other_station": 58, "mime_unsupported": 74, "hard_excluded": 63, "resolution_low": 56, "license_forbidden": 5, "license_unclear": 2}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 revert-n — 2026-11-05T17:53:21Z
- 撤站 st02229 st05323；原因：非站景：st02229列车过矢部川桥照再犯；st05323为灾害损毁照(Hiroshima-dosya)


## ws15 local accept batch3 — 2026-11-05T17:55:49Z
- st07109 水落(福井県) ← File:Mizuochi Station 2020.jpg：站牌 OCR「水落」+目检竖牌水落駅；done。
- round3 其余暂存拒收：洗马/川路/寿(富士急)候选无站名牌证据；首尔Yaksu x2+INS军舰(薬水)、慈寿寺 x2(寿)、Suraksan(水落)、下沙(下立)、象峰/鹤峰(峰)、三重朝陽x3(朝陽,县不符) 异国/他站/县不符。


## ws15 refetch round 1 — 2026-11-05T18:04:03Z
- queue: wrong_station 重抓队列 13 站（stage=mismatch_removal）
- accepted(GPS<=2km)=0 staged_no_gps=13 still_missing=0
- reject_dist={"title_non_station_scene": 17, "duplicate_title": 5, "title_names_other_station": 55, "mime_unsupported": 65, "hard_excluded": 55, "resolution_low": 39, "license_forbidden": 5, "license_unclear": 2}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 local accept batch4 — 2026-11-05T18:15:10Z
- st02229 江の浦 ← File:Nishitetsu Enoura Station01.jpg (review)
- st05323 梅林 ← File:Bairin Station building 2.jpg (done)


## ws15 finalize missing — 2026-11-05T18:18:01Z
- st00577 福井(岡山)：Commons 仅福井県福井駅(同名异县)与货物南福井场景，无本站合格候选
- st01798 明星(三重)：仅检车区/车库/列车照与中央大学明治大学(他站)，无本站站景
- st02193 三潴(福岡)：仅水间铁道水间观音駅(他线)与消防署(非站景)，无本站站景
- st02231 塩塚(福岡)：rounds1-2 检索零候选
- st02232 徳益(福岡)：仅无站名牌站台照，不满足站牌 OCR/目检口径
- st02517 川路(長野)：仅上海铜川路(异国)与无站名牌 Kawaji-eki 照
- st02777 洗馬(長野)：仅无站名牌 Seba 站房照与木曾路册页/旧画
- st04955 药水(奈良)：仅首尔药水站(异国)x3 与军舰照(非站景)
- st06754 寿(山梨)：仅北京慈寿寺(异国)x2 与无站名牌富士急寿照
- st07703 下立(富山)：仅上海下沙(异国)与折立站/报纸扫描件(他站/非站景)
- st07773 峰(栃木)：仅福州象峰(异国)x3 与横滨鹤峰巴士站(他站)
- st08679 朝阳(長野)：仅三重县朝日站(县不符)x3
- wrong_station 15 队列与 ws16 异国 10 队列至此全部处置完毕（补图/标缺），未覆盖站转 B2 客流策略续抓。


## ws15 refetch round 1 — 2026-11-05T18:29:47Z
- queue: wrong_station 重抓队列 30 站（stage=mismatch_removal）
- accepted(GPS<=2km)=20 staged_no_gps=10 still_missing=0
- reject_dist={"hard_excluded": 94, "resolution_low": 133, "duplicate_title": 43, "mime_unsupported": 142, "title_names_other_station": 161, "license_unclear": 3, "no_author_metadata": 7, "title_non_station_scene": 7}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 revert-n — 2026-11-05T18:44:53Z
- 撤站 st00716；原因：非站景：单轨高架轨道街景照无站体(round5 GPS 234m 误收)


## ws15 finalize missing 补漏 — 2026-11-05T18:48:46Z
- st02036 彦根口(滋賀)：rounds1-4 仅彦根駅闸口/他站候选，无本站合格候选


## ws15 local accept batch5 — 2026-11-05T18:55:22Z
- st05521 京王永山 ← File:Keio-railway-KO40-Keio-nagayama-station-platform-20130711-145642.jpg (done)
- st05329 安芸長束 ← File:Aki-Nagatsuka Station building 2.jpg (done)
- st03844 近鉄下田 ← File:Kintetsu-Shimoda stn.jpg (review)
- 拒收标缺 7 站（同名异线/异县）：st00190 稲荷町(広島広電)←东京 Metro、st00571 栄(岡山水島)←名古屋名城线、st00827 東野(岐阜明知)←京都市营、st01249 長尾(大阪JR)←ことでん香川、st01523 霞ケ関(埼玉東上)←东京 Metro、st02692 今津(大分)←阪神兵庫、st01474 泉(福島常磐)←九州新干线出水系泉(鹿児)。


## ws15 finalize missing — 2026-11-05T18:56:59Z
- st00190 稲荷町(広島広電)：候选为东京 Metro 稲荷町(同名异线)，无本站合格候选
- st00571 栄(岡山水島本線)：候选为名古屋名城线栄(同名异线)，无本站合格候选
- st00827 東野(岐阜明知線)：候选为京都市营 T06 東野(同名异线)，无本站合格候选
- st01249 長尾(大阪JR片町線)：候选为ことでん長尾(香川,同名异线)，无本站合格候选
- st01474 泉(福島常磐線)：候选 Izumi Station 为九州(鹿児)出水系大型站房(同名异县)，无本站合格候选
- st01523 霞ケ関(埼玉東上線)：候选为东京 Metro 霞ケ関(同名异线)，无本站合格候选
- st02692 今津(大分日豊本線)：候选为阪神今津(兵庫,同名异线,邻站 Kusugawa/Hanshin-kokudo 证)，无本站合格候选
- wrong_station 15 队列与 ws16 异国 10 队列至此全部处置完毕（补图/标缺），未覆盖站转 B2 客流策略续抓。


## ws15 refetch round 1 — 2026-11-05T19:09:56Z
- queue: wrong_station 重抓队列 41 站（stage=mismatch_removal）
- accepted(GPS<=2km)=9 staged_no_gps=29 still_missing=3
- reject_dist={"mime_unsupported": 252, "duplicate_title": 10, "resolution_low": 74, "title_names_other_station": 154, "hard_excluded": 30, "title_non_station_scene": 5, "license_unclear": 5, "no_author_metadata": 5}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 revert-n — 2026-11-05T19:47:28Z
- 撤站 st00353；原因：LOCAL6复核:既存图为冲绳Yui Rail市立病院前(同名异线错挂,横幅Naha City Hospital Station+单轨轨梁),目标为鹿児岛市电停留场


## ws15 local accept batch6 — 2026-11-05T19:49:03Z
- st02739 播磨町 ← File:Sanyo Harimacho Station.jpg (done)
- st03029 清児 ← File:Sechigo station Mizuma railway.jpg (review)
- st03489 筑前植木 ← File:JRKyushu Chikuzenueki Station01.jpg (review)
- st03516 備後本庄 ← File:Bingo-honjo Station.jpg (done)
- st03843 築山 ← File:Tsukiyama stn.jpg (review)
- st04818 西線9条旭山公園通 ← File:Sapporo Street Car Nishisen Kujo Asahiyama Koen Dori Station.jpg (review)
- st05067 平城 ← File:Kintetsu-Heijo-station01.jpg (done)
- st05315 安登 ← File:Ato station.jpg (review)
- st05911 鹿王院 ← File:嵐電鹿王院駅嵐山方面ホーム.JPG (review)
- st05925 鳴滝 ← File:京福鳴滝駅2.JPG (review)
- st06035 稲戸井 ← File:Kantetsu inatoi-station.jpg (review)
- st06994 安部山公園 ← File:Abeyamakoen station2.jpg (review)
- st07049 薩摩松元 ← File:JR Kyushu Satsuma-Matsumoto station.jpg (review)
- st07245 安岡 ← File:YasuokaStation.jpg (done)
- st07672 越中舟橋 ← File:Etchuufunahashi sta1.jpg (review)
- st07684 五百石 ← File:Gohyakukoku Station.jpg (done)
- st07857 床波 ← File:Tokonamistation.jpg (review)
- st07975 清峰高校前 ← File:Seiho koukou mae station.jpg (review)
- st08515 西富山 ← File:Nishi-Toyama Station 2020.jpg (done)
- st08535 勢野北口 ← File:Seyakitaguchi Station.jpg (done)
- st08538 元山上口 ← File:Motosanjoguchi Station.jpg (done)
- st08539 萩の台 ← File:Haginodai stn.jpg (review)
- st08734 福島学院前 ← File:Fukushimagakuimmae Station.jpg (review)
- st08739 保原 ← File:Hobara Station.jpg (review)
- 拒收标缺 5 站见 finalize6：st00353 市立病院前(鹿児)←冲绳 Yui Rail 同名异线、st00716 北方(福岡)←美濃北方(岐阜)/警察署/巴士总站、st04604 山田西町 无站名标识、st06696 美濃川合←发电站非站景、st07039 吉富←社区巴士非站景。
- st00353 HEAD 既存错挂图(冲绳 Yui Rail)经 revert-n 撤除。


## ws15 finalize missing batch6 — 2026-11-05T19:57:39Z
- st00353 市立病院前(鹿児島市電)：round6 候选 2 张均为冲绳 Yui Rail 那霸市立病院前(同名异线)；HEAD 既存错挂图亦为 Yui Rail(横幅 Naha City Hospital Station)，revert-n 撤除后候选枯竭
- st00716 北方(福岡小倉線)：候选为美濃北方(岐阜,废站)站舍/北方警察署(岐阜)/巴士总站，同名异县+非站景，无本站合格候选
- st04604 山田西町(高知土赞线)：唯一候选为无站名标识的无人站台照，站牌 OCR/目检未见站名不算通过，候选枯竭
- st06696 美濃川合(岐阜太多线)：唯一候选为发电站(Minokawai power station)非站景，候选枯竭
- st07039 吉富(福岡)：候选 2 张均为吉富町社区巴士/大交北部巴士，非站景(巴士)，候选枯竭


## ws15 refetch round 1 — 2026-11-05T20:12:49Z
- queue: wrong_station 重抓队列 40 站（stage=mismatch_removal）
- accepted(GPS<=2km)=10 staged_no_gps=21 still_missing=9
- reject_dist={"title_names_other_station": 157, "duplicate_title": 6, "mime_unsupported": 261, "resolution_low": 50, "hard_excluded": 28, "license_unclear": 14, "license_forbidden": 6, "no_author_metadata": 2, "near_duplicate": 1, "title_non_station_scene": 4}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 local accept batch7 — 2026-11-05T20:26:40Z
- st00548 河原 ← File:JRW kawahara sta.jpg (done)
- st02524 切石 ← File:Kiriishi-sta.jpg (review)
- st03028 石才 ← File:Ishizai-station-2022.jpg (done)
- st03367 池尻 ← File:JRKyushu Ikejiri Station02.jpg (review)
- st03383 上三緒 ← File:Kamimio Station.JPG (review)
- st04956 葛 ← File:Kuzu stn.jpg (review)
- st05364 大乗 ← File:Onori stn.jpg (review)
- st06503 感田 ← File:Ganda Station.jpg (done)
- st07515 やながわ希望の森公園前 ← File:Yanagawa-kibounomori-kouemmae Station 02.jpg (review)
- st07676 新庄田中 ← File:Shinjyotanakaeki.JPG (done)
- st07683 榎町 ← File:Enokimachi sta1.jpg (review)
- st07861 南中川 ← File:Minaminakagawa stn.jpg (review)
- st08674 中野松川 ← File:Nakanomatsukawa sta.jpg (review)
- st08738 上保原 ← File:Kamihobara Station.jpg (review)
- 拒收标缺 7 站见 finalize7：st00040 大谷(和歌)←韩国大邱/版画、st01459 小泉町(富山軌道)←群马东武小泉町同名异线、st03765 鹿児←巴士错区域、st04575 高水←标题他站 Ikusabata、st05365 安芸長浜/st06253 青野ケ原 无站名标识、st07707 西滑川←历史黑白照无站牌。


## ws15 finalize missing batch7 — 2026-11-05T20:29:23Z
- st00040 大谷(和歌山線)：候选为韩国大邱 Daegok 站台(异国)与东海道五十三次版画x2(非站景)，无本站可验证候选
- st01459 小泉町(富山軌道線支線)：候选 3 张均为群马东武小泉町线小泉町(TI45,同名异线)，OCR 命中亦为他站牌
- st03765 鹿児(高知伊野線)：候选 2 张均为巴士照(Kako-bus,OCR 见西加古川駅/姫路=兵库区域)，非站景+错区域
- st04575 高水(山口)：候选标题均为 Ikusabata Station(他站)，标题站名闸门拒；OCR/目检无本站名
- st05365 安芸長浜(広島呉線)：唯一候选为圆顶站房远景无站名标识，站牌 OCR/目检未见站名不算通过
- st06253 青野ケ原(兵庫加古川線)：候选 2 张(Former Aonogahara stn)站牌均不清晰可读，不算通过
- st07707 西滑川(富山地鉄本線)：唯一候选为历史黑白扫描照，仅图外 caption 有站名，场景内无站牌


## ws15 refetch round 1 — 2026-11-05T20:45:07Z
- queue: wrong_station 重抓队列 40 站（stage=mismatch_removal）
- accepted(GPS<=2km)=7 staged_no_gps=19 still_missing=14
- reject_dist={"title_names_other_station": 124, "duplicate_title": 3, "mime_unsupported": 257, "resolution_low": 67, "title_non_station_scene": 9, "hard_excluded": 13, "license_unclear": 13}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 local accept batch8 — 2026-11-05T21:05:10Z
- st03783 鳴谷 ← File:Tosaden NarutaniDentei.JPG (done)
- st04648 小村神社前 ← File:Omurajinjamae stn.jpg (review)
- st04683 海浦 ← File:Uminoura Station 3.JPG (done)
- st05192 備前福河 ← File:Bizen-Fukukawa Station.jpg (done)
- st06886 伊予平野 ← File:Iyo-Hirano stn.jpg (review)
- st07509 南角田 ← File:MinamikakudaEki2005-4.jpg (review)
- st07671 越中泉 ← File:Etchuuizumi sta1.jpg (review)
- st07972 潜竜ケ滝 ← File:Mr senryugataki station.jpg (review)
- st07982 三代橋 ← File:Mr midaibashi station.jpg (review)
- st08194 子吉 ← File:Koyoshi station.jpg (review)
- st08232 江崎 ← File:Esakistation.jpg (review)
- st08737 高子 ← File:Takako Station.jpg (review)
- st08807 磯鶏 ← File:Sokei-Sta01.JPG (review)
- 拒收标缺 6 站见 finalize8：st05977 東開聞 列车田野远景无站名、st07712 早月加積 3 候选均无站名、st07964 中田平 遗迹导览牌无站名、st08280 真倉 无站名+抽象图、st08405 林 乘车口牌/葡萄牙 Oriente(异国)、st08736 向瀬上 无站名。


## ws15 revert-n — 2026-11-05T21:11:42Z
- 撤站 st03600；原因：round8 GPS 接受复核撤除: 标题 View near Ikoinomura Station, GPS 584m, 目检为路口草地纯风景无站房站台站牌, 非站景


## ws15 finalize missing batch8 — 2026-11-05T21:13:22Z
- st05977 東開聞(指宿枕崎線)：唯一候选为列车田野远景(标题東開聞駅列車)，站名不可读，非站景主体
- st07712 早月加積(富山地鉄本線)：3 候选均无站名(/1 警察官重点パトロール駅横幅、/2 2番線のりば吊牌、/3 站房+重点バス停留所横幅)
- st07964 中田平(松浦鉄道西九州線)：候选为站房远景+里田原遺跡/歴史民俗資料館导览牌，场景内无站名标识
- st08280 真倉(舞鶴線)：/1 山坡停车场远景无站名、/2 蓝色抽象图形非站照
- st08405 林(城端線)：/1 候车亭竖牌为「ワンマン乗車口」非站名、/2/3 为葡萄牙里斯本 CP Oriente 站(异国, Saída 出口牌)
- st08736 向瀬上(阿武隈急行線)：唯一候选为高架站房/跨线桥远景，无站名标识


## ws15 refetch round 1 — 2026-11-05T21:27:53Z
- queue: wrong_station 重抓队列 33 站（stage=mismatch_removal）
- accepted(GPS<=2km)=5 staged_no_gps=12 still_missing=16
- reject_dist={"resolution_low": 41, "title_names_other_station": 132, "duplicate_title": 3, "mime_unsupported": 130, "title_non_station_scene": 3, "hard_excluded": 10, "no_author_metadata": 2, "license_unclear": 1}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 local accept batch9 — 2026-11-05T21:40:37Z
- st00317 升形 ← File:Masukata station.jpg (review)
- st03414 新月 ← File:JR East Niitsuki Station Platform, Iwate Pref.jpg (done)
- st05088 比津 ← File:Hitsu stn 1.jpg (review)
- st08226 越ケ浜 ← File:Kosigahamastation.jpg (review)
- st08287 五十猛 ← File:五十猛駅 ホーム.jpg (done)
- st08318 ほうらい丘 ← File:坂本ケーブルほうらい丘駅.JPG (review)
- st08816 吉里吉里 ← File:Kirikiri station,Otsuchi.jpg (review)
- 拒收标缺 5 站见 finalize9：st03280 小杉(富山)←武蔵小杉(神奈川)异县错挂、st04602 六条(福井)←车照/名古屋泵站/札幌市电西線六条同名异线、st04643 土佐岩原←列车主体无站名、st06057 鶴丸←NHK 电波塔非站景、st06247 新西脇←警察官駐在所牌无站名。


## ws15 revert-n — 2026-11-05T21:47:07Z
- 撤站 st01628 st04564；原因：round9 GPS 接受复核撤除: st01628 为秋田新干线こまち行驶照无站(标题他站 Shoden); st04564 为夜间近黑照(阶梯+天桥)无站名标识


## ws15 finalize missing batch9 — 2026-11-05T21:48:03Z
- st03280 小杉(富山上滝線)：2 候选均为 JR 武蔵小杉(神奈川)新南改札/横須賀線口，异县错挂；OCR「小杉」为武蔵小杉子串误命中
- st04602 六条(ハピラインふくい線)：候选=车照(Toyota 86)/名古屋市六条泵站/札幌市電西線六条(北海道同名异线)，无本站候选
- st04643 土佐岩原(土讃線)：唯一候选为 Kiha58 列车站台停靠主体照，无站名牌可读，非站景主体
- st06057 鶴丸(吉都線)：唯一候选为 NHK-JOG-FM 鹿児(鶴丸)电波塔照，非站景
- st06247 新西脇(加古川線)：唯一候选站房竖牌为「警察官駐在所」(裁切放大确认)，场景内无站名标识


## ws15 refetch round 1 — 2026-11-05T21:57:08Z
- queue: wrong_station 重抓队列 12 站（stage=mismatch_removal）
- accepted(GPS<=2km)=0 staged_no_gps=1 still_missing=11
- reject_dist={"title_names_other_station": 43, "duplicate_title": 2, "mime_unsupported": 8, "hard_excluded": 6, "resolution_low": 16, "title_non_station_scene": 1, "no_author_metadata": 2}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws15 finalize missing batch10 — 2026-11-05T22:04:19Z
- st01628 生田(秋田県)：round10 暂存 3 候选均为神奈川生田(小田急小田原線站台/小田急生田駅牌目检确认/JR 生田)，同名异线；此前 round9 GPS 接受项为新干线行驶照已撤(REVERT7)；候选池枯竭


## ws15 refetch round 1 — 2026-11-05T22:11:23Z
- queue: wrong_station 重抓队列 5 站（stage=mismatch_removal）
- accepted(GPS<=2km)=0 staged_no_gps=0 still_missing=5
- reject_dist={"no_author_metadata": 2, "resolution_low": 3, "mime_unsupported": 3, "title_names_other_station": 9}
- 无 GPS 候选经 artifact 回传，本地 OCR+目检后另行提交；证据见 reports/ws15_refetch_evidence.json


## ws17 below-spec replace WS17-B01 — 2026-11-05T22:53:44Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=3 staged=17 confirmed=5 skipped=0
- reject_dist={"hard_excluded": 48, "same_as_current": 25, "resolution_low_lt_1600": 62, "title_names_other_station": 76, "mime_unsupported": 61, "title_non_station_scene": 11, "duplicate_title": 2, "no_author_metadata": 9, "resolution_not_upgrade": 17, "quality_reject_low_color": 10}


## ws17 local accept B01 — 2026-11-05T23:17:55Z
- st02672 河内花園 ← File:Kawachi-Hanazono Station north entrance.jpg (done, score 6.53→6.23)
- st05704 文の里 ← File:Fuminosato station exit 4.jpg (done, score 6.54→6.46)
- st05719 田辺 ← File:Tanabe station exit.jpg (done, score 6.26→6.30)
- st06640 岸里 ← File:Entrance No.2 of Kishinosato Station 2.jpg (done, score 6.01→5.00)
- st06967 千林 ← File:Keihan Senbayashi Station platform - panoramio.jpg (done, score 6.51→5.39)
- st08365 新深江 ← File:Shin-Fukae station exit 1.jpg (done, score 6.58→6.22)
- st01324 JR河内永和 ← File:JR-Kawachi-Eiwa Station 2019,08.jpg (done, score 6.58→6.17)
- st06575 维持现图 below_spec_confirmed：候选全为银行/超市/人像（りそな銀行/食品館アプロ/初芝崇史）非站景
- st02549 维持现图 below_spec_confirmed：候选竖幅街景停留场，无站名牌可读，分不优于现图
- st02573 维持现图 below_spec_confirmed：候选竖幅街景，塚西停留场柱牌可见但构图/分不优于现图
- st02574 维持现图 below_spec_confirmed：候选街景轨道照，无东玉出停留场牌可读
- st03851 维持现图 below_spec_confirmed：候选全为法善寺寺庙照，非站景
- st04004 维持现图 below_spec_confirmed：候选夜景月台无站名/列车照（JR201/287 系）
- st08464 维持现图 below_spec_confirmed：候选全为西塚/服部川古坟群照，非站景
- st06611 维持现图 below_spec_confirmed：唯一站名候选为竖幅 iscore3.68<5.0，引入 low_score 新缺陷
- st08054 维持现图 below_spec_confirmed：候选竖幅 iscore3.25，现图缺陷为 low_score 无更优候选
- st06609 维持现图 below_spec_confirmed：候选竖幅 iscore3.49，引入 low_score 新缺陷
- runner 42124115966 暂存 47 候选/17 站全量 OCR(全名匹配)+逐图目检；接受 7 / 标 below_spec_confirmed 10。


## ws15 revert-n（本地 API，零 Actions 分钟） — 2026-11-06T01:30:57Z
- 撤站 st01215 st01213；原因：st01215 错挂 JR 木幡（唯一站证「JR 木幡」牌=st01213 之站，站证反向，审计 P1）；st01213 现图标题 Shintetsu Kobata（神铁同名异线）且框内无可读站牌，身份未证
- 两站回重抓队列（stage=mismatch_removal）；st01215 撤下图经目检为 JR 木幡站证清晰图，重抓 st01213 时可作候选
- 零分钟通道：GitHub git-data API 单提交（base_tree + sha:null 删除），force=false，推后回读


## ws17 below-spec replace WS17-B02 — 2026-11-06T03:25:46Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=24 confirmed=1 skipped=0
- reject_dist={"same_as_current": 24, "resolution_low_lt_1600": 113, "hard_excluded": 64, "resolution_not_upgrade": 43, "title_names_other_station": 99, "quality_reject_low_color": 22, "mime_unsupported": 23, "title_non_station_scene": 11, "no_author_metadata": 17, "duplicate_title": 7, "license_unclear": 2}


## ws17 local accept B02 — 2026-11-06T03:50:02Z
- st05710 東梅田 ← File:Higashi-umeda Platform Track 2.jpg (done, score 6.65→7.18)
- st01071 维持现图 below_spec_confirmed：唯一超分候选为「お願い」告示牌特写，无站名证据
- st01126 维持现图 below_spec_confirmed：候选分均低于现图 6.98
- st01255 维持现图 below_spec_confirmed：候选分均低于现图 6.74（闸机/公寓照）
- st01289 维持现图 below_spec_confirmed：唯一超分候选为小学照非站景
- st01999 维持现图 below_spec_confirmed：候选分均低于现图 6.81
- st02000 维持现图 below_spec_confirmed：超分候选为道口轨道远景，框内无站名牌
- st02555 维持现图 below_spec_confirmed：候选分均低于现图 7.02（阪堺列车照）
- st02656 维持现图 below_spec_confirmed：候选分均低于现图 7.02（奶箱/电器广告照）
- st03239 维持现图 below_spec_confirmed：候选分均低于现图 7.02
- st03671 维持现图 below_spec_confirmed：候选分均低于现图 7.07（阪急曽根但分不足）
- st04876 维持现图 below_spec_confirmed：OCR 命中中津为大阪メトロ中津出入口，记录线路为阪急→运营商前缀不符新闸拒；其余分不足
- st04881 维持现图 below_spec_confirmed：候选分均低于现图 6.94
- st04969 维持现图 below_spec_confirmed：候选分均低于现图 6.78
- st04971 维持现图 below_spec_confirmed：OCR 命中矢田为名鉄矢田（名古屋），记录为近鉄→运营商前缀不符新闸拒
- st04977 维持现图 below_spec_confirmed：候选全为车展汽车照非站景
- st05716 维持现图 below_spec_confirmed：OCR 全名命中千林大宮但 iscore6.33<现 7.06 分差不足
- st06573 维持现图 below_spec_confirmed：唯一超分候选为南海 2200 系天空列车照非站景
- st06574 维持现图 below_spec_confirmed：候选为南海 600 系列车照且分低于现图
- st06576 维持现图 below_spec_confirmed：候选分均低于现图 6.91；OCR 命中白鷺来自商铺「白鷺駅前店」招牌非站牌
- st06581 维持现图 below_spec_confirmed：候选为南海列车照/阪堺停留场且分低于现图 6.82
- st06736 维持现图 below_spec_confirmed：候选分均低于现图 7.03（阪急崇禅寺但分不足）
- st06969 维持现图 below_spec_confirmed：OCR 全名命中京阪土居且运营商匹配但 iscore6.63<现 6.79 分差不足
- st08055 维持现图 below_spec_confirmed：OCR 命中高師浜来自诊所地址牌非站牌；其余分不足
- runner <B02_RUN_ID> 暂存候选全量 OCR(全名匹配)+逐图目检；接受 1 / 标 below_spec_confirmed 23。


## ws17 below-spec replace WS17-B03 — 2026-11-06T04:03:46Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=23 confirmed=1 skipped=0
- reject_dist={"same_as_current": 25, "hard_excluded": 56, "quality_reject_low_color": 22, "resolution_low_lt_1600": 118, "duplicate_title": 7, "title_names_other_station": 62, "mime_unsupported": 39, "resolution_not_upgrade": 80, "title_non_station_scene": 5, "no_author_metadata": 3, "license_forbidden": 4, "license_unclear": 2, "quality_reject_white_screenshot": 1}


## ws17 B03 revert（本地 API，零分钟） — 2026-11-06T04:10:56Z
- 撤 st03236：runner 自动替换图目检为厕所照（标题「阪急吹田駅トイレ」含站名过标题闸但主体非站景）；且旧图「JR West Suita」与阪急记录运营商不符=同名异运营商第 6 簇（JR 吹田 vs 阪急吹田）；回重抓队列
- 闸门补丁：NON_SCENE 黑名单加 toilet/restroom/トイレ/化粧室


## ws17 local accept B03 — 2026-11-06T04:16:21Z
- st01284 维持现图 below_spec_confirmed：候选 iscore5.8<现 7.24 分差不足
- st01988 维持现图 below_spec_confirmed：最优候选 7.08<现 7.12 分差不足
- st02548 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st02917 维持现图 below_spec_confirmed：OCR 命中来自货车常备铭牌非站牌且分不足
- st03253 维持现图 below_spec_confirmed：无站名命中（ monorail 延伸广告/商铺照）
- st03847 维持现图 below_spec_confirmed：无站名命中（近铁发车标示无站名）
- st03967 维持现图 below_spec_confirmed：无站名命中
- st04793 维持现图 below_spec_confirmed：无站名命中（换乘案内/改名案内牌）
- st04870 维持现图 below_spec_confirmed：候选 6.28<现 7.13 分差不足
- st04882 维持现图 below_spec_confirmed：候选 6.83<现 7.18 分差不足
- st04883 维持现图 below_spec_confirmed：OCR 命中 JR 長居与御堂筋線记录运营商不符+分不足
- st04889 维持现图 below_spec_confirmed：候选 5.89<现 7.07 分差不足
- st04935 维持现图 below_spec_confirmed：OCR 命中来自诊所招牌语境且 5.97<7.33
- st04970 维持现图 below_spec_confirmed：无站名命中
- st05725 维持现图 below_spec_confirmed：候选 6.6<现 7.08 分差不足
- st05950 维持现图 below_spec_confirmed：候选 6.26<现 7.21 分差不足
- st06549 维持现图 below_spec_confirmed：无站名命中（银行/广告牌）
- st06582 维持现图 below_spec_confirmed：候选 6.5<现 7.09 分差不足
- st07410 维持现图 below_spec_confirmed：无站名命中
- st07420 维持现图 below_spec_confirmed：候选 6.42<现 7.28 分差不足
- st07424 维持现图 below_spec_confirmed：候选 4.86<现 7.3 分差不足
- st08366 维持现图 below_spec_confirmed：无站名命中（江之电标题 runner 已拒）
- st08451 维持现图 below_spec_confirmed：候选为 JR225 系列车照且分不足
- runner 42159311966 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 23。


## ws17 below-spec replace WS17-B04 — 2026-11-06T04:24:42Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=24 confirmed=0 skipped=0
- reject_dist={"title_names_other_station": 128, "resolution_low_lt_1600": 84, "same_as_current": 25, "hard_excluded": 57, "title_non_station_scene": 22, "quality_reject_low_color": 16, "resolution_not_upgrade": 57, "duplicate_title": 9, "no_author_metadata": 5, "mime_unsupported": 10, "near_duplicate": 1, "oversize_gt_25mb": 7}


## ws17 local accept B04 — 2026-11-06T04:33:07Z
- st01260 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st02547 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st02556 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st02558 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st02567 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st02679 维持现图 below_spec_confirmed：候选 6.84<现 7.41 分差不足
- st02684 维持现图 below_spec_confirmed：候选 6.73<现 7.49 分差不足
- st03447 维持现图 below_spec_confirmed：候选 6.41<现 7.53 分差不足
- st03850 维持现图 below_spec_confirmed：OCR 命中 Onji 为观音寺（香川）语境且 6.78<7.53
- st04787 维持现图 below_spec_confirmed：候选 5.55<现 7.58 分差不足
- st04937 维持现图 below_spec_confirmed：候选 6.01<现 7.53 分差不足
- st05714 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st05717 维持现图 below_spec_confirmed：候选 7.07<现 7.59 分差不足
- st05718 维持现图 below_spec_confirmed：候选 6.57<现 7.51 分差不足
- st05952 维持现图 below_spec_confirmed：候选 6.99<现 7.51 分差不足
- st06639 维持现图 below_spec_confirmed：候选 6.77<现 7.35 分差不足
- st06707 维持现图 below_spec_confirmed：候选 6.38<现 7.35 分差不足
- st06962 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st06964 维持现图 below_spec_confirmed：候选 6.74<现 7.64 分差不足
- st06966 维持现图 below_spec_confirmed：无站名命中且候选分不足
- st07374 维持现图 below_spec_confirmed：候选 6.58<现 7.61 分差不足
- st07376 维持现图 below_spec_confirmed：候选 7.07<现 7.54 分差不足
- st08369 维持现图 below_spec_confirmed：候选 6.48<现 7.54 分差不足
- st08408 维持现图 below_spec_confirmed：候选 6.17<现 7.45 分差不足
- runner 42161614385 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 24。


## ws17 below-spec replace WS17-B05 — 2026-11-06T04:43:53Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"resolution_not_upgrade": 51, "same_as_current": 25, "resolution_low_lt_1600": 94, "hard_excluded": 87, "quality_reject_low_color": 25, "no_author_metadata": 15, "title_names_other_station": 68, "title_non_station_scene": 19, "mime_unsupported": 9, "duplicate_title": 3, "oversize_gt_25mb": 2}


## ws17 local accept B05 — 2026-11-06T04:48:48Z
- st00071 维持现图 below_spec_confirmed：无站名命中且候选最高 6.85<=7.99
- st01776 维持现图 below_spec_confirmed：无站名命中且候选最高 6.22<=7.72
- st01953 维持现图 below_spec_confirmed：无站名命中且候选最高 5.99<=7.66
- st02047 维持现图 below_spec_confirmed：无站名命中且候选最高 6.48<=7.71
- st02563 维持现图 below_spec_confirmed：无站名命中且候选最高 6.93<=7.65
- st02580 维持现图 below_spec_confirmed：命中 新今宮駅前 但 6.44<=7.68 分差不足
- st03033 维持现图 below_spec_confirmed：无站名命中且候选最高 6.33<=7.88
- st03251 维持现图 below_spec_confirmed：无站名命中且候选最高 6.32<=7.76
- st03252 维持现图 below_spec_confirmed：无站名命中且候选最高 5.34<=7.98
- st03456 维持现图 below_spec_confirmed：无站名命中且候选最高 6.58<=7.73
- st03855 维持现图 below_spec_confirmed：命中 長瀬 但 6.75<=8.13 分差不足
- st04779 维持现图 below_spec_confirmed：无站名命中且候选最高 6.36<=7.75
- st04780 维持现图 below_spec_confirmed：无站名命中且候选最高 6.36<=7.75
- st04869 维持现图 below_spec_confirmed：无站名命中且候选最高 7.11<=8.32
- st04877 维持现图 below_spec_confirmed：命中 Umeda 但 7.03<=7.72 分差不足
- st05113 维持现图 below_spec_confirmed：无站名命中且候选最高 6.49<=8.15
- st05114 维持现图 below_spec_confirmed：无站名命中且候选最高 6.31<=8.00
- st05708 维持现图 below_spec_confirmed：无站名命中且候选最高 6.97<=8.13
- st05877 维持现图 below_spec_confirmed：命中 井高野 但 7.80<=7.80 分差不足
- st06540 维持现图 below_spec_confirmed：命中 大和田 但 7.07<=8.00 分差不足
- st06578 维持现图 below_spec_confirmed：无站名命中且候选最高 6.33<=8.29
- st06704 维持现图 below_spec_confirmed：命中 北千里 但 6.35<=7.89 分差不足
- st06718 维持现图 below_spec_confirmed：命中 総持寺 但 6.50<=7.68 分差不足
- st06965 维持现图 below_spec_confirmed：命中 関目 但 6.46<=8.05 分差不足
- st08368 维持现图 below_spec_confirmed：命中 Minami-Tatsumi 但 7.15<=7.72 分差不足
- runner 42163290441 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 25。


## ws17 below-spec replace WS17-B06 — 2026-11-06T04:56:04Z
- queue: 8 站（review/below_spec 高分替换）
- replaced=0 staged=8 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 36, "hard_excluded": 38, "title_non_station_scene": 5, "same_as_current": 8, "quality_reject_low_color": 5, "title_names_other_station": 13, "resolution_not_upgrade": 10}


## ws17 local accept B06 — 2026-11-06T04:58:42Z
- st01788 维持现图 below_spec_confirmed：无站名命中且最高 6.59<8.97
- st03848 维持现图 below_spec_confirmed：命中 河内山本 但 6.34<8.64 分差不足
- st06558 维持现图 below_spec_confirmed：无站名命中且最高 5.68<8.76
- st06705 维持现图 below_spec_confirmed：命中 南千里 但 6.62<8.66 分差不足
- st06717 维持现图 below_spec_confirmed：无站名命中且最高 6.78<8.59
- st08112 维持现图 below_spec_confirmed：无站名命中且最高 6.26<8.39
- st08533 维持现图 below_spec_confirmed：无站名命中且最高 6.17<9.16
- st08727 维持现图 below_spec_confirmed：无站名命中且最高 6.79<8.56
- runner 42164807440 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 8。


## ws17 below-spec replace WS17-B07 — 2026-11-06T05:08:30Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=4 staged=21 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 178, "no_author_metadata": 17, "same_as_current": 25, "mime_unsupported": 31, "resolution_not_upgrade": 30, "quality_reject_low_color": 35, "title_non_station_scene": 7, "hard_excluded": 31, "license_unclear": 3, "title_names_other_station": 56, "duplicate_title": 5}


## ws17 B07 revert（P0，本地 API 零分钟） — 2026-11-06T05:17:42Z
- 撤 st02165 新宿：runner 自动替换图目检为 JR 新宿站全景招牌（Shinjuku Station 新宿駅），记录线路仅丸ノ内線→运营商不符=P0；恢复替换前 review 态旧图旧元数据（photo/license blob 复用旧 sha）


## ws17 local accept B07 — 2026-11-06T05:23:05Z
- st00897 四ツ木 ← File:Yotsugi-STA Entrance.jpg (done, score 5.61→7.07)
- st03937 武蔵砂川 ← File:Musashi-Sunagawa sta2020-2.jpg (done, score 6.59→7.50)
- st05520 京王多摩センター ← File:Keio-Tama-Center-Sta-Gate.JPG (done, score 6.93→6.95)
- st05569 京王堀之内 ← File:Keio-Horinouchi-Sta-S.JPG (done, score 5.14→6.90)
- st08377 沼部 ← File:Numabe Station 2024 May 30 various 16 15 53 422000.jpeg (done, score 6.44→6.75)
- st00493 维持现图 below_spec_confirmed：OCR 命中高野为 JR 西日本姫新線高野（JR 标识），记录日暮里・舎人ライナー→运营商不符拒
- st00930 维持现图 below_spec_confirmed：候选最高 6.52 vs 现 6.63 分差不足或无站名命中
- st00931 维持现图 below_spec_confirmed：候选最高 6.76 vs 现 6.55 分差不足或无站名命中
- st01526 维持现图 below_spec_confirmed：候选最高 6.49 vs 现 6.84 分差不足或无站名命中
- st01529 维持现图 below_spec_confirmed：候选最高 7.16 vs 现 6.41 分差不足或无站名命中
- st01863 维持现图 below_spec_confirmed：候选最高 7.14 vs 现 6.55 分差不足或无站名命中
- st01867 维持现图 below_spec_confirmed：候选最高 5.25 vs 现 6.57 分差不足或无站名命中
- st02135 维持现图 below_spec_confirmed：候选最高 5.34 vs 现 6.52 分差不足或无站名命中
- st03700 维持现图 below_spec_confirmed：候选最高 5.71 vs 现 6.66 分差不足或无站名命中
- st03896 维持现图 below_spec_confirmed：候选最高 7.10 vs 现 6.75 分差不足或无站名命中
- st03935 维持现图 below_spec_confirmed：候选最高 6.68 vs 现 6.84 分差不足或无站名命中
- st05563 维持现图 below_spec_confirmed：候选最高 6.18 vs 现 6.77 分差不足或无站名命中
- st06227 维持现图 below_spec_confirmed：候选最高 6.56 vs 现 6.70 分差不足或无站名命中
- st06236 维持现图 below_spec_confirmed：候选最高 5.95 vs 现 6.72 分差不足或无站名命中
- st07871 维持现图 below_spec_confirmed：候选最高 6.32 vs 现 6.70 分差不足或无站名命中
- st07884 维持现图 below_spec_confirmed：候选最高 5.88 vs 现 6.89 分差不足或无站名命中
- runner 42165678188 暂存候选全量 OCR(全名匹配)+逐图目检；接受 5 / 标 below_spec_confirmed 16。


## ws17 below-spec replace WS17-B08 — 2026-11-06T05:34:16Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 253, "same_as_current": 25, "mime_unsupported": 38, "hard_excluded": 32, "quality_reject_low_color": 17, "title_names_other_station": 65, "title_non_station_scene": 2, "duplicate_title": 3, "resolution_not_upgrade": 24, "quality_reject_blurry": 1, "no_author_metadata": 11, "oversize_gt_25mb": 1, "license_unclear": 1}


## ws17 local accept B08 — 2026-11-06T05:40:13Z
- st01533 维持现图 below_spec_confirmed：无站名命中且最高 7.14<7.16
- st01536 维持现图 below_spec_confirmed：命中 千歳船橋 但 6.83<7.26
- st01645 维持现图 below_spec_confirmed：命中 小田急永山 但 6.79<7.26
- st01734 维持现图 below_spec_confirmed：命中 一橋学園 但 6.38<7.10
- st01735 维持现图 below_spec_confirmed：无站名命中且最高 6.80<7.04
- st01741 维持现图 below_spec_confirmed：命中 Musashiseki 但 6.64<7.00
- st02203 维持现图 below_spec_confirmed：命中 北野 但 6.09<7.10
- st02421 维持现图 below_spec_confirmed：命中 小宮 但 7.39<7.04
- st02422 维持现图 below_spec_confirmed：命中 北八王子 但 6.52<7.34
- st03154 维持现图 below_spec_confirmed：无站名命中且最高 6.85<6.96
- st03174 维持现图 below_spec_confirmed：无站名命中且最高 5.92<7.05
- st03697 维持现图 below_spec_confirmed：无站名命中且最高 5.68<6.97
- st03698 维持现图 below_spec_confirmed：命中 堀切菖蒲園 但 6.84<7.35
- st04538 维持现图 below_spec_confirmed：命中 西武園 但 6.45<7.40
- st04903 维持现图 below_spec_confirmed：命中 南新宿 但 6.62<7.02
- st05550 维持现图 below_spec_confirmed：命中 平山城址公園 但 6.36<7.03
- st05552 维持现图 below_spec_confirmed：无站名命中且最高 5.59<7.17
- st05558 维持现图 below_spec_confirmed：命中 武蔵野台 但 6.44<7.35
- st07872 维持现图 below_spec_confirmed：命中 荒川七丁目 但 6.21<7.34
- st07878 维持现图 below_spec_confirmed：命中 滝野川一丁目 但 5.93<6.94
- st07881 维持现图 below_spec_confirmed：无站名命中且最高 6.65<6.96
- st07883 维持现图 below_spec_confirmed：命中 大塚駅前 但 6.82<7.31
- st08307 维持现图 below_spec_confirmed：无站名命中且最高 5.56<6.95
- st08374 维持现图 below_spec_confirmed：命中 武蔵新田 但 7.02<7.34
- st08549 维持现图 below_spec_confirmed：命中 千鳥町 但 7.10<7.15
- runner 42168299403 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 25。


## ws17 below-spec replace WS17-B09 — 2026-11-06T05:49:42Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"same_as_current": 25, "hard_excluded": 44, "resolution_low_lt_1600": 151, "title_non_station_scene": 11, "resolution_not_upgrade": 14, "mime_unsupported": 46, "title_names_other_station": 110, "quality_reject_low_color": 17, "no_author_metadata": 9, "duplicate_title": 5, "license_unclear": 4}


## ws17 local accept B09 — 2026-11-06T05:54:33Z
- st00468 维持现图 below_spec_confirmed：命中 住吉 但最高 5.24<7.78
- st01521 维持现图 below_spec_confirmed：命中 日比谷 但最高 4.10<7.42
- st01534 维持现图 below_spec_confirmed：命中 豪徳寺 但最高 5.81<7.46
- st01537 维持现图 below_spec_confirmed：无站名命中且最高 3.15<7.62
- st01622 维持现图 below_spec_confirmed：命中 鶴川 但 3.46<7.62
- st01636 维持现图 below_spec_confirmed：命中 和泉多摩川 但最高 7.50<7.63
- st01729 维持现图 below_spec_confirmed：无站名命中且最高 4.13<7.51
- st01748 维持现图 below_spec_confirmed：命中 野方 但最高 6.52<7.50
- st01864 维持现图 below_spec_confirmed：无站名命中且最高 7.18<7.68
- st02167 维持现图 below_spec_confirmed：命中 つくし野 但最高 4.44<7.62（候选为车照）
- st02398 维持现图 below_spec_confirmed：命中 箱根ケ崎 但最高 4.32<7.43
- st03134 维持现图 below_spec_confirmed：无站名命中且最高 3.54<7.76
- st03167 维持现图 below_spec_confirmed：无站名命中且最高 5.91<7.55
- st03178 维持现图 below_spec_confirmed：命中 六本木一丁目 但最高 3.95<7.41
- st03425 维持现图 below_spec_confirmed：无站名命中且最高 7.50<7.77
- st04223 维持现图 below_spec_confirmed：无站名命中且最高 5.91<7.47
- st04495 维持现图 below_spec_confirmed：无站名命中且最高 6.81<7.64
- st04502 维持现图 below_spec_confirmed：命中 中神 但最高 5.81<7.53
- st05467 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.69
- st06234 维持现图 below_spec_confirmed：无站名命中且 4.95<7.76
- st06235 维持现图 below_spec_confirmed：无站名命中且最高 7.37<7.77
- st07864 维持现图 below_spec_confirmed：命中 梶原 但最高 6.64<7.63
- st07887 维持现图 below_spec_confirmed：无站名命中且 2.28<7.64（候选为车照）
- st08305 维持现图 below_spec_confirmed：命中 上板橋 但最高 5.52<7.66
- st08555 维持现图 below_spec_confirmed：命中 洗足池 但最高 1.94<7.57
- runner 42169828734 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 25。


## ws17 P0 revert st00259 — 2026-11-06T06:14:05Z
- st00259 大久保(京都・近鉄) 撤除误挂照 File:JRE Okubo-STA Platform1-2.jpg（实为 JR 东东京大久保，案内牌 OCR「中央・総武線/新宿・秋葉原・千葉方」）；
- 与 st00260(东京) 同 sha256 6b17e1c6（B10 verify 批内 dup 闸门拦截暴露）；
- st00260 现图正确保留；st00259 置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 below-spec replace WS17-B10 — 2026-11-06T06:24:54Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=24 confirmed=1 skipped=0
- reject_dist={"same_as_current": 25, "mime_unsupported": 30, "resolution_low_lt_1600": 180, "title_names_other_station": 118, "hard_excluded": 47, "resolution_not_upgrade": 30, "quality_reject_low_color": 9, "title_non_station_scene": 7, "duplicate_title": 5, "no_author_metadata": 10, "license_unclear": 3, "oversize_gt_25mb": 1}


## ws17 local accept B10 — 2026-11-06T06:29:27Z
- st08053 维持现图 below_spec_confirmed：无站名命中且最高 7.19<7.79
- st01860 维持现图 below_spec_confirmed：无站名命中且最高 5.24<7.83
- st04225 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.88
- st05453 维持现图 below_spec_confirmed：命中 柴崎体育館 但最高 6.52<7.90
- st05560 维持现图 below_spec_confirmed：无站名命中且最高 6.32<7.90
- st00260 维持现图 below_spec_confirmed：候选为秋田大久保(异县)且 6.50<7.94，拒
- st07224 维持现图 below_spec_confirmed：命中 見沼代親水公園 但最高 7.32<7.95
- st04226 维持现图 below_spec_confirmed：命中 豊洲 但最高 5.52<7.98
- st07225 维持现图 below_spec_confirmed：命中 舎人 但最高 6.52<8.00
- st04234 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.01
- st04224 维持现图 below_spec_confirmed：无站名命中且最高 6.68<8.03
- st05535 维持现图 below_spec_confirmed：命中 大島 但最高 5.15<8.03
- st01532 维持现图 below_spec_confirmed：命中 世田谷代田 但最高 6.80<8.04
- st08308 维持现图 below_spec_confirmed：命中 北池袋 但最高 6.32<8.11
- st00916 维持现图 below_spec_confirmed：命中 天空橋 但最高 3.52<8.15（夜景）
- st01488 维持现图 below_spec_confirmed：命中 湯島 但最高 5.50<8.16（候选3 岩手湯島异县拒）
- st01050 维持现图 below_spec_confirmed：无站名命中且最高 5.24<8.18
- st01854 维持现图 below_spec_confirmed：无站名命中且最高 6.52<8.21
- st04240 维持现图 below_spec_confirmed：无站名命中且最高 3.54<8.22
- st01520 维持现图 below_spec_confirmed：无站名命中且最高 4.50<8.37
- st02090 维持现图 below_spec_confirmed：命中 永田町 但最高 5.13<8.44
- st07228 维持现图 below_spec_confirmed：命中 西新井大師西 但最高 6.52<8.44
- st01926 维持现图 below_spec_confirmed：命中 上中里 但最高 6.50<8.76
- st06338 维持现图 below_spec_confirmed：无站名命中且最高 4.52<8.82
- runner 42173343422 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 24。


## ws17 below-spec replace WS17-B11 — 2026-11-06T06:37:52Z
- queue: 7 站（review/below_spec 高分替换）
- replaced=1 staged=6 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 17, "mime_unsupported": 8, "same_as_current": 7, "quality_reject_low_color": 9, "title_names_other_station": 23, "duplicate_title": 2, "license_unclear": 2, "hard_excluded": 12, "resolution_not_upgrade": 7, "title_non_station_scene": 3}


## ws17 local accept B11 — 2026-11-06T06:40:22Z
- st06233 维持现图 below_spec_confirmed：命中 荏原町 但最高 6.50<8.87
- st01492 维持现图 below_spec_confirmed：候选为 JR 西日暮里站台 vs 记录日暮里・舎人ライナー，运营商不符拒；且 5.50<8.88
- st04503 维持现图 below_spec_confirmed：无站名命中且最高 6.60<8.88
- st00592 维持现图 below_spec_confirmed：命中 江北 但最高 4.52<9.04
- st04230 维持现图 below_spec_confirmed：命中 有明 但最高 4.03<9.08
- st03153 维持现图 below_spec_confirmed：命中 西小山 但最高 4.50<9.36
- runner 42174930519 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 6。


## ws17 below-spec replace WS17-B12 — 2026-11-06T06:52:09Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=2 staged=17 confirmed=6 skipped=0
- reject_dist={"same_as_current": 25, "resolution_low_lt_1600": 92, "license_unclear": 16, "hard_excluded": 10, "mime_unsupported": 38, "title_names_other_station": 76, "quality_reject_low_color": 18, "title_non_station_scene": 12, "resolution_not_upgrade": 6, "no_author_metadata": 3, "duplicate_title": 2, "oversize_gt_25mb": 7}


## ws17 local accept B12 — 2026-11-06T06:58:02Z
- st03398 维持现图 below_spec_confirmed：无站名命中且最高 4.80<5.40
- st04820 维持现图 below_spec_confirmed：候选为东京渋谷/新桥(异县)且 2.55<5.88
- st04276 维持现图 below_spec_confirmed：命中 蘭越 但最高 5.04<6.60
- st08644 维持现图 below_spec_confirmed：最高 4.80<6.91（候选3 站牌命中但 2.82）
- st01969 维持现图 below_spec_confirmed：候选为神奈川川崎(异县)且 2.32<6.48
- st04802 维持现图 below_spec_confirmed：雪ミク车照 2.15<6.57
- st04812 维持现图 below_spec_confirmed：无站名命中且最高 2.80<7.07
- st04813 维持现图 below_spec_confirmed：车照 1.76<7.07
- st04307 维持现图 below_spec_confirmed：最高 5.80<6.98（候选2 为 C11 机车照）
- st03943 维持现图 below_spec_confirmed：命中 西帯広 但最高 5.80<6.99
- st03946 维持现图 below_spec_confirmed：命中 幕別 但最高 5.80<7.10
- st01965 维持现图 below_spec_confirmed：命中 杉並町 但最高 2.80<7.05（候选为时钟 plaque/上屋特写）
- st00752 维持现图 below_spec_confirmed：无站名命中且最高 6.08<6.81
- st04799 维持现图 below_spec_confirmed：雪ミク车照最高 3.09<6.29
- st04821 维持现图 below_spec_confirmed：命中 中央区役所前 但最高 3.25<6.74
- st08648 维持现图 below_spec_confirmed：命中系北剣淵子串误命中且最高 5.80<6.97
- st02020 维持现图 below_spec_confirmed：命中 武佐 但最高 4.80<6.95
- runner 42176125711 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 17。


## ws17 below-spec replace WS17-B13 — 2026-11-06T07:10:43Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"same_as_current": 25, "license_unclear": 16, "quality_reject_low_color": 21, "hard_excluded": 31, "title_names_other_station": 64, "resolution_low_lt_1600": 60, "mime_unsupported": 78, "title_non_station_scene": 8, "resolution_not_upgrade": 4, "duplicate_title": 5, "oversize_gt_25mb": 1}


## ws17 local accept B13 — 2026-11-06T07:14:11Z
- st00743 维持现图 below_spec_confirmed：无站名命中且最高 6.80<7.29
- st00759 维持现图 below_spec_confirmed：最高 5.09<7.92（候选2 宮城東北本線白石同名异线拒）
- st00768 维持现图 below_spec_confirmed：无站名命中且最高 6.80<7.80
- st00770 维持现图 below_spec_confirmed：无站名命中且最高 4.39<7.44
- st00780 维持现图 below_spec_confirmed：命中 虎杖浜 但最高 5.80<7.13
- st00792 维持现图 below_spec_confirmed：命中 川端 但最高 4.80<7.26
- st00806 维持现图 below_spec_confirmed：无站名命中且最高 6.80<7.96
- st00809 维持现图 below_spec_confirmed：命中 太平 但最高 6.80<7.37
- st01963 维持现图 below_spec_confirmed：时钟特写 2.41<7.57
- st01970 维持现图 below_spec_confirmed：候选为名古屋巴士/神户(异县)且最高 2.04<7.57
- st01984 维持现图 below_spec_confirmed：2.41<7.47
- st03395 维持现图 below_spec_confirmed：无站名命中且最高 5.80<7.47
- st03974 维持现图 below_spec_confirmed：命中 札弦 但最高 5.04<7.32
- st04256 维持现图 below_spec_confirmed：命中 幌向 但最高 5.80<7.59
- st04265 维持现图 below_spec_confirmed：无站名命中且最高 5.80<7.99
- st04287 维持现图 below_spec_confirmed：命中 天塩中川 但最高 5.80<7.43
- st04303 维持现图 below_spec_confirmed：候选2 香川高徳琴平線塩谷同名异线拒；最高 4.80<7.29
- st04309 维持现图 below_spec_confirmed：命中 渡島沼尻 但最高 7.12<7.30
- st04800 维持现图 below_spec_confirmed：命中 狸小路 但最高 2.64<7.30
- st04822 维持现图 below_spec_confirmed：候选标题西4丁目(他站)且 2.52<7.28
- st04995 维持现图 below_spec_confirmed：命中 北18条 但最高 5.09<7.39
- st07312 维持现图 below_spec_confirmed：最高 7.12<7.30
- st07313 维持现图 below_spec_confirmed：命中 北13条東 但最高 5.09<7.52
- st07314 维持现图 below_spec_confirmed：最高 7.09<7.46
- st08653 维持现图 below_spec_confirmed：命中 北永山 但最高 5.80<7.36
- runner 42178076053 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 25。


## ws17 P0 revert st02732 — 2026-11-06T07:30:31Z
- st02732 高砂(兵庫・山陽電鉄) 撤除误挂照 File:JR Hakodate-Main-Line Takasago Station building (South Exit).jpg（站房 JR logo+「高砂駅」=JR 北海道函館本線高砂）；
- 与 st02733(北海道) 同 sha256 116ae593（B14 verify 批内 dup 闸门拦截暴露）；
- st02733 现图正确保留；st02732 置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 below-spec replace WS17-B14 — 2026-11-06T07:41:57Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"same_as_current": 25, "license_unclear": 31, "resolution_low_lt_1600": 87, "title_names_other_station": 40, "title_non_station_scene": 32, "resolution_not_upgrade": 17, "mime_unsupported": 44, "oversize_gt_25mb": 4, "no_author_metadata": 3, "hard_excluded": 10, "quality_reject_low_color": 17, "duplicate_title": 2, "license_forbidden": 3}


## ws17 local accept B14 — 2026-11-06T07:45:00Z
- st08662 维持现图 below_spec_confirmed：命中 佐久 但最高 6.80<7.99
- st04304 维持现图 below_spec_confirmed：命中 然別 但最高 6.80<8.02
- st04314 维持现图 below_spec_confirmed：命中 札苅 但最高 6.80<8.03
- st00767 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.07
- st07587 维持现图 below_spec_confirmed：命中 北舟岡 但最高 6.80<8.08
- st00757 维持现图 below_spec_confirmed：命中 白石 但最高 5.80<8.14
- st01978 维持现图 below_spec_confirmed：命中 十字街 但最高 4.04<8.19
- st08660 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.22
- st04281 维持现图 below_spec_confirmed：命中 峰延 但最高 7.80<8.28
- st05403 维持现图 below_spec_confirmed：无站名命中且最高 7.54<8.28
- st08387 维持现图 below_spec_confirmed：命中 安平 但最高 6.80<8.31
- st04325 维持现图 below_spec_confirmed：命中 黒松内 但最高 6.80<8.32
- st04327 维持现图 below_spec_confirmed：最高 6.80<8.46（候选3 贝壳标本非站景拒）
- st03945 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.50
- st04251 维持现图 below_spec_confirmed：命中 東久根別 但最高 6.80<8.55
- st02733 维持现图 below_spec_confirmed：命中 高砂 但最高 4.80<8.55（候选3 木曽古画非站景拒）
- st08390 维持现图 below_spec_confirmed：最高 6.80<8.55（候选2 上麻生他站拒）
- st08655 维持现图 below_spec_confirmed：最高 7.24<8.62
- st00771 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.68
- st04277 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.70
- st08649 维持现图 below_spec_confirmed：最高 6.80<8.70（候选3 NDL 古画非站景拒）
- st08654 维持现图 below_spec_confirmed：最高 7.21<8.70
- st05001 维持现图 below_spec_confirmed：最高 5.09<8.71（候选3 神奈川南線中之島同名异线拒）
- st04317 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.72
- st00769 维持现图 below_spec_confirmed：命中 恵み野 但最高 3.71<8.75
- runner 42181502394 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 25。


## ws17 below-spec replace WS17-B15 — 2026-11-06T07:57:33Z
- queue: 21 站（review/below_spec 高分替换）
- replaced=1 staged=20 confirmed=0 skipped=0
- reject_dist={"same_as_current": 21, "license_unclear": 20, "resolution_low_lt_1600": 46, "mime_unsupported": 67, "title_names_other_station": 20, "quality_reject_low_color": 26, "hard_excluded": 19, "title_non_station_scene": 23, "resolution_not_upgrade": 7, "duplicate_title": 1, "no_author_metadata": 1}


## ws17 revert B15 st04264 — 2026-11-06T08:02:39Z
- runner 31b553ef 自动替换 st04264 深川 为 File:Fukagawa station North square 20120903.jpg（砾石停车场+远景高架，无站名标识/无站房主体）→ 站证不成立，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 local accept B15 — 2026-11-06T08:04:17Z
- st08393 维持现图 below_spec_confirmed：命中 栗丘 但最高 5.02<8.78（候选2 神社非站景拒）
- st00815 维持现图 below_spec_confirmed：无站名命中且最高 7.09<8.84
- st03396 维持现图 below_spec_confirmed：命中 西神楽 但最高 6.80<8.85
- st01966 维持现图 below_spec_confirmed：命中 五稜郭公園前 但最高 5.04<8.87（防風板/案内板特写）
- st01967 维持现图 below_spec_confirmed：命中 中央病院前 但最高 2.80<8.89（停留所上屋特写）
- st03969 维持现图 below_spec_confirmed：命中 浜小清水 但最高 4.80<8.89
- st04266 维持现图 below_spec_confirmed：无站名命中且最高 6.80<8.91
- st00754 维持现图 below_spec_confirmed：命中 琴似 但最高 5.09<8.96
- st04250 维持现图 below_spec_confirmed：无站名命中且最高 6.02<8.98
- st00727 维持现图 below_spec_confirmed：无站名命中且最高 6.24<9.00
- st00783 维持现图 below_spec_confirmed：命中 伊達紋別 但最高 2.52<9.12
- st00756 维持现图 below_spec_confirmed：无站名命中且最高 6.80<9.19
- st01980 维持现图 below_spec_confirmed：无站名命中且最高 4.80<9.19
- st04278 维持现图 below_spec_confirmed：无站名命中且最高 6.80<9.18
- st01973 维持现图 below_spec_confirmed：命中 松風町 但最高 5.50<9.18
- st04324 维持现图 below_spec_confirmed：无站名命中且最高 6.80<9.26
- st04310 维持现图 below_spec_confirmed：无站名命中且最高 6.80<9.28
- st04288 维持现图 below_spec_confirmed：命中 幌延 但最高 6.80<9.35（候选1 掲示板特写）
- st01938 维持现图 below_spec_confirmed：候选长边 1800<现图 2048 缩边拒（且最高 6.80 无分差优势）
- st01981 维持现图 below_spec_confirmed：命中 湯の川温泉 但最高 3.03<9.64（候选为酒店照）
- runner 42183176167 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 20。


## ws17 below-spec replace WS17-B16 — 2026-11-06T08:19:41Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=2 staged=19 confirmed=4 skipped=0
- reject_dist={"same_as_current": 25, "resolution_low_lt_1600": 100, "title_names_other_station": 61, "quality_reject_low_color": 23, "duplicate_title": 6, "resolution_not_upgrade": 19, "license_unclear": 2, "hard_excluded": 28, "mime_unsupported": 75, "title_non_station_scene": 4, "no_author_metadata": 3}


## ws17 revert B16 st02689+st01299 — 2026-11-06T08:27:11Z
- runner 7d701c8b 自动替换 st02689 魚崎（高架通道+「阪神電車のりば 出口」吊牌，无站名）与 st01299 西宮（出口案内牌+巴士案内板主体，无站名牌）→ 站证不成立，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 local accept B16 — 2026-11-06T08:28:38Z
- st01057 维持现图 below_spec_confirmed：无站名命中且 5.04<5.40
- st01270 维持现图 below_spec_confirmed：命中 西宮名塩 但 5.93<6.36
- st01300 维持现图 below_spec_confirmed：候选为 JR 西宮站体 vs 记录阪神系，运营商不符拒；且 3.52<7.29
- st02730 维持现图 below_spec_confirmed：候选为 JR 223 系车照且 3.19<7.29
- st03232 维持现图 below_spec_confirmed：河流照非站景 3.09<6.74
- st03261 维持现图 below_spec_confirmed：无站名命中且最高 4.58<6.73
- st03669 维持现图 below_spec_confirmed：无站名命中且最高 6.50<6.95
- st03673 维持现图 below_spec_confirmed：无站名命中且 2.56<7.03
- st03676 维持现图 below_spec_confirmed：命中 英賀保 但最高 5.36<6.93
- st04924 维持现图 below_spec_confirmed：命中 春日野道 但最高 3.52<7.06
- st05045 维持现图 below_spec_confirmed：命中 甘地 但最高 4.75<6.56
- st05191 维持现图 below_spec_confirmed：命中 天和 但最高 5.66<7.24
- st05435 维持现图 below_spec_confirmed：候选为芬兰 Rautjärvi 风景(异国)拒；且 3.26<6.75
- st06083 维持现图 below_spec_confirmed：命中 山陽天満 但最高 3.89<7.14
- st06239 维持现图 below_spec_confirmed：命中 神野 但最高 5.41<6.86
- st06244 维持现图 below_spec_confirmed：命中 黒田庄 但最高 4.30<7.27
- st06337 维持现图 below_spec_confirmed：候选为 JR/阪神三宮站房景 vs 记录ポートライナー，运营商不符拒；主体公园/街景
- st07322 维持现图 below_spec_confirmed：券売機/改札口特写 3.52<7.25
- st08107 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.06
- runner 42185727578 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 19。


## ws17 below-spec replace WS17-B17 — 2026-11-06T08:47:37Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"resolution_not_upgrade": 47, "resolution_low_lt_1600": 74, "same_as_current": 25, "hard_excluded": 112, "title_names_other_station": 67, "title_non_station_scene": 22, "mime_unsupported": 14, "quality_reject_low_color": 19, "duplicate_title": 13, "no_author_metadata": 5, "license_unclear": 2, "license_forbidden": 1}


## ws17 local accept B17 — 2026-11-06T08:52:48Z
- st01304 维持现图 below_spec_confirmed：车照 3.25<7.30
- st05050 维持现图 below_spec_confirmed：命中 野里 但最高 4.75<7.31
- st07319 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.34
- st08412 维持现图 below_spec_confirmed：命中 王子公園 但最高 4.52<7.35
- st06633 维持现图 below_spec_confirmed：命中 みなと元町 但最高 4.50<7.36
- st01197 维持现图 below_spec_confirmed：最高 4.58<7.37（候选3 京都木津同名异线拒）
- st02724 维持现图 below_spec_confirmed：命中 西新町 但最高 5.88<7.43
- st04704 维持现图 below_spec_confirmed：候选熊本桑水异县/废线迹非站景拒；最高 3.52<7.44
- st08143 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.45
- st05107 维持现图 below_spec_confirmed：出口案内特写 3.52<7.46
- st07318 维持现图 below_spec_confirmed：无站名命中且最高 6.50<7.46
- st03256 维持现图 below_spec_confirmed：无站名命中且最高 5.50<7.47
- st02687 维持现图 below_spec_confirmed：无站名命中且最高 4.03<7.48
- st05098 维持现图 below_spec_confirmed：无站名命中且最高 6.93<7.48
- st06630 维持现图 below_spec_confirmed：命中 御崎公園 但最高 5.50<7.48
- st01298 维持现图 below_spec_confirmed：命中 甲子園口 但最高 5.52<7.49
- st08860 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.49
- st00470 维持现图 below_spec_confirmed：命中 住吉 但最高 3.52<7.50
- st00708 维持现图 below_spec_confirmed：命中 山本 但最高 4.52<7.50
- st08409 维持现图 below_spec_confirmed：命中 園田 但最高 6.52<7.53
- st04166 维持现图 below_spec_confirmed：命中 西相生 但最高 5.78<7.55
- st03670 维持现图 below_spec_confirmed：候选大阪豊中/阪急曽根同名异线拒；最高 3.00<7.56
- st05102 维持现图 below_spec_confirmed：命中 鼓滝 但最高 6.52<7.56
- st08859 维持现图 below_spec_confirmed：命中 南公園 但最高 3.52<7.56
- st02713 维持现图 below_spec_confirmed：无站名命中且最高 3.52<7.60
- runner 42189100752 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 25。


## ws17 below-spec replace WS17-B18 — 2026-11-06T09:04:12Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=0 staged=24 confirmed=0 skipped=0
- reject_dist={"same_as_current": 24, "title_names_other_station": 68, "resolution_low_lt_1600": 37, "resolution_not_upgrade": 59, "title_non_station_scene": 22, "hard_excluded": 112, "quality_reject_low_color": 23, "mime_unsupported": 16, "duplicate_title": 7, "no_author_metadata": 6, "license_unclear": 1}


## ws17 local accept B18 — 2026-11-06T09:07:22Z
- st06251 维持现图 below_spec_confirmed：最高 5.66<7.60（候选3 车照拒）
- st08108 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.62
- st08058 维持现图 below_spec_confirmed：无站名命中且最高 7.13<7.64
- st05106 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.69
- st03675 维持现图 below_spec_confirmed：命中 手柄山平和公園 但最高 3.54<7.70
- st01293 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.71
- st01303 维持现图 below_spec_confirmed：命中 芦屋 但最高 4.52<7.72
- st04703 维持现图 below_spec_confirmed：无站名命中且最高 6.58<7.72
- st08146 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.74
- st04919 维持现图 below_spec_confirmed：命中 石屋川 但最高 5.52<7.75
- st07321 维持现图 below_spec_confirmed：命中 市民広場 但最高 4.26<7.78
- st01561 维持现图 below_spec_confirmed：无站名命中且最高 3.52<7.94
- st06334 维持现图 below_spec_confirmed：无站名命中且最高 4.50<8.13
- st02704 维持现图 below_spec_confirmed：命中 大開 但最高 5.52<8.16
- st06335 维持现图 below_spec_confirmed：命中 湊川公園 但最高 6.52<8.17
- st04922 维持现图 below_spec_confirmed：命中 西灘 但最高 6.52<8.24
- st02693 维持现图 below_spec_confirmed：无站名命中且最高 6.52<8.33
- st08057 维持现图 below_spec_confirmed：命中 アイランド北口 但最高 6.52<8.34
- st04693 维持现图 below_spec_confirmed：无站名命中且最高 6.52<8.46
- st06634 维持现图 below_spec_confirmed：命中 ハーバーランド 但最高 6.50<8.48
- st04696 维持现图 below_spec_confirmed：命中 花山 但最高 6.58<8.67
- st06740 维持现图 below_spec_confirmed：最高 5.52<8.63（候选2/3 北条古川他站拒）
- st06329 维持现图 below_spec_confirmed：无站名命中且最高 6.52<8.73
- st01557 维持现图 below_spec_confirmed：候选福岛常磐线草野同名异线拒；最高 4.59<8.38
- runner 42191034501 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 24。


## ws17 below-spec replace WS17-B19 — 2026-11-06T09:15:01Z
- queue: 4 站（review/below_spec 高分替换）
- replaced=0 staged=4 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 21, "resolution_not_upgrade": 23, "hard_excluded": 18, "same_as_current": 4, "title_non_station_scene": 1, "title_names_other_station": 34, "quality_reject_low_color": 7, "mime_unsupported": 4, "quality_reject_blurry": 1}


## ws17 local accept B19 — 2026-11-06T09:16:22Z
- st01311 维持现图 below_spec_confirmed：无站名命中且最高 7.52<8.76
- st03678 维持现图 below_spec_confirmed：无站名命中且最高 4.13<9.36
- st04169 维持现图 below_spec_confirmed：最高 4.50<9.57（候选3 长野饭田线竜野同名异线拒）
- st00507 维持现图 below_spec_confirmed：候选为三日月阵屋古建非站景拒；1.75 且现图无分
- runner 42192788960 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 4。


## ws17 below-spec replace WS17-B20 — 2026-11-06T09:28:55Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=5 staged=20 confirmed=0 skipped=0
- reject_dist={"same_as_current": 25, "hard_excluded": 35, "resolution_low_lt_1600": 117, "mime_unsupported": 54, "quality_reject_low_color": 30, "title_names_other_station": 18, "duplicate_title": 5, "no_author_metadata": 20, "resolution_not_upgrade": 13, "title_non_station_scene": 19}


## ws17 revert B20 st00973+st04398 — 2026-11-06T09:34:01Z
- runner ed3d47d0…(B20=commit ed3d47d0 前一次 runner) 自动替换 st00973 根岸（罐车/货车主体）与 st04398 新高島（荒地人行桥航拍、无站体无站名）→ 站证不成立/非站景，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 local accept B20 — 2026-11-06T09:35:54Z
- st06769 相模湖 ← File:JREast-Chuo-main-line-JC25-Sagamiko-station-platform-20220730-062444.jpg (done, score 7.33→6.21)
- st00864 维持现图 below_spec_confirmed：京急车照 2.13<6.38
- st00865 维持现图 below_spec_confirmed：巴士照 3.55<7.31
- st01380 维持现图 below_spec_confirmed：送电线/寺院非站景 4.78<5.89
- st01382 维持现图 below_spec_confirmed：最高 5.52<7.24（候选3 邮便局非站景）
- st01623 维持现图 below_spec_confirmed：最高 4.32<7.07（JA/邮便局非站景）
- st01626 维持现图 below_spec_confirmed：命中 読売ランド前 但最高 3.80<7.06
- st01627 维持现图 below_spec_confirmed：命中 生田 但最高 5.52<6.79
- st01885 维持现图 below_spec_confirmed：候选1 站台照 7.50>6.71 但站名不可见（OCR 仅车号）站证不成立拒
- st02099 维持现图 below_spec_confirmed：无站名命中且最高 6.59<6.98
- st02152 维持现图 below_spec_confirmed：最高 6.66<7.03（东武车照非本站运营商）
- st02153 维持现图 below_spec_confirmed：最高 5.08<7.01（小学/车照非站景）
- st02158 维持现图 below_spec_confirmed：最高 4.50<7.30（候选3 福岛江田同名异线拒）
- st02160 维持现图 below_spec_confirmed：无站名命中且最高 5.91<6.68
- st03091 维持现图 below_spec_confirmed：命中 長後 但最高 6.36<7.20
- st03097 维持现图 below_spec_confirmed：命中 藤沢本町 但最高 6.26<7.41
- st04394 维持现图 below_spec_confirmed：命中 妙蓮寺 但最高 3.00<6.90（候选2 寺院非站景）
- st05060 维持现图 below_spec_confirmed：候选为新潟燕三条路边站同名异线拒；3.52<7.38
- st05729 维持现图 below_spec_confirmed：无站名命中且最高 5.52<6.96
- st06748 维持现图 below_spec_confirmed：车照/无关图 3.58<7.40
- runner 42194133501 暂存候选全量 OCR(全名匹配)+逐图目检；接受 1 / 标 below_spec_confirmed 19。


## ws17 revert B20 st00973+st04398 — 2026-11-06T09:37:37Z
- runner ed3d47d0…(B20=commit ed3d47d0 前一次 runner) 自动替换 st00973 根岸（罐车/货车主体）与 st04398 新高島（荒地人行桥航拍、无站体无站名）→ 站证不成立/非站景，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 below-spec replace WS17-B21 — 2026-11-06T09:50:20Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=2 staged=19 confirmed=0 skipped=4
- reject_dist={"same_as_current": 21, "hard_excluded": 20, "resolution_low_lt_1600": 90, "mime_unsupported": 50, "quality_reject_low_color": 27, "title_names_other_station": 15, "duplicate_title": 5, "resolution_not_upgrade": 10, "no_author_metadata": 14, "title_non_station_scene": 13}


## ws17 revert B20 st00973+st04398 — 2026-11-06T09:58:11Z
- runner ed3d47d0…(B20=commit ed3d47d0 前一次 runner) 自动替换 st00973 根岸（罐车/货车主体）与 st04398 新高島（荒地人行桥航拍、无站体无站名）→ 站证不成立/非站景，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 below-spec replace WS17-B21 — 2026-11-06T10:09:12Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=24 confirmed=1 skipped=0
- reject_dist={"resolution_low_lt_1600": 132, "hard_excluded": 43, "same_as_current": 25, "resolution_not_upgrade": 23, "title_names_other_station": 30, "no_author_metadata": 12, "mime_unsupported": 48, "title_non_station_scene": 13, "quality_reject_low_color": 8, "duplicate_title": 4, "license_unclear": 6}


## ws17 local accept B21 — 2026-11-06T10:14:12Z
- st00853 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.56
- st00855 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.80
- st00857 维持现图 below_spec_confirmed：命中 京急新子安 但最高 5.50<7.42
- st01616 维持现图 below_spec_confirmed：命中 座間 但最高 4.65<7.81
- st01617 维持现图 below_spec_confirmed：无站名命中且最高 4.50<7.45
- st01624 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.60
- st01625 维持现图 below_spec_confirmed：无站名命中且最高 4.52<7.97（dist 987m）
- st02098 维持现图 below_spec_confirmed：无站名命中且最高 6.05<7.64
- st02163 维持现图 below_spec_confirmed：命中 田奈 但最高 5.24<7.45
- st03088 维持现图 below_spec_confirmed：无站名命中且最高 5.50<7.61
- st03121 维持现图 below_spec_confirmed：无站名命中且最高 5.52<7.60
- st03717 维持现图 below_spec_confirmed：无站名命中且最高 6.52<7.62
- st03830 维持现图 below_spec_confirmed：无站名命中且最高 3.91<7.53
- st03861 维持现图 below_spec_confirmed：无站名命中且最高 4.13<7.72
- st04391 维持现图 below_spec_confirmed：命中 綱島 但最高 6.09<7.82
- st04986 维持现图 below_spec_confirmed：无站名命中且最高 6.52<8.02
- st05058 维持现图 below_spec_confirmed：最高 3.91<7.67（小学/路边非站景拒）
- st05061 维持现图 below_spec_confirmed：最高 3.50<7.81（高楼/防波堤非站景、dist~700-850m）
- st05065 维持现图 below_spec_confirmed：命中 海の公園南口 但最高 2.52<7.44
- st05687 维持现图 below_spec_confirmed：商业设施/通风塔非站景 2.66<7.74
- st05692 维持现图 below_spec_confirmed：最高 4.32<7.55（候选2 长野上田电铁蒔田同名异线拒）
- st05702 维持现图 below_spec_confirmed：无站名命中且最高 5.24<7.70
- st05741 维持现图 below_spec_confirmed：无站名命中且最高 5.24<8.01
- st08866 维持现图 below_spec_confirmed：无站名命中且最高 5.52<7.63
- runner 42196827100 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 24。


## ws17 below-spec replace WS17-B22 — 2026-11-06T10:46:19Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=14 confirmed=10 skipped=0
- reject_dist={"same_as_current": 25, "resolution_low_lt_1600": 65, "title_non_station_scene": 22, "title_names_other_station": 73, "hard_excluded": 19, "duplicate_title": 3, "resolution_not_upgrade": 7, "quality_reject_low_color": 18, "mime_unsupported": 93, "no_author_metadata": 1}


## ws17 local accept B22 — 2026-11-06T10:51:29Z
- st05624 南久留米 ← File:Minami-Kurume Station building 05 JAN 2026.jpg (done, score 6.27→6.20)
- st00458 维持现图 below_spec_confirmed：候选 NDL 古画/西铁车照非站景拒（4.50>3.86 但闸门不过）
- st00663 维持现图 below_spec_confirmed：无站名命中且最高 6.52<6.53
- st02187 维持现图 below_spec_confirmed：互通口/小学非站景 2.52<5.69
- st02191 维持现图 below_spec_confirmed：候选滋贺/京都·丹后大溝异县拒；3.50<6.40
- st02222 维持现图 below_spec_confirmed：候选中国马田墟/土耳其布尔萨/特拉维夫异国拒；3.62<6.56
- st02229 维持现图 below_spec_confirmed：候选神奈川江之浦观景台异县/非站景拒；3.50<4.27
- st02236 维持现图 below_spec_confirmed：古画非站景 3.28<4.14
- st03025 维持现图 below_spec_confirmed：无站名命中且最高 4.13<6.26
- st03367 维持现图 below_spec_confirmed：候选东京池尻大桥同名异县拒；2.38<4.14
- st03488 维持现图 below_spec_confirmed：候选广岛深入山/新入院异县拒；3.58<6.35
- st03492 维持现图 below_spec_confirmed：候选爱尔兰 Leixlip/瑞典 Akalla 异国拒；4.95<6.22
- st04533 维持现图 below_spec_confirmed：无站名命中且最高 6.50<6.58
- st04837 维持现图 below_spec_confirmed：无站名命中且最高 6.13<6.43
- runner 42203866174 暂存候选全量 OCR(全名匹配)+逐图目检；接受 1 / 标 below_spec_confirmed 13。


## ws17 P1 revert gate-misuse 8 站 — 2026-11-06T10:58:07Z
- 本地裁决误用 relevance score 作分数闸（workflow 闸为 image_score）；审计 15 个历史 PICK，8 站接受后分低于接受前，违反高分替换口径，撤除：
- st01324, st02672, st05624, st05704, st06640, st06769, st06967, st08365
- 恢复各站替换前 photo/license blob 与 state/index 条目（回 review 池）；st05624 标 below_spec_confirmed(B22)；其余 7 站回池待正确闸重试。


## ws17 P0 revert st02559 — 2026-11-06T11:17:27Z
- st02559 船尾(福岡・JR後藤寺線) 撤除误挂照 File:阪堺電車「船尾」停留所.jpg（街面轨道+低站台=大阪阪堺電車；标题运营商自证）；
- 与 st02558(大阪阪堺) 同 sha256 8dc30682（B23 verify 批内 dup 闸门拦截暴露）；
- st02558 现图正确保留；st02559 置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 below-spec replace WS17-B23 — 2026-11-06T11:29:21Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=2 staged=19 confirmed=3 skipped=0
- reject_dist={"resolution_low_lt_1600": 57, "no_author_metadata": 1, "duplicate_title": 6, "title_names_other_station": 117, "same_as_current": 24, "hard_excluded": 26, "title_non_station_scene": 19, "quality_reject_low_color": 16, "mime_unsupported": 95, "license_unclear": 9, "oversize_gt_25mb": 1, "near_duplicate": 1, "resolution_not_upgrade": 5, "quality_reject_blurry": 2}


## ws17 revert B23 st00672 — 2026-11-06T11:37:44Z
- runner da0bcb53 自动替换 st00672 千鳥 为 File:View from Chidori Station (east).jpg（稻田眺望、无站体无站名）→ 站证不成立，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 local accept B23 — 2026-11-06T11:39:20Z
- st02265 金山 ← File:Fukuoka Kanayama-STA Entrance2.jpg (done, score 7.20→7.44)
- st02212 维持现图 below_spec_confirmed：isc 5.88<6.65
- st04536 维持现图 below_spec_confirmed：isc 6.45<6.69
- st01155 维持现图 below_spec_confirmed：isc 5.79<6.74
- st01191 维持现图 below_spec_confirmed：isc 5.92<6.74（候选1 意大利全景异国拒）
- st01175 维持现图 below_spec_confirmed：候选千叶幕张丰砂异县拒（isc 过闸但无本站站证）
- st02186 维持现图 below_spec_confirmed：isc 5.93<6.93
- st04827 维持现图 below_spec_confirmed：isc 6.79<6.93
- st03483 维持现图 below_spec_confirmed：isc 5.80<6.96
- st06510 维持现图 below_spec_confirmed：isc 5.98<6.96
- st06511 维持现图 below_spec_confirmed：isc 6.51<7.04（候选2 东武动物园异运营商拒）
- st02240 维持现图 below_spec_confirmed：候选台湾 TRA 车照异国拒；isc 6.94<7.05
- st03370 维持现图 below_spec_confirmed：候选大阪阪急河原町异县拒；isc 3.51<7.22
- st03371 维持现图 below_spec_confirmed：候选2 邮便局非站景拒（isc 7.86 无站证）
- st01962 维持现图 below_spec_confirmed：isc 7.33<7.38
- st03378 维持现图 below_spec_confirmed：isc 5.97<7.44
- st05659 维持现图 below_spec_confirmed：isc 7.20<7.50（候选2 墓碑非站景）
- st02190 维持现图 below_spec_confirmed：isc 7.53<7.56（神社/会馆非站景）
- st08418 维持现图 below_spec_confirmed：isc 6.52<7.16
- runner 42209382012 暂存候选全量 OCR(全名匹配)+逐图目检；接受 1 / 标 below_spec_confirmed 18。


## ws17 below-spec replace WS17-B24 — 2026-11-06T11:59:21Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=4 staged=21 confirmed=0 skipped=0
- reject_dist={"title_names_other_station": 72, "hard_excluded": 61, "resolution_low_lt_1600": 69, "title_non_station_scene": 29, "same_as_current": 25, "mime_unsupported": 43, "no_author_metadata": 3, "quality_reject_low_color": 25, "license_unclear": 1, "duplicate_title": 12, "resolution_not_upgrade": 10}


## ws17 revert B24 st04194+st06168 — 2026-11-06T12:04:47Z
- runner 50074cec 自动替换 st04194 原（马赛克壁画+站长室吊牌、无站名）与 st06168 浄心（闸口+方向案内、案内站名为他站、无「浄心」站名）→ 站证不成立，撤除；
- 恢复替换前 photo/license blob 与 state/index 条目（review 态保留）。


## ws17 local accept B24 — 2026-11-06T12:06:17Z
- st00006 维持现图 below_spec_confirmed：isc 6.85<7.93
- st00399 维持现图 below_spec_confirmed：/3 站证清晰但 isc 3.53<5.0 质量下限拒；/1 isc 5.83 无站名；/2 案内板 2.58
- st00682 维持现图 below_spec_confirmed：isc 6.88<7.65（路口/车照）
- st00690 维持现图 below_spec_confirmed：isc 7.09<7.60
- st01092 维持现图 below_spec_confirmed：isc 5.93<6.19
- st01171 维持现图 below_spec_confirmed：isc 6.41<7.71
- st02209 维持现图 below_spec_confirmed：/2 巴士站时刻表牌非地铁站拒；/3 福岛会津本郷同名异线拒；isc 6.20 仅微超
- st02244 维持现图 below_spec_confirmed：isc 6.48<7.71
- st02246 维持现图 below_spec_confirmed：isc 7.02<7.60
- st03023 维持现图 below_spec_confirmed：isc 6.74<7.65
- st03246 维持现图 below_spec_confirmed：isc 5.11<8.79
- st03372 维持现图 below_spec_confirmed：isc 6.13<8.58（候选为 SL 广场人像）
- st03384 维持现图 below_spec_confirmed：isc 7.38<8.24
- st03484 维持现图 below_spec_confirmed：isc 6.69<8.30
- st04457 维持现图 below_spec_confirmed：isc 5.85<6.57（车照）
- st04830 维持现图 below_spec_confirmed：isc 7.58<7.91（矿渣山眺望）
- st06521 维持现图 below_spec_confirmed：isc 5.79<8.23
- st06528 维持现图 below_spec_confirmed：isc 6.84<7.93
- st07753 维持现图 below_spec_confirmed：isc 3.08<4.50
- st07831 维持现图 below_spec_confirmed：isc 6.91<7.98（巴士站牌）
- st08851 维持现图 below_spec_confirmed：isc 6.02<6.24
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 21。


## ws17 below-spec replace WS17-B25 — 2026-11-06T12:19:21Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=24 confirmed=0 skipped=0
- reject_dist={"same_as_current": 24, "hard_excluded": 65, "resolution_low_lt_1600": 121, "title_names_other_station": 136, "quality_reject_low_color": 19, "no_author_metadata": 9, "duplicate_title": 8, "title_non_station_scene": 14, "mime_unsupported": 17, "resolution_not_upgrade": 13, "license_unclear": 1}


## ws17 P0 revert st01288 — 2026-11-06T12:38:07Z
- st01288 三郷(愛知・名鉄瀬戸線) 撤除误挂照 File:JR Musashino Line Misato Station Platform 2022-04-06.jpg（站牌 MY13+邻站新三郷/吉川+方向幕新松戸/武蔵浦和/府中本町=JR 東日本武蔵野線埼玉三郷，目检自证）；
- legacy batch-4 批量导入(104d4083, 2026-11-03)同名错挂，与目标坐标相距 ~350km；st01287(埼玉) 自有正确照 c900d358 不受影响；
- st01288 置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 local accept B25 — 2026-11-06T12:40:39Z
- st03083 徳重・名古屋芸大 ← File:Tokushige Nagoya Geidai sta.jpg (done, score 7.00→7.18)
- st04454 豊橋公園前 ← File:愛知県豊橋市 豊橋鉄道東田本線 豊橋公園前電停 20240812 1408 (2).jpg (done, score 7.01→7.31)
- st01096 维持现图 below_spec_confirmed：最高 isc 6.43<6.76
- st01112 维持现图 below_spec_confirmed：最高 isc 6.41<7.50
- st01803 维持现图 below_spec_confirmed：最高 isc 6.17<7.11（改札 QR 告示/无站名）
- st02213 维持现图 below_spec_confirmed：最高 isc 7.09<7.39
- st02279 维持现图 below_spec_confirmed：最高 isc 7.34<7.37
- st02357 维持现图 below_spec_confirmed：最高 isc 7.12<7.41（/3 路口街景无站名）
- st02482 维持现图 below_spec_confirmed：仅候选 isc 2.39<7.21（车照）
- st03463 维持现图 below_spec_confirmed：最高 isc 7.23<7.49（/3 巴士站牌拒）
- st03464 维持现图 below_spec_confirmed：最高 isc 6.72<7.49
- st03465 维持现图 below_spec_confirmed：最高 isc 6.20<7.35
- st03468 维持现图 below_spec_confirmed：isc 6.93<6.94（差 0.01 不过闸）
- st03774 维持现图 below_spec_confirmed：最高 isc 6.52<6.82
- st04453 维持现图 below_spec_confirmed：最高 isc 7.27<7.45
- st04759 维持现图 below_spec_confirmed：最高 isc 7.06<7.37
- st04761 维持现图 below_spec_confirmed：最高 isc 5.99<7.43
- st04775 维持现图 below_spec_confirmed：最高 isc 5.41<7.21
- st06183 维持现图 below_spec_confirmed：最高 isc 6.48<7.41
- st07759 维持现图 below_spec_confirmed：最高 isc 6.73<7.37
- st07838 维持现图 below_spec_confirmed：最高 isc 6.35<7.27（/2 车照拒）
- st07847 维持现图 below_spec_confirmed：最高 isc 6.55<6.83
- st08857 维持现图 below_spec_confirmed：最高 isc 6.89<6.98
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 2 / 标 below_spec_confirmed 21。


## ws17 P0 revert 戸田簇双站 — 2026-11-06T13:08:07Z
- st03421 戸田(山口・山陽本線)/st03422 戸田(愛知・近鉄名古屋線) 同挂 sha 4a5b274b File:JR Toda Station Platform.jpg；目检吊牌「埼京線/Saikyō Line」+方向幕 武蔵浦和・大宮・川越/池袋・新宿・大崎 = JR 東日本埼京線埼玉戸田（高架+团地背景互证）；
- legacy 同名错挂（157 基线 dup 之一），B26 verify 批内 dup 闸暴露（st03422 在批）；
- st03420(埼玉) 自有照 6722457f 不受影响；双站置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 below-spec replace WS17-B26 — 2026-11-06T13:20:45Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=1 staged=23 confirmed=0 skipped=0
- reject_dist={"resolution_not_upgrade": 9, "hard_excluded": 39, "resolution_low_lt_1600": 98, "same_as_current": 24, "title_names_other_station": 94, "mime_unsupported": 38, "quality_reject_low_color": 30, "duplicate_title": 9, "quality_reject_blurry": 1, "title_non_station_scene": 5, "license_unclear": 2, "no_author_metadata": 1}


## ws17 local accept B26 — 2026-11-06T13:25:51Z
- st00560 维持现图 below_spec_confirmed：最高 isc 8.38<8.73
- st01095 维持现图 below_spec_confirmed：最高 isc 6.82<7.97
- st01104 维持现图 below_spec_confirmed：最高 isc 7.67<7.88
- st01105 维持现图 below_spec_confirmed：最高 isc 6.78<7.86
- st01109 维持现图 below_spec_confirmed：最高 isc 6.31<7.78
- st01422 维持现图 below_spec_confirmed：最高 isc 7.47<8.32
- st01590 维持现图 below_spec_confirmed：最高 isc 7.13<8.78
- st02278 维持现图 below_spec_confirmed：最高 isc 7.37<7.71
- st02319 维持现图 below_spec_confirmed：最高 isc 7.03<8.90
- st02337 维持现图 below_spec_confirmed：最高 isc 6.35<7.72
- st02390 维持现图 below_spec_confirmed：最高 isc 7.86<9.20
- st02472 维持现图 below_spec_confirmed：最高 isc 6.00<8.13
- st02483 维持现图 below_spec_confirmed：最高 isc 6.39<7.94
- st02788 维持现图 below_spec_confirmed：最高 isc 7.18<8.18
- st03075 维持现图 below_spec_confirmed：最高 isc 7.08<8.59
- st03472 维持现图 below_spec_confirmed：最高 isc 7.21<7.55
- st04455 维持现图 below_spec_confirmed：最高 isc 7.52<7.73
- st04766 维持现图 below_spec_confirmed：最高 isc 7.59<7.96
- st04773 维持现图 below_spec_confirmed：最高 isc 6.42<7.71
- st07837 维持现图 below_spec_confirmed：最高 isc 6.89<7.98
- st07846 维持现图 below_spec_confirmed：最高 isc 7.28<7.97
- st07849 维持现图 below_spec_confirmed：最高 isc 6.69<7.73
- st07896 维持现图 below_spec_confirmed：最高 isc 6.63<8.91（候选为名铁巴士站牌拒）
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 23。


## ws17 below-spec replace WS17-B27 — 2026-11-06T13:42:10Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=20 confirmed=4 skipped=0
- reject_dist={"resolution_low_lt_1600": 96, "mime_unsupported": 131, "same_as_current": 25, "license_unclear": 3, "quality_reject_low_color": 11, "title_names_other_station": 48, "duplicate_title": 5, "hard_excluded": 14, "title_non_station_scene": 5, "resolution_not_upgrade": 11, "no_author_metadata": 3, "oversize_gt_25mb": 8}


## ws17 local accept B27 — 2026-11-06T13:56:02Z
- st02680 九条 ← File:Kyoto Kujo-STA Platform1-2.jpg (done, score 6.13→6.99)
- st06981 藤森 ← File:Fujinomori Sta. West Entrance.jpg (done, score 6.24→6.76)
- st01052 维持现图 below_spec_confirmed：最高 isc 6.17<6.33
- st01059 维持现图 below_spec_confirmed：最高 isc 5.61<5.71
- st01244 维持现图 below_spec_confirmed：最高 isc 5.94<6.21
- st01578 维持现图 below_spec_confirmed：最高 isc 3.41<9.64
- st04012 维持现图 below_spec_confirmed：isc 7.68>5.24 但候选为車塚古墳/埴轮列非站景拒
- st05070 维持现图 below_spec_confirmed：isc 7.63>6.34 但候选为影视宣传照（Red Carpet 人像）非站景拒
- st05071 维持现图 below_spec_confirmed：最高 isc 5.65<6.18
- st05905 维持现图 below_spec_confirmed：最高 isc 5.95<6.16
- st05916 维持现图 below_spec_confirmed：最高 isc 5.50<5.88
- st05920 维持现图 below_spec_confirmed：isc 7.83>6.37 但候选为嵐電モボ车照拒
- st05922 维持现图 below_spec_confirmed：isc 7.31>5.71 但候选为香港西湾河站异国拒（OCR Sai 子串误命中）
- st05925 维持现图 below_spec_confirmed：isc 6.91>4.20 但候选为网球场/神社参道非站景拒
- st05928 维持现图 below_spec_confirmed：isc 7.05>6.09 但候选为妙心寺寺院照拒
- st06160 维持现图 below_spec_confirmed：最高 isc 7.68<9.22
- st07666 维持现图 below_spec_confirmed：最高 isc 5.58<5.68
- st07757 维持现图 below_spec_confirmed：最高 isc 7.35<9.43
- st08266 维持现图 below_spec_confirmed：最高 isc 5.88<6.46
- st08666 维持现图 below_spec_confirmed：isc 6.49>6.21 但候选为缆车特写无「多宝塔」站名拒
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 2 / 标 below_spec_confirmed 18。


## ws17 below-spec replace WS17-B28 — 2026-11-06T14:16:07Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=24 confirmed=0 skipped=0
- reject_dist={"title_names_other_station": 44, "hard_excluded": 26, "resolution_low_lt_1600": 99, "same_as_current": 25, "resolution_not_upgrade": 21, "license_unclear": 8, "mime_unsupported": 52, "quality_reject_low_color": 16, "no_author_metadata": 8, "title_non_station_scene": 25, "duplicate_title": 1}


## ws17 local accept B28 — 2026-11-06T14:23:04Z
- st01066 维持现图 below_spec_confirmed：最高 isc 7.09<7.26
- st01203 维持现图 below_spec_confirmed：最高 isc 7.48<7.64
- st01239 维持现图 below_spec_confirmed：最高 isc 5.32<6.75
- st01245 维持现图 below_spec_confirmed：最高 isc 5.48<6.55
- st03376 维持现图 below_spec_confirmed：最高 isc 6.74<7.25
- st04008 维持现图 below_spec_confirmed：最高 isc 6.89<7.65
- st04009 维持现图 below_spec_confirmed：isc 6.59>6.54 但候选为香川富野荘同名异县照拒
- st04010 维持现图 below_spec_confirmed：最高 isc 6.63<7.02
- st04547 维持现图 below_spec_confirmed：isc 7.64>7.21 但候选为人名照（Hiroshi H. Miyamura）非站景拒
- st04548 维持现图 below_spec_confirmed：最高 isc 6.30<7.14
- st05912 维持现图 below_spec_confirmed：isc 8.39>6.63 但候选为車折神社芸能人奉纳栅栏/神社境内非站景拒
- st05930 维持现图 below_spec_confirmed：最高 isc 6.72<7.16
- st06078 维持现图 below_spec_confirmed：最高 isc 6.40<6.47
- st06726 维持现图 below_spec_confirmed：最高 isc 6.80<7.42
- st06727 维持现图 below_spec_confirmed：最高 isc 6.57<7.52
- st06730 维持现图 below_spec_confirmed：最高 isc 6.63<7.33
- st06731 维持现图 below_spec_confirmed：最高 isc 6.59<7.63
- st06844 维持现图 below_spec_confirmed：最高 isc 5.93<7.29
- st06845 维持现图 below_spec_confirmed：最高 isc 6.27<7.33
- st06846 维持现图 below_spec_confirmed：最高 isc 6.01<7.07
- st06854 维持现图 below_spec_confirmed：最高 isc 6.47<6.87
- st07667 维持现图 below_spec_confirmed：最高 isc 6.64<6.70
- st08261 维持现图 below_spec_confirmed：最高 isc 6.47<7.21
- st08293 维持现图 below_spec_confirmed：最高 isc 6.49<6.75
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 24。


## ws17 below-spec replace WS17-B29 — 2026-11-06T14:39:17Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=2 staged=14 confirmed=9 skipped=0
- reject_dist={"duplicate_title": 2, "hard_excluded": 48, "resolution_low_lt_1600": 79, "resolution_not_upgrade": 27, "same_as_current": 25, "oversize_gt_25mb": 1, "mime_unsupported": 156, "title_names_other_station": 65, "title_non_station_scene": 11, "quality_reject_low_color": 15, "no_author_metadata": 3, "license_unclear": 1}


## ws17 P0 revert B29 legacy 错挂四站 — 2026-11-06T14:54:35Z
- st00693 小倉(京都・近鉄) 挂北九州单轨小仓照（单轨车辆+轨道梁目检）；st04544 下天津(京都・宮福) 挂天津地铁1号线下瓦房照（中文牌目检）；st05908 嵐山(京福) 挂阪急嵐山站房照（与 st05909 同 sha，阪急目检；st05909 保留）；st07456 船岡(京都・山陰) 挂 JR 東日本東北本線船岡照（宫城 heritage 站房目检）；
- 均 legacy 批量导入错挂；四站置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 revert B29 st01446 — 2026-11-06T15:04:49Z
- runner 789afea6 自动替换 st01446 下奥井 为施工期轨道透视照：全图无「下奥井」站名（右侧蓝竖牌为施工告示「お願い/工事中中」+ANTETSU，裁切放大目检），站证不成立，撤除；
- 恢复替换前 photo/license blob（File:Shimookui Station(1) - flickr.jpg）与 state/index 条目（review 态保留）。


## ws17 local accept B29 — 2026-11-06T15:11:17Z
- st01790 维持现图 below_spec_confirmed：最高 isc 6.67<8.43
- st05121 维持现图 below_spec_confirmed：最高 isc 5.15<5.98
- st05909 维持现图 below_spec_confirmed：最高 isc 6.04<8.33（现图=阪急嵐山站房，归属正确）
- st05910 维持现图 below_spec_confirmed：最高 isc 5.48<8.28（现图=站前踏切轨道视，归属正确）
- st06196 维持现图 below_spec_confirmed：最高 isc 6.38<8.42
- st06978 维持现图 below_spec_confirmed：最高 isc 7.13<7.92
- st07685 维持现图 below_spec_confirmed：isc 6.75>5.44 但候选为 ATTC2017 乒乓球赛人名照非站景拒
- st08275 维持现图 below_spec_confirmed：最高 isc 6.56<8.07
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 8。


## ws17 below-spec replace WS17-B30 — 2026-11-06T15:27:07Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=21 confirmed=4 skipped=0
- reject_dist={"title_non_station_scene": 9, "title_names_other_station": 76, "resolution_low_lt_1600": 74, "duplicate_title": 10, "hard_excluded": 29, "same_as_current": 25, "quality_reject_low_color": 13, "resolution_not_upgrade": 5, "quality_reject_white_screenshot": 1, "mime_unsupported": 99, "no_author_metadata": 3, "license_unclear": 2}


## ws17 local accept B30 — 2026-11-06T15:38:59Z
- st01458 堀川小泉 ← File:Horikawakoizumieki.jpg (done, score 7.24→7.29)
- st01451 维持现图 below_spec_confirmed：最高 isc 6.23<6.85
- st01454 维持现图 below_spec_confirmed：isc 6.93>6.51 但候选为大広田站他站照拒
- st01461 维持现图 below_spec_confirmed：最高 isc 6.45<7.33
- st01465 维持现图 below_spec_confirmed：isc 6.35>6.13 但候选为高知とさでん交通ごめん・なかまち電停异县照拒
- st01976 维持现图 below_spec_confirmed：最高 isc 6.01<7.40
- st02800 维持现图 below_spec_confirmed：最高 isc 7.21<7.26
- st02804 维持现图 below_spec_confirmed：isc 7.36>6.17 但候选为万叶线 MLRV1006 车照拒
- st02810 维持现图 below_spec_confirmed：最高 isc 6.95<7.49
- st02816 维持现图 below_spec_confirmed：isc 7.44>7.03 但候选为旭ヶ丘站他站照拒
- st02818 维持现图 below_spec_confirmed：isc 7.44>7.30 但候选为旭ヶ丘站他站照拒
- st02822 维持现图 below_spec_confirmed：最高 isc 4.32<7.26
- st03290 维持现图 below_spec_confirmed：最高 isc 7.02<7.23
- st03641 维持现图 below_spec_confirmed：isc 8.19>6.26 但候选为邮便局/车照非站景拒
- st05120 维持现图 below_spec_confirmed：最高 isc 5.90<6.62
- st07677 维持现图 below_spec_confirmed：最高 isc 6.85<6.98
- st07700 维持现图 below_spec_confirmed：最高 isc 6.62<7.26
- st07701 维持现图 below_spec_confirmed：最高 isc 6.70<7.10
- st07705 维持现图 below_spec_confirmed：最高 isc 6.16<7.04
- st08516 维持现图 below_spec_confirmed：最高 isc 6.93<7.10
- st08521 维持现图 below_spec_confirmed：最高 isc 6.25<7.04
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 1 / 标 below_spec_confirmed 20。


## ws17 below-spec replace WS17-B31 — 2026-11-06T15:55:51Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=23 confirmed=2 skipped=0
- reject_dist={"resolution_low_lt_1600": 66, "same_as_current": 25, "mime_unsupported": 102, "hard_excluded": 20, "title_names_other_station": 68, "duplicate_title": 10, "quality_reject_low_color": 13, "no_author_metadata": 8, "resolution_not_upgrade": 12, "license_unclear": 5, "title_non_station_scene": 1}


## ws17 local accept B31 — 2026-11-06T16:02:02Z
- st00134 维持现图 below_spec_confirmed：isc 7.04>5.31 但候选为银行/交番/机车照非站景拒
- st00236 维持现图 below_spec_confirmed：最高 isc 8.19<8.59
- st01429 维持现图 below_spec_confirmed：最高 isc 7.01<7.84
- st01453 维持现图 below_spec_confirmed：最高 isc 6.00<8.04
- st01457 维持现图 below_spec_confirmed：最高 isc 6.61<8.96
- st01471 维持现图 below_spec_confirmed：最高 isc 6.25<8.83
- st03282 维持现图 below_spec_confirmed：最高 isc 7.38<7.55
- st03285 维持现图 below_spec_confirmed：最高 isc 6.45<9.07
- st03286 维持现图 below_spec_confirmed：最高 isc 5.95<8.56
- st03528 维持现图 below_spec_confirmed：isc 6.18>5.30 但候选为小学分校照非站景拒
- st03657 维持现图 below_spec_confirmed：最高 isc 6.98<7.82
- st05311 维持现图 below_spec_confirmed：最高 isc 7.15<9.19
- st05312 维持现图 below_spec_confirmed：最高 isc 6.30<8.65
- st05315 维持现图 below_spec_confirmed：isc 7.24>4.22 但候选为他站舍迹/热海 ATOS 幕拒
- st07240 维持现图 below_spec_confirmed：isc 7.98>5.32 但候选为 JR 四国高知站（高架+土电电车目检）同名异县拒
- st07691 维持现图 below_spec_confirmed：最高 isc 6.87<8.22
- st07692 维持现图 below_spec_confirmed：最高 isc 6.54<7.52
- st07708 维持现图 below_spec_confirmed：最高 isc 6.38<7.50
- st08176 维持现图 below_spec_confirmed：最高 isc 6.90<8.10
- st08398 维持现图 below_spec_confirmed：最高 isc 7.51<7.58
- st08401 维持现图 below_spec_confirmed：最高 isc 7.51<8.03
- st08403 维持现图 below_spec_confirmed：最高 isc 6.72<7.64
- st08404 维持现图 below_spec_confirmed：最高 isc 7.25<8.32
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 0 / 标 below_spec_confirmed 23。


## ws17 P0 revert st03261 — 2026-11-06T16:23:11Z
- st03261 古市(兵庫・JR東西線) 撤除误挂照 File:Platform of HRT Furuichi Station.JPG（高架 AGT+站台门=広岛新交通 Astram 古市；标题 HRT 运营商自证）；
- 与 st03262(広岛 Astram) 同 sha 23ea79e0（legacy 基线 dup），B32 verify 批内 dup 闸暴露；
- st03262 保留正确照；st03261 置 missing 回重抓队列（dead stage=mismatch_removal）。


## ws17 below-spec replace WS17-B32 — 2026-11-06T16:36:06Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=23 confirmed=2 skipped=0
- reject_dist={"resolution_low_lt_1600": 60, "resolution_not_upgrade": 22, "same_as_current": 25, "mime_unsupported": 118, "title_names_other_station": 120, "title_non_station_scene": 2, "duplicate_title": 6, "hard_excluded": 13, "quality_reject_low_color": 15, "license_forbidden": 2, "license_unclear": 3}


## ws17 local accept B32 — 2026-11-06T16:42:14Z
- st05349 新井口 ← File:Shin-Inokuchi Station 20260613.jpg (done, score 7.11→7.18)
- st00128 维持现图 below_spec_confirmed：最高 isc 5.91<6.24
- st00180 维持现图 below_spec_confirmed：最高 isc 6.53<6.80
- st03262 维持现图 below_spec_confirmed：最高 isc 6.42<6.73
- st03500 维持现图 below_spec_confirmed：isc 7.47>6.97 但候选为瑞典 Hultsfred 站异国拒
- st03530 维持现图 below_spec_confirmed：最高 isc 7.41<7.62
- st03532 维持现图 below_spec_confirmed：最高 isc 6.73<6.86
- st03533 维持现图 below_spec_confirmed：最高 isc 6.94<7.62
- st04333 维持现图 below_spec_confirmed：最高 isc 5.08<6.07
- st04334 维持现图 below_spec_confirmed：最高 isc 5.72<6.11
- st04343 维持现图 below_spec_confirmed：最高 isc 7.15<7.55
- st04344 维持现图 below_spec_confirmed：最高 isc 6.80<6.97
- st05123 维持现图 below_spec_confirmed：最高 isc 7.02<7.11
- st05127 维持现图 below_spec_confirmed：最高 isc 7.17<7.85
- st05128 维持现图 below_spec_confirmed：最高 isc 7.39<7.57
- st05131 维持现图 below_spec_confirmed：isc 7.21>6.33 但候选为三重桑名消防署/警察署非站景拒
- st05339 维持现图 below_spec_confirmed：最高 isc 7.15<7.18
- st05353 维持现图 below_spec_confirmed：最高 isc 6.54<7.05
- st05919 维持现图 below_spec_confirmed：最高 isc 6.58<6.97
- st07989 维持现图 below_spec_confirmed：最高 isc 7.20<7.35
- st08003 维持现图 below_spec_confirmed：最高 isc 6.32<6.68
- st08006 维持现图 below_spec_confirmed：最高 isc 6.79<6.99
- st08012 维持现图 below_spec_confirmed：最高 isc 7.32<7.40
- runner 42212140449 暂存候选全量 OCR(全名匹配)+逐图目检；接受 1 / 标 below_spec_confirmed 22。


## ws17 queue rebuild (audit handoff) — 2026-11-06T16:48:16Z
- low_conf_identity.json(332bc346) 677 站标记 low_conf_identity；其中 549 站 status done→review（state+index 状态位仅改此字段，photo/blob 不动）入优先重捕段；
- missing 31 站不入 ws17 队列（runner 仅吃 review），留 fetch 通道；
- 队列=优先段 A(pool∩low_conf)+余段 B，县内站数降序/县内 score 升序，25/批，B33 起。


## ws17 local accept B33 — 2026-11-06T23:48:09Z
- st01830 穴川 ← File:Kintetsu Anagawa 1.jpg (done, score 6.69→7.01)
- st02044 大学前 ← File:Ueda-dentetsu-Daigakumae-station-platform-20110907-074518.jpg (done, score 5.32→6.09)
- st00336 维持现图 below_spec_confirmed：近鉄加茂 3 候选 isc 6.80/6.98/7.07<现图 7.47；京都加茂(JR奈良線)异县混入
- st01800 维持现图 below_spec_confirmed：候选全为栃木 JR両毛線 小俣/小俣(Obata)异县，无站证；isc≤7.33<8.78
- st01822 维持现图 below_spec_confirmed：候选=長崎 島原鉄道 南島原(Minami-Shimabara)，异县；isc 6.29<8.63
- st01823 维持现图 below_spec_confirmed：候选=千葉 JR総武線 松尾等；仅 OCR「松尾」无法区分同运营商类型同名簇；isc≤8.11<9.85
- st02052 维持现图 below_spec_confirmed：候选=日野自動車製バス/セレガ/甲州街道街景，非站景；isc≤7.54（唯一>6.69 者为公路街景）
- st02120 维持现图 below_spec_confirmed：c1 栃木 大桑(東武)异县 isc4.48；c2 189系あずさ車照 5.92；均<6.63
- st02360 维持现图 below_spec_confirmed：c1 木版画非照片；c2 桜駅構内 6.22<6.38；c3 近鉄湯の山線車両 6.88>6.38 但列車主体拒
- st02439 维持现图 below_spec_confirmed：候选=広島 大崎下島御手洗，异县；isc≤6.17<8.07
- st02440 维持现图 below_spec_confirmed：同上（広島 大崎下島），异县；isc≤6.17<7.24
- st06096 维持现图 below_spec_confirmed：c1/c2 站景 isc 6.59/6.07<7.00；c3 ALPICO 車両 7.8 拒
- st06721 维持现图 below_spec_confirmed：JR東海富田(三重)正确但 isc≤7.17<9.49
- st06935 维持现图 below_spec_confirmed：c1 JR東日本岩手 柳原 异县异运营商 isc7.33<7.94；c3 愛媛 柳原 异县
- st07970 维持现图 below_spec_confirmed：dup_image 隔离（图=小海線高岩 正确，配对站 st07969 長崎西九州線 错挂待审计）；本批不改状态
- runner 42256039521 SUMMARY replaced=3/staged=22；因 dup_image 闸整批未提交，自动替换 3 站（st00255/st01222/st00447）留 B33b 重派；
- 本批 25 站剔除 dup 命中 6 站（st02802/st03037/st03126/st03294/st03318/st03649）与 st07970（复算 dup）→ 16 站进本地裁决；接受 2 / below_spec_confirmed 13 / 不入提交 1(st07970)。


## ws17 below-spec replace WS17-B33b — 2026-11-06T23:56:34Z
- queue: 3 站（review/below_spec 高分替换）
- replaced=3 staged=0 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 15, "duplicate_title": 2, "resolution_not_upgrade": 10, "same_as_current": 3, "title_names_other_station": 28, "hard_excluded": 2, "title_non_station_scene": 2}


## ws17 below-spec replace WS17-B34 — 2026-11-07T00:24:23Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=18 confirmed=6 skipped=0
- reject_dist={"resolution_low_lt_1600": 74, "duplicate_title": 13, "hard_excluded": 15, "same_as_current": 25, "quality_reject_low_color": 7, "title_names_other_station": 70, "title_non_station_scene": 8, "mime_unsupported": 117, "resolution_not_upgrade": 7, "no_author_metadata": 1}


## ws17 local accept B33 — 2026-11-07T00:31:37Z
- st02023 平田 ← File:Hirata Station (Kochi), ekisha.jpg (done, score 6.55→7.54)
- st00139 维持现图 below_spec_confirmed：候选为静岡 藤枝 高須駅跡与讃岐うどん店，异县非站景；isc≤5.71<6.88
- st02342 维持现图 below_spec_confirmed：候选全为名鉄朝倉(愛知)异县异运营商；isc≤7.95 但无本站站证（本站为高知土佐電/とさでん）
- st02995 维持现图 below_spec_confirmed：c1 高知下山駅 5.46<6.79；c2 大畑山景 4.75；c3 京都バス停 2.38（hit=下山 属巴士名）
- st03730 维持现图 below_spec_confirmed：c1 高知宝永町郵便局 6.86>6.65 但非站景
- st03731 维持现图 below_spec_confirmed：候选均为 1993 年車両照 2.47/6.06/2.72<7.05
- st03732 维持现图 below_spec_confirmed：候选 3 张站台候车照 5.71~6.34<6.91，无更优
- st03737 维持现图 below_spec_confirmed：候选 6.29<6.60
- st03748 维持现图 below_spec_confirmed：候选 6.29<6.64
- st03757 维持现图 below_spec_confirmed：候选 6.22<6.51 且为車照
- st03766 维持现图 below_spec_confirmed：c2 岩手 下船渡 7.67>5.69 —— 「舟戸」⊂「下船渡」子串误判，异县拒
- st03772 维持现图 below_spec_confirmed：c2 OCR 篠原 命中但 isc6.52<6.82（千葉佐原系异县），拒
- st03784 维持现图 below_spec_confirmed：c1 广州地铁北山 5.73；c2/c3 宮城 JR北山 6.11/6.85<6.90 异县
- st03797 维持现图 below_spec_confirmed：c1 試運転 6.73<6.88；c2 関係者乗車会 5.29；c3 3000型車照 3.1
- st04626 维持现图 below_spec_confirmed：c1/c2 高知仁井田 6.53/6.49<6.66；c3 栃木仁井田 异县
- st04635 维持现图 below_spec_confirmed：候选全为熊本 阿蘇大野郷（多ノ郷⊂阿蘇大野郷 子串风险），异县；isc≤6.21<6.88
- st06361 维持现图 below_spec_confirmed：c1 試運転 6.73>6.22 但車照主体；c2 5.29；c3 車照 3.1
- st06942 维持现图 below_spec_confirmed：候选 185系車照 2.61<6.40
- runner 42256039521 SUMMARY replaced=3/staged=22；因 dup_image 闸整批未提交，自动替换 3 站（st00255/st01222/st00447）留 B33b 重派；
- 本批 25 站剔除 dup 命中 6 站（st02802/st03037/st03126/st03294/st03318/st03649）与 st07970（复算 dup）→ 16 站进本地裁决；接受 2 / below_spec_confirmed 13 / 不入提交 1(st07970)。


## ws17 local accept WS17-B34 — 2026-11-07T00:31:37Z
- st02023 平田 ← File:Hirata Station (Kochi), ekisha.jpg (done, score 7.54→7.54)
- st00139 维持现图 below_spec_confirmed：候选为静岡 藤枝 高須駅跡与讃岐うどん店，异县非站景；isc≤5.71<6.88
- st02342 维持现图 below_spec_confirmed：候选全为名鉄朝倉(愛知)异县异运营商；isc≤7.95 但无本站站证（本站为高知土佐電/とさでん）
- st02995 维持现图 below_spec_confirmed：c1 高知下山駅 5.46<6.79；c2 大畑山景 4.75；c3 京都バス停 2.38（hit=下山 属巴士名）
- st03730 维持现图 below_spec_confirmed：c1 高知宝永町郵便局 6.86>6.65 但非站景
- st03731 维持现图 below_spec_confirmed：候选均为 1993 年車両照 2.47/6.06/2.72<7.05
- st03732 维持现图 below_spec_confirmed：候选 3 张站台候车照 5.71~6.34<6.91，无更优
- st03737 维持现图 below_spec_confirmed：候选 6.29<6.60
- st03748 维持现图 below_spec_confirmed：候选 6.29<6.64
- st03757 维持现图 below_spec_confirmed：候选 6.22<6.51 且为車照
- st03766 维持现图 below_spec_confirmed：c2 岩手 下船渡 7.67>5.69 —— 「舟戸」⊂「下船渡」子串误判，异县拒
- st03772 维持现图 below_spec_confirmed：c2 OCR 篠原 命中但 isc6.52<6.82（千葉佐原系异县），拒
- st03784 维持现图 below_spec_confirmed：c1 广州地铁北山 5.73；c2/c3 宮城 JR北山 6.11/6.85<6.90 异县
- st03797 维持现图 below_spec_confirmed：c1 試運転 6.73<6.88；c2 関係者乗車会 5.29；c3 3000型車照 3.1
- st04626 维持现图 below_spec_confirmed：c1/c2 高知仁井田 6.53/6.49<6.66；c3 栃木仁井田 异县
- st04635 维持现图 below_spec_confirmed：候选全为熊本 阿蘇大野郷（多ノ郷⊂阿蘇大野郷 子串风险），异县；isc≤6.21<6.88
- st06361 维持现图 below_spec_confirmed：c1 試運転 6.73>6.22 但車照主体；c2 5.29；c3 車照 3.1
- st06942 维持现图 below_spec_confirmed：候选 185系車照 2.61<6.40
- runner run 42316923596 success：replaced=1(st03781 伊野 站内售票处，GPS/标题站证，目检通过) / confirmed=6 / staged=18；verify 0 拦截 → 提交 73b2dca9
- 18 站暂存裁决：接受 1(st02023) / below_spec_confirmed 17
- 6 站 runner 直接 confirmed：st03112/st02991/st04648/st03736/st03763/st03777


## ws17 below-spec replace WS17-B35 — 2026-11-07T00:45:19Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=16 confirmed=8 skipped=0
- reject_dist={"same_as_current": 25, "title_names_other_station": 117, "quality_reject_low_color": 25, "resolution_low_lt_1600": 77, "mime_unsupported": 196, "resolution_not_upgrade": 14, "hard_excluded": 12, "title_non_station_scene": 10, "no_author_metadata": 8, "duplicate_title": 2, "oversize_gt_25mb": 9, "license_unclear": 1}


## ws17 local accept WS17-B35 — 2026-11-07T00:47:41Z
- st01757 维持现图 below_spec_confirmed：候选全为浅间列车照（大宮/长野 異県），车照主体；isc≤5.59<6.53
- st01780 维持现图 below_spec_confirmed：候选为近鉄列車照（伊勢中川/名阪），isc≤5.57<6.63 且车照主体
- st01799 维持现图 below_spec_confirmed：c1/c2 德国 Lütticher Straße 里程碑照；c3 同类 7.16>6.23 但非站景
- st01810 维持现图 below_spec_confirmed：c1/c3 均为近鉄列車照（Local Tsushinmachi）；c3 7.38>6.85 但车照主体
- st05094 维持现图 below_spec_confirmed：c1/c2 爱沙尼亚转车盘、c3 予讃線轨道照，非站景/异线
- st06110 维持现图 below_spec_confirmed：c1 Nanawa-station 5.63<5.69
- st06111 维持现图 below_spec_confirmed：c3 277系車照 8.12>6.54 但车照主体；c1 5.89<6.54
- st06807 维持现图 below_spec_confirmed：c1 豊橋中瀬古町公民館 7.28>5.43 非站景
- st08296 维持现图 below_spec_confirmed：c2/c3 2444系車照 7.65~7.71>6.00 车照主体；c1 5.94<6.00
- st08297 维持现图 below_spec_confirmed：c3 三峰山景 7.08>6.31 非站景；c1/c2 神社石碑
- st08298 维持现图 below_spec_confirmed：c1 四日市西警察署 7.96>5.64 非站景；c2/c3 車照
- st08299 维持现图 below_spec_confirmed：c1~c3 全为 2444系車照 7.65~8.24>6.60 车照主体
- st08301 维持现图 below_spec_confirmed：c1/c2/c3 isc≤5.25<5.78
- st08508 维持现图 below_spec_confirmed：c1/c2/c3 广州黄边站，异県
- st08696 维持现图 below_spec_confirmed：c2 军事演习照 6.58>4.47 非站景；c1 3.16<4.47
- st08705 维持现图 below_spec_confirmed：c1/c3 大阪 Metro ドーム前千代崎（千代崎⊂ドーム前千代崎 同名子串）；c2 車照 5.63<6.69
- runner run 42319052528 success：replaced=1 st08295 伊勢松本（站房全景，站名牌「伊勢松本駅」可读，目检通过，1800×~545 超宽条幅记异常）/ confirmed=8 / staged=44(16 站)
- 16 站暂存裁决：0 接受 / 16 below_spec_confirmed（候选全为车照、异県同名、非站景）
- 8 站 runner 直接 confirmed：st00107/st05092/st05088/st01827/st01782/st08415/st05091/st08345


## ws17 below-spec replace WS17-B36 — 2026-11-07T00:59:00Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=22 confirmed=3 skipped=0
- reject_dist={"same_as_current": 25, "mime_unsupported": 90, "title_names_other_station": 29, "resolution_low_lt_1600": 69, "license_unclear": 5, "hard_excluded": 10, "title_non_station_scene": 6, "quality_reject_low_color": 12, "resolution_not_upgrade": 14, "no_author_metadata": 2, "duplicate_title": 2}


## ws17 local accept WS17-B36 — 2026-11-07T01:01:05Z
- st02453 维持现图 below_spec_confirmed：候选最高 isc 7.10<8.25
- st02502 维持现图 below_spec_confirmed：候选最高 isc 5.60<8.26
- st02533 维持现图 below_spec_confirmed：候选最高 isc 7.13<8.45（OCR 西条 命中但分数不及）
- st02540 维持现图 below_spec_confirmed：候选最高 isc 6.60<7.17
- st02543 维持现图 below_spec_confirmed：候选最高 isc 7.22<7.81
- st02765 维持现图 below_spec_confirmed：候选最高 isc 6.38<6.96（十二兼 命中但不及）
- st03037 维持现图 below_spec_confirmed：候选最高 isc 6.75<7.82（城下 命中但不及）
- st05416 维持现图 below_spec_confirmed：候选最高 isc 6.80<6.85
- st05597 维持现图 below_spec_confirmed：候选最高 isc 6.81<8.20
- st06087 维持现图 below_spec_confirmed：候选最高 isc 4.61<4.78
- st06090 维持现图 below_spec_confirmed：候选最高 isc 6.71<7.21（三溝 命中但不及）
- st06098 维持现图 below_spec_confirmed：候选最高 isc 6.58<6.75（西松本 命中但不及）
- st06319 维持现图 below_spec_confirmed：候选最高 isc 7.28<8.18
- st06947 维持现图 below_spec_confirmed：候选最高 isc 7.32<7.54
- st08489 维持现图 below_spec_confirmed：候选最高 isc 7.13<8.22
- st08678 维持现图 below_spec_confirmed：候选最高 isc 7.44<8.48
- st08682 维持现图 below_spec_confirmed：候选最高 isc 7.02<8.12（権堂 命中但不及）
- st02519 维持现图 below_spec_confirmed：c2 7.26>6.03 但图为印度 Balligavi 古迹；c1 4.95<6.03
- st02524 维持现图 below_spec_confirmed：c1 Kiriishi tunnel 6.22>3.24 但为隧道照非站景
- st02775 维持现图 below_spec_confirmed：c3 7.01>6.77 但为歌川广重木版画 NDL，非照片
- st08674 维持现图 below_spec_confirmed：c1 8.30>3.14 但为「中野松川郵便局」照，非站景
- st08676 维持现图 below_spec_confirmed：c1 7.53>7.02「Yomase Goso」无站名/站景证据
- runner run 42320502622 success：replaced=0 / confirmed=3(st08672/st02770/st08670) / staged=57(22 站)
- 22 站暂存裁决：0 接受 / 22 below_spec_confirmed（候选最高分普遍<现图，或过闸但为邮局/隧道/古迹/木版画）


## ws17 below-spec replace WS17-B37 — 2026-11-07T01:13:56Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=3 staged=22 confirmed=0 skipped=0
- reject_dist={"same_as_current": 23, "title_names_other_station": 164, "title_non_station_scene": 19, "hard_excluded": 77, "resolution_low_lt_1600": 88, "mime_unsupported": 50, "duplicate_title": 22, "no_author_metadata": 14, "quality_reject_low_color": 10, "resolution_not_upgrade": 41}


## ws17 local accept WS17-B37 — 2026-11-07T03:20:52Z
- st02751 大阪梅田 ← File:Hanshin-Osaka-Umeda-STA Department-store-gate.jpg (done, score 6.45→7.57)
- st05242 南方 ← File:Hankyu Minamikata-STA South-West-Entrance.jpg (done, score 4.52→6.94)
- st00070 维持现图 below_spec_confirmed：野田：唯一过数值闸候选为大和路快速车照，无站证
- st00112 维持现图 below_spec_confirmed：最高候选分 6.32<6.54，且为駅前通り/方向牌
- st00425 维持现图 below_spec_confirmed：貝塚最高 7.35<7.36，无更优
- st00886 维持现图 below_spec_confirmed：日本橋最高 7.51<7.53
- st01021 维持现图 below_spec_confirmed：滝谷最高 6.98<7.57
- st01098 维持现图 below_spec_confirmed：最高 6.20<6.83
- st01119 维持现图 below_spec_confirmed：京橋最高 6.19<7.60
- st01275 维持现图 below_spec_confirmed：平野最高 6.15<7.36
- st01280 维持现图 below_spec_confirmed：柏原：7.15 候选为街景车辆；站内候选中无「柏原」站名
- st01324 维持现图 below_spec_confirmed：最高 6.44<6.58
- st02659 维持现图 below_spec_confirmed：箪山最高 6.73<7.86
- st02672 维持现图 below_spec_confirmed：河内花園：7.24 候选为関西みらい銀行，非站景；其余 6.23/6.17<6.53
- st03235 维持现图 below_spec_confirmed：吹田最高 6.78<7.23
- st04559 维持现图 below_spec_confirmed：西最高 6.88<7.10
- st04874 维持现图 below_spec_confirmed：最高 6.39<7.21
- st05648 维持现图 below_spec_confirmed：庄内最高 6.61<7.65
- st05704 维持现图 below_spec_confirmed：文の里 6.46<6.54
- st06640 维持现图 below_spec_confirmed：岸里：7.39 候选为「汐見橋-岸里玉出」车头方向幕（南海），非岸里站
- st06967 维持现图 below_spec_confirmed：千林最高 6.37<6.51
- st08365 维持现图 below_spec_confirmed：新深江最高 6.32<6.58
- B37 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 f063c2cc）
- B37 runner replaced=3（st01947/st01948/st05374）；staged=65 条覆盖 22 站


## ws17 below-spec replace WS17-B38 — 2026-11-07T03:35:11Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=24 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 86, "title_names_other_station": 26, "same_as_current": 25, "hard_excluded": 40, "resolution_not_upgrade": 43, "quality_reject_low_color": 6, "mime_unsupported": 5, "title_non_station_scene": 5, "duplicate_title": 20, "no_author_metadata": 2}


## ws17 local accept WS17-B38 — 2026-11-07T03:42:39Z
- st00162 维持现图 below_spec_confirmed：市役所前：最高 6.77<8.20
- st00536 维持现图 below_spec_confirmed：大原：站名命中但最高 7.70<7.97
- st00718 维持现图 below_spec_confirmed：大町：最高 6.90<7.91
- st00937 维持现图 below_spec_confirmed：勝田台：最高 6.57<6.58
- st00938 维持现图 below_spec_confirmed：京成大和田：最高 6.37<7.41
- st01082 维持现图 below_spec_confirmed：柏たなか：最高 6.32<7.92
- st01723 维持现图 below_spec_confirmed：井野：最高 6.34<8.11
- st01831 维持现图 below_spec_confirmed：穴川：站名命中但竖幅 3.63<7.65
- st02667 维持现图 below_spec_confirmed：学園前：最高 7.18<7.75
- st03690 维持现图 below_spec_confirmed：京成西船：最高 5.81<8.17
- st03703 维持现图 below_spec_confirmed：京成酒々井：最高 6.61<8.12
- st03714 维持现图 below_spec_confirmed：新千葉：站名命中但竖幅 3.58<8.27
- st03721 维持现图 below_spec_confirmed：大森台：最高 7.53<7.84
- st05160 维持现图 below_spec_confirmed：鎌取：最高 6.43<7.98
- st05461 维持现图 below_spec_confirmed：東船橋：最高 7.33<7.64
- st05482 维持现图 below_spec_confirmed：下総中山：最高 6.42<7.37
- st07090 维持现图 below_spec_confirmed：鵜原：站名命中但最高 7.65<8.35
- st07750 维持现图 below_spec_confirmed：東京ディズニーランド・ステーション：7.84 过数值闸，画面为站房但无站名文字，按站名可见闸门拒
- st07752 维持现图 below_spec_confirmed：東京ディズニーシー・ステーション：最高 6.34<6.96
- st08560 维持现图 below_spec_confirmed：新柏：站名命中但最高 6.76<7.39
- st08561 维持现图 below_spec_confirmed：豊四季：最高 6.81<6.86
- st08568 维持现图 below_spec_confirmed：七光台：最高 6.79<7.82
- st08579 维持现图 below_spec_confirmed：六実：站名命中但 7.12<7.25
- st08758 维持现图 below_spec_confirmed：海士有木：站名命中但最高 6.74<8.10
- B38 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 efc825db）
- B38 runner replaced=1（st00945 東中山）；staged=72 条覆盖 24 站


## ws17 below-spec replace WS17-B39 — 2026-11-07T03:56:02Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=21 confirmed=3 skipped=0
- reject_dist={"mime_unsupported": 110, "resolution_low_lt_1600": 73, "title_names_other_station": 60, "duplicate_title": 8, "same_as_current": 25, "hard_excluded": 26, "resolution_not_upgrade": 15, "quality_reject_low_color": 20, "license_unclear": 2, "license_forbidden": 6, "no_author_metadata": 2}


## ws17 local accept WS17-B39 — 2026-11-07T04:03:26Z
- st02681 九条 ← File:Kintetsu Kujo Station east entrance.jpg (done, score 6.13→6.86)
- st07191 新王寺 ← File:Shin-Ōji Station 202608.jpg (done, score 6.32→6.59)
- st00055 维持现图 below_spec_confirmed：桜井：候选长边 1800<现图 2048，尺寸闸不过
- st00064 维持现图 below_spec_confirmed：帯解：最高 6.19，无站名站证
- st01232 维持现图 below_spec_confirmed：郡山：候选长边 1800<现图 2048
- st01761 维持现图 below_spec_confirmed：五位堂：最高 5.51<6.72
- st01785 维持现图 below_spec_confirmed：長谷寺：最高 6.09<6.12
- st01786 维持现图 below_spec_confirmed：大和朝倉：最高 5.85<6.11
- st02669 维持现图 below_spec_confirmed：菖蒲池：7.39/7.30 为彩虹湖景，非站景
- st02670 维持现图 below_spec_confirmed：新大宮：6.49>5.97 但画面为公路跨线桥，无站名
- st02696 维持现图 below_spec_confirmed：平端：最高 6.44<6.51
- st02697 维持现图 below_spec_confirmed：二階堂：7.53 为粉色花丛，非站景
- st03462 维持现图 below_spec_confirmed：白庭台：8.06/7.07 为バーミヤン餐饮店，非站景
- st03841 维持现图 below_spec_confirmed：真菅：7.14 为松塚-真菅间车照，非站景
- st03843 维持现图 below_spec_confirmed：築山：7.68 为石室古迹，非站景
- st04956 维持现图 below_spec_confirmed：葛：/1 为东武葛生駅（栃木）异站；/2 改札无站名；/3 无站证
- st04957 维持现图 below_spec_confirmed：市尾：5.88<6.78
- st04961 维持现图 below_spec_confirmed：二上山：4.14/4.00 为书籍插图页
- st05075 维持现图 below_spec_confirmed：畝傍御陵前：站名命中但最高 6.76<6.88
- st07188 维持现图 below_spec_confirmed：池部：最高 5.96<6.67
- st08539 维持现图 below_spec_confirmed：萩の台：最高 6.43，画面为街角电箱/保育园门，非站景
- B39 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 cdede37b）
- B39 runner replaced=1（st01286）；runner 自动确认 3；staged=59 条覆盖 21 站


## ws17 below-spec replace WS17-B40 — 2026-11-07T04:16:35Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=9 staged=16 confirmed=0 skipped=0
- reject_dist={"license_unclear": 7, "title_names_other_station": 59, "hard_excluded": 47, "resolution_not_upgrade": 63, "title_non_station_scene": 14, "same_as_current": 21, "duplicate_title": 20, "resolution_low_lt_1600": 90, "no_author_metadata": 4, "mime_unsupported": 14, "license_forbidden": 21, "quality_reject_low_color": 17}


## ws17 local accept WS17-B40 — 2026-11-07T04:31:22Z
- st01214 木幡 ← File:Shintetsu Kobata Station.jpg (done, score 4.91→6.80)
- st00573 维持现图 below_spec_confirmed：栄：最高 7.08<7.31
- st00704 维持现图 below_spec_confirmed：岩屋：最高 6.95<7.21
- st00878 维持现图 below_spec_confirmed：三田：候选为东京都营三田线三田駅（白金高輪/目黒/第一京浜），异县
- st01055 维持现图 below_spec_confirmed：豊岡：候选长边 1800<现图 2048，尺寸闸不过
- st01264 维持现图 below_spec_confirmed：尼崎：最高 6.50<7.38
- st01274 维持现图 below_spec_confirmed：平野：能勢電鉄平野駅名命中但最高 6.52<7.47
- st01294 维持现图 below_spec_confirmed：塚口：最高 6.72<7.47
- st01552 维持现图 below_spec_confirmed：広野：候选为 JR 広野駅（福島常磐線）站台，与兵庫記録不符
- st02691 维持现图 below_spec_confirmed：今津：最高 6.44<7.51
- st02717 维持现图 below_spec_confirmed：霞ケ丘：最高 7.35<7.46
- st04017 维持现图 below_spec_confirmed：竹田：候选为大邱/盆唐 Jukjeon（韩国），异国
- st04167 维持现图 below_spec_confirmed：相生：候选长边 1800<现图 2048
- st04923 维持现图 below_spec_confirmed：春日野道：最高 7.01<7.42
- st06249 维持现图 below_spec_confirmed：滝：/1 为 JR烏山線滝駅（栃木）异站；/2 街景；/3 民家路景
- st06336 维持现图 below_spec_confirmed：三宮：最高 4.47<5.66
- B40 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 e59785b9）
- B40 runner replaced=9；staged=48 条覆盖 16 站；本地接受 1
- P1 记档：st01302 芦屋（JR 记录）runner 替换图仍为阪神芦屋站台（前图亦为阪神），需身份裁决；st03329 横山替换图为神鉄 6514 车照（站台可见），暂留观察


## ws17 P1 revert st01302 芦屋（2026-11-07）
- st01302 芦屋（JR・東海道本線）当前图为 阪神芦屋駅2番線ホーム（同名异站，相距约1km）→ 错站，撤图置 missing；index 摘除；photo/license 待删；removed_misattached 留档；待补 JR 芦屋站景（已在 data/low_conf_identity.json）。


## ws17 below-spec replace WS17-B41r — 2026-11-07T05:15:08Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=23 confirmed=1 skipped=0
- reject_dist={"hard_excluded": 69, "duplicate_title": 25, "resolution_low_lt_1600": 142, "same_as_current": 25, "quality_reject_low_color": 10, "title_names_other_station": 91, "mime_unsupported": 43, "resolution_not_upgrade": 45, "title_non_station_scene": 10, "no_author_metadata": 24, "license_unclear": 4}


## ws17 local accept WS17-B41r — 2026-11-07T05:22:18Z
- st00187 维持现图 below_spec_confirmed：八丁堀：最高 6.64<8.81
- st00305 维持现图 below_spec_confirmed：白山：站名命中但最高 6.66<7.81
- st00877 维持现图 below_spec_confirmed：三田：最高 6.96<7.37
- st00885 维持现图 below_spec_confirmed：日本橋：最高 6.56<7.57
- st00891 维持现图 below_spec_confirmed：浅草：最高 5.95<7.22（竖幅候选 0.05 为差图）
- st00892 维持现图 below_spec_confirmed：浅草：最高 5.95<7.18
- st00925 维持现图 below_spec_confirmed：梅屋敷：最高 6.45<7.83
- st01120 维持现图 below_spec_confirmed：京橋：7.86>7.44 且长边达标，但画面仅银座线站台/线路牌，无「京橋」站名
- st01440 维持现图 below_spec_confirmed：新富町：站名命中但最高 7.54<7.88
- st01518 维持现图 below_spec_confirmed：大手町：7.19>6.87 但仅换乘线路牌（半蔵門/千代田/東西/都営三田），无「大手町」站名
- st01522 维持现图 below_spec_confirmed：霞ケ関：最高 6.96<8.19
- st01562 维持现图 below_spec_confirmed：山下：最高 7.01<7.76
- st01977 维持现图 below_spec_confirmed：末広町：站名命中但 7.02<7.53
- st02051 维持现图 below_spec_confirmed：日野：最高 6.59<6.70
- st02147 维持现图 below_spec_confirmed：入谷：最高 7.81<8.43
- st02235 维持现图 below_spec_confirmed：桜台：最高 6.55<8.46
- st03654 维持现图 below_spec_confirmed：栄町：6.66>4.52 且长边达标，但画面为丸ノ内線站台/楼梯，无「栄町」站名
- st04481 维持现图 below_spec_confirmed：両国：最高 7.40<8.62
- st04483 维持现图 below_spec_confirmed：森下：站名命中但最高 6.90<8.38
- st04516 维持现图 below_spec_confirmed：中野：最高 7.45<7.48
- st04782 维持现图 below_spec_confirmed：山田：最高 7.03<7.64
- st05486 维持现图 below_spec_confirmed：平井：站名命中 Hirai 但 6.56<7.94
- st05548 维持现图 below_spec_confirmed：長沼：最高 5.90<7.90
- B41 首次 run 42339007612 因撤回提交改 head 导致 Commit & push 非 fast-forward（state 冲突）整批未推；重派 B41r run 42341152074 success → 提交 7c1f5d35
- B41r 三查：foreign 0 / same_name_other_line 0 / dup_image 0
- B41r runner replaced=1（st02165 新宿，1800x632 超宽全景，7.57>6.80）；staged=69 条覆盖 23 站；本地 0 接受


## ws17 below-spec replace WS17-B42 — 2026-11-07T05:35:09Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"same_as_current": 25, "duplicate_title": 21, "resolution_low_lt_1600": 72, "no_author_metadata": 9, "hard_excluded": 56, "title_names_other_station": 86, "mime_unsupported": 54, "oversize_gt_25mb": 2, "license_unclear": 10, "quality_reject_low_color": 16, "resolution_not_upgrade": 14, "title_non_station_scene": 46}


## ws17 local accept WS17-B42 — 2026-11-07T05:40:52Z
- st00258 大久保 ← File:JR East Ōkubo Station building in Katagami City, Akita Pref.jpg (done, score 8.05→8.13)
- st00952 维持现图 below_spec_confirmed：余子：最高 7.09<7.29
- st00954 维持现图 below_spec_confirmed：中浜：最高 4.37<7.38
- st00955 维持现图 below_spec_confirmed：米子空港：/2 7.63>7.52 但为海上自卫队基地楼，/1 海上保安厅，无站名
- st00962 维持现图 below_spec_confirmed：富士見町：最高 6.84<8.57
- st01160 维持现图 below_spec_confirmed：市場：站名命中但最高 7.38<7.59
- st01223 维持现图 below_spec_confirmed：亀山：最高 6.85<7.62
- st01265 维持现图 below_spec_confirmed：伊丹：最高 7.30<8.40
- st01266 维持现图 below_spec_confirmed：伊丹：最高 7.30<7.61
- st01315 维持现图 below_spec_confirmed：塩屋：最高 7.83<7.99
- st01374 维持现图 below_spec_confirmed：国府：最高 7.53<8.61
- st02736 维持现图 below_spec_confirmed：別府：最高 6.97<8.13
- st02748 维持现图 below_spec_confirmed：荒井：最高 7.04<8.28
- st02753 维持现图 below_spec_confirmed：御影：最高 6.49<7.53
- st03229 维持现图 below_spec_confirmed：黒井：最高 8.09<8.14
- st03400 维持现图 below_spec_confirmed：緑が丘：站名命中但 7.00<7.74
- st03448 维持现图 below_spec_confirmed：長田：最高 6.40<8.56
- st03449 维持现图 below_spec_confirmed：長田：站名命中但 7.30<7.65
- st04138 维持现图 below_spec_confirmed：小野：最高 6.59<7.80
- st04215 维持现图 below_spec_confirmed：丸山：最高 6.39<8.51
- st05020 维持现图 below_spec_confirmed：松崎：最高 8.07<8.66
- st05024 维持现图 below_spec_confirmed：浦安：最高 7.99<8.70
- st05030 维持现图 below_spec_confirmed：御来屋：最高 6.81<7.27
- st07292 维持现图 below_spec_confirmed：岸本：/3 7.78>7.72 但为列车+大山风景，车照非站景
- st08269 维持现图 below_spec_confirmed：福部：/3 7.86>7.57 但为福部町综合支所（町役场），非站景
- B42 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 21ecfa00）
- B42 runner replaced=0、confirmed=0；staged=70 条覆盖 25 站；rejected_notable=132；本地接受 1


## ws17 P1 revert st02165 新宿（超宽全景，2026-11-07）
- runner B41r 将 st02165 新宿替换为 1800x632 全景（7.57>6.80）；按站图展示比例中心裁切后站房与「新宿駅 Shinjuku Station」大字被切，主体成街道细带 → 回退原图 1800x1200（6.80），标 below_spec_confirmed 防重复覆盖。


## ws17 below-spec replace WS17-B43 — 2026-11-07T05:56:57Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=1 staged=24 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 107, "same_as_current": 25, "license_unclear": 7, "title_non_station_scene": 6, "duplicate_title": 6, "title_names_other_station": 26, "mime_unsupported": 27, "quality_reject_low_color": 17, "hard_excluded": 35, "resolution_not_upgrade": 19, "no_author_metadata": 1}


## ws17 local accept WS17-B43 — 2026-11-07T06:32:14Z
- st01113 维持现图 below_spec_confirmed：吹上：最高 7.21<7.39
- st01287 维持现图 below_spec_confirmed：三郷：最高 6.12<7.76
- st01932 维持现图 below_spec_confirmed：川口：最高 6.62<8.50
- st02068 维持现图 below_spec_confirmed：杉戸高野台：最高 7.37<7.90
- st02069 维持现图 below_spec_confirmed：東武動物公園：最高 7.12<8.27
- st02079 维持现图 below_spec_confirmed：新越谷：最高 5.76<8.63
- st02304 维持现图 below_spec_confirmed：南桜井：最高 7.73<8.11（/3 为 1800x333 条幅）
- st02399 维持现图 below_spec_confirmed：金子：站名命中但最高 7.34<8.59
- st02589 维持现图 below_spec_confirmed：鷲宮：最高 6.66<7.90
- st03149 维持现图 below_spec_confirmed：和光市：最高 7.09<7.58
- st03420 维持现图 below_spec_confirmed：戸田：最高 7.39<7.67
- st04213 维持现图 below_spec_confirmed：沼南：站名命中但最高 6.49<7.51
- st04218 维持现图 below_spec_confirmed：伊奈中央：站名命中但最高 6.11<7.81
- st04407 维持现图 below_spec_confirmed：仏子：站名命中但最高 6.59<7.97
- st05580 维持现图 below_spec_confirmed：武州荒木：站名命中但最高 7.34<7.74
- st05581 维持现图 below_spec_confirmed：東行田：站名命中但 7.46<7.52
- st05595 维持现图 below_spec_confirmed：小前田：站名命中但最高 6.39<7.55
- st05596 维持现图 below_spec_confirmed：桜沢：最高 6.81<7.60
- st05603 维持现图 below_spec_confirmed：親鼻：最高 6.41<7.22
- st05887 维持现图 below_spec_confirmed：武州唐沢：最高 6.38<7.73
- st06119 维持现图 below_spec_confirmed：入曽：最高 6.82<7.83
- st06120 维持现图 below_spec_confirmed：新所沢：站名命中但最高 6.93<7.87
- st08313 维持现图 below_spec_confirmed：玉淀：站名命中但最高 7.57<7.68
- st08570 维持现图 below_spec_confirmed：藤の牛島：最高 7.21<7.65
- B43 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 8ce3261c）
- B43 runner replaced=1（st03369 一本松，1800x1014，score 3.32）；staged=69 条覆盖 24 站；本地 0 接受


## ws17 below-spec replace WS17-B44 — 2026-11-07T06:44:08Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=4 staged=21 confirmed=0 skipped=0
- reject_dist={"resolution_low_lt_1600": 129, "same_as_current": 25, "mime_unsupported": 47, "oversize_gt_25mb": 4, "title_non_station_scene": 15, "no_author_metadata": 9, "duplicate_title": 33, "title_names_other_station": 140, "quality_reject_low_color": 14, "resolution_not_upgrade": 40, "hard_excluded": 63, "license_unclear": 3}


## ws17 local accept WS17-B44 — 2026-11-07T07:59:31Z
- st00003 维持现图 below_spec_confirmed：高田：最高 7.49<8.50
- st00163 维持现图 below_spec_confirmed：市役所前：最高 6.80<6.96
- st00572 维持现图 below_spec_confirmed：栄：最高 6.21<7.07
- st00640 维持现图 below_spec_confirmed：東諫早：7.91>7.90 但为彩绘列车过桥车照，无站名
- st00648 维持现图 below_spec_confirmed：松原：最高 6.31<7.95
- st01097 维持现图 below_spec_confirmed：今池：站名命中但 6.47<6.49
- st01163 维持现图 below_spec_confirmed：赤池：最高 5.57<7.01
- st01452 维持现图 below_spec_confirmed：競輪場前：最高 6.23<6.45
- st02162 维持现图 below_spec_confirmed：藤が丘：站名命中但最高 6.33<7.43
- st02359 维持现图 below_spec_confirmed：桜：最高 6.40<7.70
- st02660 维持现图 below_spec_confirmed：瓢箪山：站名命中但最高 6.95<7.40
- st02782 维持现图 below_spec_confirmed：春日井：候选长边 1800<现图 2048，尺寸闸不过
- st02783 维持现图 below_spec_confirmed：春日井：7.75>7.46 但为站前时钟雕塑街景，无站名
- st02828 维持现图 below_spec_confirmed：本山：站名命中但最高 6.09<6.15
- st04132 维持现图 below_spec_confirmed：比良：最高 6.63<7.12
- st04459 维持现图 below_spec_confirmed：運動公園前：站名命中但 5.92<7.25
- st04972 维持现图 below_spec_confirmed：矢田：站名命中但最高 7.25<7.38
- st05385 维持现图 below_spec_confirmed：神代：站名命中但 7.34<8.02
- st07146 维持现图 below_spec_confirmed：山口：最高 6.92<7.26
- st07942 维持现图 below_spec_confirmed：松浦：最高 6.71<8.09
- st07969 维持现图 below_spec_confirmed：高岩：最高 7.03<7.74
- B44 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 1348523016）
- B44 runner replaced=4（st02492 豊川/st01649 黒川/st06168 浄心/st02322 山王）；staged=58 条覆盖 21 站；本地 0 接受
- P1：st02492 豊川 runner 替换图为 1800x335 条幅，按展示比例不可用 → 回退原图 2048x1357 并 bsc（另提交）


## ws17 P1 revert st02492 豊川（条幅，2026-11-07）
- runner B44 将 st02492 豊川替换为 1800x335 全景条幅（6.04）；条幅按站图展示比例不可读 → 回退原图 2048x1357（丰川駅东西自由通路站房，score 未评）并标 below_spec_confirmed。


## ws17 below-spec replace WS17-B45 — 2026-11-07T08:18:19Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=0 staged=25 confirmed=0 skipped=0
- reject_dist={"duplicate_title": 29, "license_unclear": 6, "resolution_not_upgrade": 12, "same_as_current": 25, "resolution_low_lt_1600": 134, "title_names_other_station": 50, "quality_reject_low_color": 18, "hard_excluded": 36, "no_author_metadata": 5, "title_non_station_scene": 4, "mime_unsupported": 20}


## ws17 local accept WS17-B45 — 2026-11-07T10:18:30Z
- st02314 山崎 ← File:MT-Yamazaki Station-Building 2.jpg (done, score 8.10→8.20)
- st00056 维持现图 below_spec_confirmed：桜井：最高 7.58<9.18
- st00150 维持现图 below_spec_confirmed：土橋：站名命中但最高 7.57<8.05
- st00310 维持现图 below_spec_confirmed：青山：最高 7.00<8.32
- st00781 维持现图 below_spec_confirmed：富浦：最高 7.35<9.46
- st00811 维持现图 below_spec_confirmed：新川：站名命中但最高 6.92<8.16
- st00881 维持现图 below_spec_confirmed：大門：最高 6.63<8.31
- st01090 维持现图 below_spec_confirmed：国際センター：站名命中但最高 6.22<8.44
- st01579 维持现图 below_spec_confirmed：植田：最高 7.91<8.51
- st01941 维持现图 below_spec_confirmed：平岸：最高 6.12<8.35
- st02267 维持现图 below_spec_confirmed：堀田：站名命中但 6.60<8.66
- st02268 维持现图 below_spec_confirmed：堀田：站名命中但 6.72<8.50
- st02284 维持现图 below_spec_confirmed：本宿：站名命中但 7.05<8.47
- st02320 维持现图 below_spec_confirmed：観音寺：最高 6.83<8.07
- st02333 维持现图 below_spec_confirmed：名和：最高 8.53<9.15
- st02340 维持现图 below_spec_confirmed：朝倉：最高 7.95<8.05
- st02364 维持现图 below_spec_confirmed：内海：站名命中但最高 7.34<8.93
- st02826 维持现图 below_spec_confirmed：東山公園：最高 6.71<7.80
- st03049 维持现图 below_spec_confirmed：江南：站名命中但 6.31<8.15
- st03052 维持现图 below_spec_confirmed：岩倉：站名命中但最高 5.89<8.51
- st03215 维持现图 below_spec_confirmed：森林公園：最高 7.06<8.68
- st03440 维持现图 below_spec_confirmed：日進：站名命中但 7.31<8.23
- st03948 维持现图 below_spec_confirmed：新富士：站名命中但 6.81<8.41
- st04204 维持现图 below_spec_confirmed：清水：站名命中但最高 6.84<7.85
- st06173 维持现图 below_spec_confirmed：若林：站名命中但 8.05<9.10
- B45 三查：foreign 0 / same_name_other_line 0 / dup_image 0（runner verify 通过后提交 cf9589c3）
- B45 runner replaced=0、confirmed=0；staged=74 条覆盖 25 站；rejected_notable=54；本地接受 1


## ws17 P1 missing st00258 大久保（同名异公司，2026-11-07）
- st00258 大久保（兵庫・山陽本線）图误为秋田 JR东日本大久保（前图亦为东京中央线大久保），第四查 operator_mismatch；无正确图可用 → 撤图置 missing + below_spec_confirmed，index 摘除，photo/license 删除。


## ws17 below-spec replace WS17-B46r — 2026-11-07T10:45:18Z
- queue: 25 站（review/below_spec 高分替换）
- replaced=3 staged=21 confirmed=1 skipped=0
- reject_dist={"hard_excluded": 26, "same_as_current": 25, "resolution_low_lt_1600": 107, "duplicate_title": 10, "resolution_not_upgrade": 14, "title_names_other_station": 87, "oversize_gt_25mb": 2, "title_non_station_scene": 6, "mime_unsupported": 112, "no_author_metadata": 6, "quality_reject_low_color": 10, "license_unclear": 7}


## ws17 local accept WS17-B46r — 2026-11-07T10:50:23Z
- st01718 维持现图 below_spec_confirmed：本庄：最高 6.03<7.21
- st01843 维持现图 below_spec_confirmed：磯部：最高 7.41<9.14（/2,/3 为 JR東日本 新潟磯部，异县）
- st02076 维持现图 below_spec_confirmed：大袋：最高 7.13<9.52
- st02881 维持现图 below_spec_confirmed：阿波山川：6.67>3.08 但为「109米」里程碑石，非站景
- st02882 维持现图 below_spec_confirmed：山瀬：最高 7.14<7.51
- st02889 维持现图 below_spec_confirmed：下浦：最高 7.14<7.50
- st02900 维持现图 below_spec_confirmed：文化の森：最高 6.21<6.66
- st02937 维持现图 below_spec_confirmed：佃：最高 6.66<7.34
- st02940 维持现图 below_spec_confirmed：三加茂：7.79>5.45 但为道の駅/路边建筑，无站名
- st03204 维持现图 below_spec_confirmed：ふじみ野：最高 7.00<7.17（/2,/3 为东京地铁车照）
- st03214 维持现图 below_spec_confirmed：森林公園：7.06>5.52 但为站前广场，无站名
- st03438 维持现图 below_spec_confirmed：日進：最高 7.21<9.02
- st04383 维持现图 below_spec_confirmed：所沢：最高 6.73<7.03
- st05211 维持现图 below_spec_confirmed：新郷：最高 6.02<6.38
- st05592 维持现图 below_spec_confirmed：永田：最高 6.44<9.42
- st05613 维持现图 below_spec_confirmed：東吾野：最高 7.54<8.96
- st05616 维持现图 below_spec_confirmed：正丸：最高 6.60<8.78
- st05885 维持现图 below_spec_confirmed：武州長瀬：站名命中但最高 6.58<7.14
- st06121 维持现图 below_spec_confirmed：航空公園：最高 7.00<7.17
- st06655 维持现图 below_spec_confirmed：道法寺：最高 7.55<8.40
- st07648 维持现图 below_spec_confirmed：西武園ゆうえんち：最高 6.59<8.97
- B46 首次 run 42363542677 因交换提交撞 head 失败；重派 B46r run 42364612763 success → 提交 e1e7b330
- B46r 三查：foreign 0 / same_name_other_line 0 / dup_image 0；第四查候选 4 条（磯部 JR东日本异县、ふじみ野 地铁车照）均不接
- B46r runner replaced=3（st01331 大宮/st01206 新田/st00541 石井，运营者均正确）、confirmed=1；staged=62（21 站）；本地 0 接受


## ws17 below-spec replace WS17-C01 — 2026-11-07T11:03:28Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=2 staged=22 confirmed=0 skipped=0
- reject_dist={"title_non_station_scene": 15, "duplicate_title": 22, "resolution_not_upgrade": 62, "hard_excluded": 59, "resolution_low_lt_1600": 89, "same_as_current": 24, "quality_reject_low_color": 30, "title_names_other_station": 72, "mime_unsupported": 10, "no_author_metadata": 7}


## ws17 C01 cleanup 裁决 — 2026-11-09T06:04:28Z（runner 42365826212）
- st01196 木津 置 missing+bsc，删 photo/license：c1 无站证、c2=新木津駅遗迹非本站、c3 木津改札内景 isc2.35≪8.66 且无站名牌
- st01265 伊丹 置 missing+bsc，删 photo/license：c1/c2 阪急伊丹(异社，第四查拦)；c3 JR伊丹観光案内所/キオスク店铺内景 isc6.35<8.4，非站舍
- st00467 住吉 置 missing+bsc，删 photo/license：c1 阪神住吉(异社)；c2 六甲ライナー住吉(神戸新交通，非JR)
- st01317 垂水 转 review：第四查「山陽」为误报：Sanyo Main Line=JR山陽本線，c2 OCR「JR神戸線 西明石・姫路方面」可证；3 张 isc≤5.86<7.35，待人工决定是否降分接受
- st01293 塚口 置 missing+bsc，删 photo/license：c1/c3 阪急塚口(异社)；c2 券売機画面特写非站景
- st03265 相野 置 missing+bsc，删 photo/license：3 张全为秋田県「あいのの」駅(JR東日本)，异县异地区，第四查 3 命中
- st03805 佐倉 置 missing+bsc，删 photo/license：runner 无候选返回
- st05483 本八幡 转 review：c2/c3 都営地下鉄本八幡(异社)；c1 仅见「JR総武線」导向牌、无站名牌且标题为都営新宿線，证据不足
- st02737 別府 转 review：c3=福岡 別府駅(异县)；c1 夜景无站证；c2 标题「JR別府駅」但为 1800×533 超宽条幅，按坑⑤不得裁切使用
- st07007 大神 转 review：c1/c3=秋田 男鹿駅(异县，第四查 JR東日本)；c2 OCR「大神駅」正确但 isc5.66<8.49
- st07025 立石 置 missing+bsc，删 photo/license：3 张全为京成 立石/青砥-亀有 东京都景(异社异县)，c1 第四查命中京成
- st00068 福島 转 review：c1 OCR「福島駅 ふくしま」+标题 Fukushima Station (JR West) 正确、c2 大阪環状線福島駅正确；isc≤6.04<7.81；c3 阪神福島(异社)
- st00072 西九条 置 missing+bsc，删 photo/license：runner 无候选返回
- st01207 新田 置 missing+bsc，删 photo/license：c1「SHINDEN STATION」无法确认为宮城県新田、c2 東武200系车照、c3 下新田駅(群馬)
- st07267 埴生 转 review：c1 OCR「厚狭/新山口方面/下関・九州方面」可证 JR 埴生，isc6.65<7.42；c3 isc7.79>7.42 但无可见站名牌，二者择一待人工
- st05376 島田 转 review：c1/c2 OCR「島田駅」正确(山口 島田)，isc≤7.71<8.01；c3 待合室内景无站证
- st05513 富士急ハイランド 转 review：3 张均为本站富士急ハイランド駅，第四查「富士急」判异社源于 index lines 推得 exp=JR，属基线冲突，需人工确认运营者口径
- st00534 大原 转 review：c1 OCR「大原駅」+标题 Ōhara Station (Okayama) 正确，isc7.6<9.14；c2=千葉 大原(异县)、c3=西大原
- st05185 邑久 置 missing+bsc，删 photo/license：3 张全为東京 尾久駅(JR東日本 東北本線)，异县；c1/c3 第四查命中
- st00880 大門 置 missing+bsc，删 photo/license：3 张全为都営浅草線 大門(東京)，目检均地下铁站台；c2 第四查命中都営，c1/c3 靠目检补拦
- st01120 京橋 接受 c3「File:Tokyo-Metro Kyobashi-STA Platform1-2.jpg」isc 7.44→7.86（photo+license 同步换）
- st03823 馬喰町 转 review：第四查「都営」为误报(画面内「都営地下鉄新宿線は西口へ」导向牌)；c1 为 JR 馬喰町総武快速站台，但现图长边2048>候选1800，不满足长边条件
- st02123 東武ワールドスクウェア 转 review：3 张均为本站東武ワールドスクウェア駅，第四查「東武」判异社源于 index lines 推得 exp=JR，属基线冲突，需人工确认
- st01993 守山 置 missing+bsc，删 photo/license：c1=磐城守山(福島)、c2=锦绘非站景、c3 告示为「奈良線/京都」与滋賀 守山(琵琶湖線)不符
- 合计 ACCEPT 1 / MISSING_BSC 12 / REVIEW 11；第四查对 Sanyo Main Line、都営导向牌、lines 跨社污染产生的误报已逐条人工复核。


## ws17 below-spec replace WS17-C02 — 2026-11-09T06:33:00Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=1 staged=15 confirmed=0 skipped=8
- reject_dist={"title_names_other_station": 67, "hard_excluded": 55, "resolution_low_lt_1600": 86, "same_as_current": 16, "mime_unsupported": 29, "duplicate_title": 10, "resolution_not_upgrade": 19, "title_non_station_scene": 15, "quality_reject_low_color": 10, "license_unclear": 6, "license_forbidden": 2, "no_author_metadata": 1}


## ws17 WS17-MISS01 无图站重捕裁决 — 2026-11-09T06:41:06Z（runner 42571733409, artifact 13653937312）
- st00014  runner 无候选，保留 review 转 WS17-MISS02
- st00040 大谷 置 missing+bsc：3 张全为韩国大邱 Daegok（Daegu 地铁 / Korail K322），c3 见「Way out 出口 / Transfer 換乘」——第一查 foreign 直接拦截
- st00051  runner 无候选，保留 review 转 WS17-MISS02
- st00085  runner 无候选，保留 review 转 WS17-MISS02
- st00149 土橋 置 missing+bsc：3 张全为名鉄 土橋駅（愛知県豊田市），OCR「土橋駅 MEITETSU TSUCHIHASHI STATION」；基线 愛媛県 郡中線（伊予鉄）。opcheck 因 郡中線 无 LINE_OP 映射未命中，人工按同名异社拦截
- st00170  runner 无候选，保留 review 转 WS17-MISS02
- st00182  runner 无候选，保留 review 转 WS17-MISS02
- st00190 稲荷町 置 missing+bsc：3 张全为東京メトロ銀座線 稲荷町（OCR いなりちょう / たわらまち），基线 広島県 広島電鉄 稲荷町 → 同名异社异县
- st00254 追分 接受 c1「File:JR Muroran-Main-Line・Sekisho-Line Oiwake Station building.jpg」isc 6.65（photo+license 同步落库）
- st00258 大久保 置 missing+bsc：c1/c2 秋田県潟上市 JR東日本 大久保（第四查两条 jr_region_mismatch）、c3 東京 JR中央・総武線 大久保（OCR 中央・総武線）；基线 兵庫県 北陸本線/山陽本線。按交接文档「st00258 置 missing+bsc」执行
- st00259  runner 无候选，保留 review 转 WS17-MISS02
- st00309 青山 接受 c1「File:JR Echigo Line Aoyama Station building.jpg」isc 6.76（photo+license 同步落库）
- st00353 市立病院前 置 missing+bsc：c1/c2 均为沖縄ゆいレール 市立病院前（高架单轨），基线 鹿児島県 鹿児島市電第二期線 路面电车站 → 同名异县异社
- st00377  runner 无候选，保留 review 转 WS17-MISS02
- st00378 中郡 置 missing+bsc：c1/c2 均为山形県 JR東日本 中郡（第四查两条命中 obs=JR東日本 exp=JR九州），基线 鹿児島市電 中郡 → 异地区异社
- st00380  runner 无候选，保留 review 转 WS17-MISS02
- st00424 貝塚 接受 c3「File:Platform of Kaizuka Station (Nishitetsu Kaizuka Line) 8.jpg」isc 6.07（photo+license 同步落库）
- st00457 大橋 置 missing+bsc：c1 西武多摩川線 是政駅と是政大橋（非本站）、c2 国立国会图书馆锦绘「木曽六十九駅 京都三條大橋」非站景照片；基线 長崎県 長崎電気軌道 大橋
- st00469 住吉 转 review：3 张均为阪堺線/上町線 住吉 路面电车照，线路相符但 self_hit=False、无可见站名牌（subject_unverified），且 st00469 处于 dup_quarantine 重复图组 → 保留人工复核
- st00473 石橋 置 missing+bsc：c1 JR東日本 石橋駅（栃木，第四查命中），基线 長崎県 長崎電軌大浦支線 石橋 → 同名异社
- st00571 栄 置 missing+bsc：c1/c3 名古屋市営地下鉄名城線 栄（OCR M 名城線）、c2 神鉄 栄（obs=神鉄，opcheck 因 水島本線 无映射漏判，人工拦截）；基线 岡山県 水島本線 栄
- st00577 福井 置 missing+bsc：c1 JR西日本 福井駅、c2/c3 JR貨物 南福井駅 （OCR 南福井駅），均 福井県；基线 岡山県 水島本線 福井 → 异县异社
- st00580 球場前 转 review：c2/c3 为水島臨海鉄道 キハ37 103 车辆照（运营者相符，OCR MIZUSHIMA RINKAI RAILWAY），但无站景/站名牌；c1 西武球場前 异社。属 no_station_evidence，保留人工复核
- st00602  runner 无候选，保留 review 转 WS17-MISS02
- 合计 ACCEPT 3 / MISSING_BSC 10 / REVIEW 2 / RETRY 9；40 候选逐条跑 OCR + 第四查，另人工补拦 opcheck 无 LINE_OP 映射的 st00149（名鉄土橋）、st00571（神鉄栄）两条同名异社。


## ws17 below-spec replace WS17-MISS02 — 2026-11-09T06:54:37Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=1 staged=16 confirmed=7 skipped=0
- reject_dist={"title_names_other_station": 88, "resolution_low_lt_1600": 91, "hard_excluded": 27, "no_author_metadata": 5, "mime_unsupported": 104, "duplicate_title": 16, "oversize_gt_25mb": 1, "title_non_station_scene": 22, "quality_reject_low_color": 10}


## WS17-C02 本地裁决 — 2026-11-09T06:55:50Z（runner 42571781149）
- st00298 今川 撤图置 missing+bsc：3 张全为新潟 羽越線 JR東日本 今川駅（OCR 今川駅 Imagawa Station / 羽越線 村上・新津方面），第四查 3 条 jr_region_mismatch；现挂图同为 JR East Imagawa，属同名簇错挂，一并撤除
- st00707 山本 撤图置 missing+bsc：c1「旧筑肥線山本駅」实为唐津市農協第2みかん選果場厂房（OCR 可证）非站景；c2/c3 为韩国 Korail 산본 Sanbon（OCR KORAIL / Surisan），第一查 foreign；现挂图为阪急山本，属错挂，撤除
- st02304 南桜井 接受 c1「File:Minamisakurai Station South Entrance 1.JPG」isc 6.26（替换原错挂图 File:Meitetsu Minami-Sakurai-STA Platforms.jpg）
- st02667 学園前 接受 c1「File:Keisei-railway-KS63-Gakuemmae-station-building-east-20200809-092452.jpg」isc 6.53（替换原错挂图 File:FamilyMart Kintetsu Gakuen-mae station No.2 platform ce）
- st02691 今津 接受 c1「File:阪神今津駅1番線ホーム.jpg」isc 6.18（替换原错挂图 File:阪急今津駅ホーム2.jpg）
- st02753 御影 接受 c1「File:阪神御影駅1・2番線ホーム.jpg」isc 6.25（替换原错挂图 File:阪急御影駅大阪方面ホーム.jpg）
- st02754 御影 接受 c1「File:JR Nemuro-Main-Line Mikage Station Platform.jpg」isc 6.11（替换原错挂图 File:Hanshin Mikage Station north entrance.jpg）
- st03376 石田 接受 c1「File:京都市営地下鉄石田駅2番出入口.jpg」isc 6.54（替换原错挂图 File:Odakyu-electric-railway-Odawara-line-Aiko-ishida-statio）
- st03565 荒尾 接受 c1「File:Platform of Arao Station (Kagoshima Main Line).jpg」isc 6.97（替换原错挂图 File:JR Central Arao Station Overall.jpg）
- st03592 朝地 接受 c1「File:JR-Kyushu-Asazi-Station.jpg」isc 4.74（替换原错挂图 File:Tobus P-M188 To-02-otsu Extend.jpg）
- st04923 春日野道 撤图置 missing+bsc：3 张均为阪急 春日野道（dist≈509m，第四查 3 条 operator_mismatch exp=阪神 obs=阪急），同名异社；现挂图也是阪急春日野道，属错挂，撤除
- st04924 春日野道 接受 c3「File:Hankyu Kasuganomichi Station platform - panoramio (11).jpg」isc 7.01（替换原错挂图 File:阪神春日野道駅大阪方面ホーム.jpg）
- st06216 岡本 接受 c1「File:阪急岡本駅1号線ホーム.jpg」isc 6.56（替换原错挂图 File:JR East Okamoto Station Platform 20221127.jpg）
- st07011 日代 撤图置 missing+bsc：3 张全为车辆照（225系100番代 / JNR DD51 844 ×2），无站景无站名牌，no_station_evidence；现挂近鉄18400 亦为车辆照，撤除
- st08644 永山 接受 c1「File:JR Soya-Main-Line Nagayama Station Platform.jpg」isc 6.82（替换原错挂图 File:Odakyu-Nagayama Station Platform 02.jpg）
- 合计 ACCEPT 11 / MISSING_BSC 4 / REVIEW 0 / RETRY 0 / NOOP 0；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## WS17-MISS02 本地裁决 — 2026-11-09T07:05:00Z（runner 42574830320）
- st00649 松原 接受 c3「File:Tokyu Matsubara-STA Platforms.jpg」isc 7.36（替换原错挂图 None）
- st00693 小倉 接受 c2「File:近鉄京都線 小倉駅 Ogura station 2013.1.10 - panoramio (1).jpg」isc 6.25（替换原错挂图 None）
- st00703 岩屋 撤图置 missing+bsc：3 张全为兵庫県 阪神岩屋駅：c2/c3 第四查 operator_mismatch（exp=JR obs=阪神），c1 OCR「阪神電車 岩屋駅（兵庫県立美術館）」；基线佐賀県唐津線，同名异县异社
- st00716 北方 转 review：c1「北九州モノレール」高架站区 dist 234.1m 但全图无站名牌、runner 因「标题无站名且 dist>200m」暂存；放大目检仍无可读站名，证据不足留人工；c2 岐阜美濃北方、c3 岐阜県警察署均非本站
- st00812 新川 撤图置 missing+bsc：c1 宮城県 JR東日本 奥新川駅（第四查 jr_region_mismatch）；c2/c3「Joden-Nikkawa-station」经 Commons/Wikidata 查证为群馬県桐生市 上毛電気鉄道 新川駅（Nikkawa, Jōmō Line），OCR「新川駅 にっかわ」；基线愛媛県伊予鉄郡中線，同名簇全错
- st00813 新川 撤图置 missing+bsc：同一组同名簇：c1/c3 为群馬県上毛電鉄 新川駅（已查证），c2 宮城県 JR東日本 奥新川駅（第四查命中）；基线愛知県豊橋鉄道東田本線，无一正确
- st00824 野志 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st00827 東野 接受 c2「File:Higashino station, Ena 2021-11.jpg」isc 7.72（替换原错挂图 None）
- st00949 馬場崎町 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st00957 和田浜 撤图置 missing+bsc：唯一候选「和田浜海岸から富士山」为静岡海岸风景照（棕榈树+富士山），非站景，no_station_evidence
- st01041 岡田 接受 c1「File:Kotoden-Kotohira-line-Okada-station-platform-20100805.jpg」isc 6.12（替换原错挂图 None）
- st01048 四所 接受 c1「File:Sisyo, enclosure, Kitakinki Tango Railway, 20080815.jpg」isc 6.22（替换原错挂图 None）
- st01070 万博記念公園 撤图置 missing+bsc：3 张均为大阪モノレール 万博記念公園駅（c2 OCR「本阪モノール 万博記念公園駅」、目检单轨高架与站台）；基线茨城県つくばエクスプレス，同名异县异社
- st01129 北浦 撤图置 missing+bsc：3 张全为宮城県 JR東日本 北浦駅（第四查 3 条 jr_region_mismatch exp=JR四国 obs=JR東日本）；基线高知県とさでん交通路面电车站
- st01167 上金田 撤图置 missing+bsc：3 张全为加拿大 Calgary「Olympic Oval / Anneau Olympique / 188 University Gate」（OCR 可证），第一查 foreign 直接拦截
- st01168 糒 撤图置 missing+bsc：c1 为 Comic Market 91 Cosplay 人像、c2 为乐队专辑封面插画，均非站景，no_station_evidence
- st01169 田川市立病院 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st01170 下伊田 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st01174 柿下温泉口 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st01180 犀川 撤图置 missing+bsc：c1 犀川調整扉門说明牌、c2 犀川河道、c3 水坝，三张均为河流/水利设施，无站景无站名牌
- st01181 東犀川三四郎 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st01185 今川河童 保留现状：runner 未返回候选，保留 review 转后续批次重捕
- st01213 木幡 保留现状：runner 自动接受的「木幡駅 - panoramio」已复核：evidence.dist_m=50.8m（京阪木幡约 700m 外）、目检站名牌「木幡」+ JR 奈良线复线架空线，四查无告警，保留
- st01215 木幡 撤图置 missing+bsc：同名三社簇：c1/c3 为神戸電鉄木幡（c1 第四查 operator_mismatch exp=京阪 obs=神鉄），c2 为 JR奈良線木幡駅；基线京阪宇治線木幡駅（读 Kowata），无一正确
- 合计 ACCEPT 5 / MISSING_BSC 10 / REVIEW 1 / RETRY 7 / NOOP 1；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## WS17-C03 本地裁决 — 2026-11-09T07:14:02Z（runner 42574870477）
- st00055 桜井 转 review：现图为桜井駅站台厕所特写（2048×1152，OCR 仅 Sakurai），站证弱但确系本站；候选 c1/c2「JR桜井線 桜井駅」dist 95.7/83.9m、OCR「桜井駅」站舍全景更好，但长边 1800<2048 违反「只升不降」；c3 名鉄桜井异社。留人工决定
- st00535 大原 撤图置 missing+bsc：3 张全为千葉県いすみ鉄道 大原/西大原（c1 标题即含 Chiba、c2 西大原）；现挂也是 JR East・Isumi Railway 大原，属同名异县；基线広島アストラムライン大原为高架站，撤除
- st00570 常盤 接受 c1「File:JR West Tokiwa Station.jpg」isc 7.31（替换原错挂图 File:JR Central Kai-tokiwa Station Platform (20221002).jpg）
- st00812 新川 撤图置 missing+bsc：WS17-MISS02 已裁 missing+bsc（宮城奥新川 / 群馬上毛電鉄新川 同名簇）；本次仅清理 index 残留 source_title/score，避免后续 opcheck --current 误报
- st00813 新川 撤图置 missing+bsc：同 st00812：WS17-MISS02 已裁决，本次清理 index 残留元数据
- st02047 桜川 保留现状：现挂「阪神桜川駅ホーム」isc 7.71 已是本站（基线含阪神なんば線）；候选 c1/c2 同站但 isc 6.48/5.89 更低，无替换价值。第四查 exp=近鉄 obs=阪神 属 LINE_OP 未覆盖阪神なんば線的基线误报，保留现图
- st02783 春日井 保留现状：现挂「Kasugai Station (Meitetsu)」isc 7.46 为名鉄小牧線（旧上飯田線）春日井駅，正确；候选 3 张全是 JR東海中央本線 春日井駅（另一座同名站，c1 山车祭、c2 自行车场、c3 站前时钟塔），异社且非站舍，保留现图
- st03254 野崎 接受 c2「File:Nozaki Station (Osaka) west entrance.jpg」isc 7.67（替换原错挂图 File:JR East Nozaki Station building 20221127.jpg）
- st04168 相生 撤图置 missing+bsc：3 张全为兵庫県 JR西日本 相生駅（c1/c2「JR Aioi Station」、c3 JRW225 车辆），现挂也是 JR West Aioi South Gate；基线岐阜県長良川鉄道越美南線相生，同名异县异社，撤除
- st04783 山田 接受 c2「File:阪急千里線 山田駅 Yamada sta. 2013.12.01 - panoramio.jpg」isc 6.12（替换原错挂图 File:大阪モノレール山田駅発車標 2番ホーム千里中央行き.jpg）
- st04971 矢田 撤图置 missing+bsc：c1 名鉄矢田駅（第四查 operator_mismatch exp=近鉄 obs=名鉄）、c2 阪和貨物線线路照非站景；现挂也是名鉄矢田站台，同名异社，撤除
- st05682 中川 撤图置 missing+bsc：c2/c3「KT-Nakagawa Station WestGate」OCR「伊勢中川」= 三重県近鉄伊勢中川駅，c1 近鉄エキファミ店内（第四查 obs=近鉄）；现挂也是 KINTETSU ISE-NAKAGAWA；基线山形県奥羽本線中川，同名异县异社，撤除
- 合计 ACCEPT 3 / MISSING_BSC 6 / REVIEW 1 / RETRY 0 / NOOP 2；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## WS17-C04 本地裁决 — 2026-11-09T07:22:02Z（runner 42576349698）
- st00648 松原 撤图置 missing+bsc：3 张全为東京都世田谷区（東急世田谷線松原 / 京王井の頭線明大前 / 小田急梅ヶ丘），现挂近鉄河内松原（大阪）亦错；基线長崎県大村線，同名簇无一正确
- st01129 北浦 撤图置 missing+bsc：WS17-MISS02 已裁 missing+bsc（宮城 JR東日本 北浦，第四查 3 条命中）；本次清理 index 残留 source_title/score
- st01648 黒川 撤图置 missing+bsc：3 张全为兵庫県 能勢電鉄 妙見の森ケーブル黒川駅（OCR「妙見の森ケーブル 黒川駅 / 妙見ケーブルのりば」），现挂小田急多摩線黒川駅（東京）亦错；基线香川県土讃線
- st02234 桜台 接受 c2「File:Platform of Sakuradai Station (Nishitetsu) 2.jpg」isc 5.45（替换原错挂图 File:Seibu Railway Shin-Sakuradai Station Platform 1.jpg）
- st02342 朝倉 撤图置 missing+bsc：3 张全为愛知県名鉄 朝倉駅（c1/c2 第四查 operator_mismatch exp=JR obs=名鉄、c3 名鉄朝倉巴士站）；基线高知県土讃線/中村線，同名异社
- st02440 下島 撤图置 missing+bsc：3 张为広島県大崎下島御手洗町並み保存地区街景（OCR「江戸みなとまち展示館」），非站景；现挂 JR東海飯田線下島駅（伊那市）异社；基线アルピコ上高地線下島駅（松本）
- st03268 瀬田 撤图置 missing+bsc：c1/c2 滋賀県 JR西日本 瀬田駅（第四查 jr_region_mismatch），c3 世田谷区豪徳寺商店街；现挂也是 JR West Seta；基线熊本県豊肥本線瀬田，同名异县
- st03784 北山 撤图置 missing+bsc：c1 为广州地铁 12 号线 北山站（GZMTR，第一查 foreign）、c2/c3 宮城県 JR東日本 北山駅（第四查 2 条命中）；现挂也是 JREast 仙山線北山；基线高知県とさでん伊野線
- st04226 豊洲 保留现状：现挂「ゆりかもめ豊洲駅のプラットホーム」isc 7.98 即本站（基线含東京臨海新交通臨海線），候选 c3 東京メトロ豊洲駅出入口 isc 7.4 更低；c2 第四查 obs=ゆりかもめ 属 LINE_OP 未覆盖临海线的基线误报，保留现图
- st04240 汐留 保留现状：现挂「ゆりかもめ汐留駅駅舎」isc 8.22 正确；3 张候选均为都営大江戸線汐留駅扶梯内景、isc≤6.5 且无站名牌，无替换价值，保留现图
- st05030 御来屋 接受 c3「File:Mikuriya Station (Tottori) waiting room ヨ5000.jpg」isc 6.61（替换原错挂图 File:JR Central Mikuriya Station Gate.jpg）
- st05532 菊川 撤图置 missing+bsc：3 张全为静岡県 JR東海 菊川駅（c1/c2 第四查 jr_region_mismatch exp=JR東日本 obs=JR東海，OCR 東海道線浜松・豊橋方面）；现挂也是 JR Central Kikugawa；基线東京都都営新宿線菊川，同名异县异社
- st05681 中川 撤图置 missing+bsc：3 张全为三重県 近鉄伊勢中川駅（c1 第四查 exp=横浜市営 obs=近鉄，c2/c3 OCR「伊勢中川」），现挂也是 KINTETSU ISE-NAKAGAWA；基线横浜市営地下鉄中川，同名异县异社
- st05973 大山 撤图置 missing+bsc：c1/c2 为栃木県 JR 小山駅（Oyama）东西口、c3 为鹿児島 西大山駅看板（OCR「西大山駅 JR日本最南端」）——站名与基线「大山」均不符；现挂山形県 羽前大山駅亦错，同名簇无一正确
- st08626 愛野 撤图置 missing+bsc：3 张全为静岡県 JR東海 愛野駅（第四查 3 条 jr_region_mismatch exp=JR九州 obs=JR東海），现挂也是 JR Central Aino；基线長崎県島原鉄道愛野，同名异县异社
- 合计 ACCEPT 2 / MISSING_BSC 11 / REVIEW 0 / RETRY 0 / NOOP 2；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## ws17 below-spec replace WS17-MISS03 — 2026-11-09T07:39:52Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=5 staged=16 confirmed=3 skipped=0
- reject_dist={"resolution_low_lt_1600": 81, "title_names_other_station": 62, "hard_excluded": 27, "title_non_station_scene": 13, "quality_reject_low_color": 10, "mime_unsupported": 45, "duplicate_title": 29, "no_author_metadata": 1, "license_unclear": 9}


## WS17-MISS03 本地裁决 — 2026-11-09T08:10:49Z（runner 42579693074）
- st01240 島ケ原 撤图置 missing+bsc：唯一候选「正月堂」为神社门楼且 GPS dist 1517.3m；现挂图为島ヶ原大橋风景非站景，runner 本轮无合格候选，撤图。
- st01241 西木津 撤图置 missing+bsc：3 张为 1989 年片町線车辆照与神户市立木津小学（神戸電鉄木津同名异社），均非站景；现挂图「Junction at JRW Kizu station」是木津駅而非西木津，撤图。
- st01249 長尾 撤图置 missing+bsc：第四查 FLAG：c1 OCR「エことでん 長尾駅 Nagao Station」、c2「Kotoden-Nagao-line」均为香川県高松琴平電鉄長尾駅，与目标大阪府 JR 片町線長尾同名异县异社；c3 为片町線车辆照无站景。现挂图同为香川「Nagao Station (Kagawa)」，撤图。
- st01282 柏原 撤图置 missing+bsc：c1 航空写真、c3 售票机均非站景；c2 木造站舍内部 OCR「篠山口・大阪方面」「For Fukuchiyama」，与现挂图「Kaibara Station Tamba Hyogo pref」同属兵庫県福知山線柏原駅，与目标滋賀県東海道本線柏原同名异线，撤图。
- st01288 三郷 保留现状：runner 已自动替换并随 9a1491eb 入库；本地回读 photo 放大复核为名鉄瀬戸線三郷駅站台（愛知県），线路 / 都道府県 / 运营者一致，第四查无冲突，保留现挂图。
- st01302 芦屋 保留现状：runner 已自动替换并随 9a1491eb 入库；本地回读 photo 放大复核为阪神本線芦屋駅2番線ホーム（兵庫県），线路 / 都道府県 / 运营者一致，第四查无冲突，保留现挂图。
- st01353 河原町 撤图置 missing+bsc：2 张候选与现挂图均为阪急京都河原町（OCR「高槻市・茨木市・淡路」「Umeda」「KYOTO」），目标为熊本県熊本市電河原町，同名异县异社，撤图。
- st01373 国府 保留现状：runner 已自动替换并随 9a1491eb 入库；本地回读 photo 放大复核为名鉄名古屋本線国府駅站舍（愛知県，dist 95.2m），线路 / 都道府県 / 运营者一致，第四查无冲突，保留现挂图。
- st01414 高ノ宮 撤图置 missing+bsc：3 张为高ノ宮神社鸟居 / 社殿 / 伊势神宫，无站景；本就无现挂图。
- st01416 朝日ケ丘 撤图置 missing+bsc：c2「Asahigaoka Station (Toyama)」为富山同名异县；c1 岐阜関市旭ヶ丘学校、c3 指挥中心，均非島根県北松江線朝日ケ丘，本就无图。
- st01432 県庁前 撤图置 missing+bsc：候选为千葉「Kenchō-mae Station (Chiba)」与沖縄ゆいレール県庁前，且第三查与 st01433/st01435 批内共享同图（intra-batch dup）；现挂图为千葉モノレール県庁前，与目标富山県同名异县，撤图。
- st01433 県庁前 撤图置 missing+bsc：候选与现挂图均为千葉県庁前 / 沖縄ゆいレール，目标高知県伊野線県庁前，同名异县；并与 st01432/st01435 批内重复同图，撤图。
- st01435 県庁前 撤图置 missing+bsc：候选为千葉県庁前 / 沖縄ゆいレール，现挂图即沖縄ゆいレール美栄橋駅，目标広島県広島新交通1号線県庁前，同名异县；批内重复同图，撤图。
- st01436 県庁前 保留现状：runner 已自动替换并随 9a1491eb 入库；本地回读 photo 放大复核为神戸市営地下鉄県庁前駅东出口（兵庫県，可见站名牌），线路 / 都道府県 / 运营者一致，第四查无冲突，保留现挂图。
- st01459 小泉町 撤图置 missing+bsc：候选与现挂图均为群馬県東武小泉町駅（OCR「小泉町駅 Koizumimachi Station」「Gunma Koizumimachi」），目标为富山県富山軌道線小泉町，同名异县异社，撤图。
- st01474 泉 接受 c1「File:JR Jōban Line Izumi Station Platform.jpg」isc 7.10（替换原错挂图 None）
- st01492 西日暮里 保留现状：runner 已自动替换并随 9a1491eb 入库；本地回读 photo 放大复核为JR 西日暮里駅站台（東京都），线路 / 都道府県 / 运营者一致，第四查无冲突，保留现挂图。
- st01523 霞ケ関 撤图置 missing+bsc：c1 为锦绘「霞ケ関」非站景；c2/c3 与现挂图均为東京メトロ霞ケ関（東京都），目标埼玉県東上本線霞ケ関，同名异县异社；c2 sha 与现挂图相同属自我重复，撤图。
- st01628 生田 撤图置 missing+bsc：c1「Komachi-21 running near Shoden Station」为列车+田野风景虽 dist 162.9m 但非站景；c2/c3 为神奈川小田急生田駅与闸机广告，同名异县，本就无图。
- st01659 杉塘 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st01792 松ケ崎 撤图置 missing+bsc：候选为京都市営地下鉄松ケ崎（OCR「まつがさき Matsugasaki 北山 国際会館 宝池」），目标三重県近鉄松ケ崎，同名异县异社，本就无图。
- st01798 明星 撤图置 missing+bsc：c1 锦绘、c2 EF65 列车照，c3「Chuomeiseistation」为多摩モノレール中央大学・明星大学駅，目标三重県近鉄明星，均不符，本就无图。
- st01836 粟ケ崎 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st01858 富士見ケ丘 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- 合计 ACCEPT 1 / MISSING_BSC 18 / REVIEW 0 / RETRY 0 / NOOP 5；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## WS17-B47 本地裁决 — 2026-11-09T08:12:06Z（runner 42579749344）
- st00007 高田 保留现状：3 张候选全为新潟「えちごトキめき鉄道妙高はねうまライン高田駅」站舍/闸机，与目标神奈川県横浜市営地下鉄4号線高田同名异县异社，保留现挂图。
- st00029 橋本 接受 c1「File:JREast-Yokohama-line-JH28-Hashimoto-station-platform-20220723-154851.jpg」isc 6.10（替换原错挂图 File:橋本駅 - panoramio.jpg）
- st00866 弘明寺 接受 c3「File:Gumyoji Station keikyu line - Nov 16 2020 various 16 56 42 142000.jpeg」isc 5.64（替换原错挂图 File:Subway-gumyoji-Sta-Platform.JPG）
- st00963 富士見町 接受 c1「File:Shonan-monorail-SMR2-Fujimicho-station-entrance-for-Ofuna-20200315-124127.jpg」isc 6.37（替换原错挂图 File:Shonan-monorail-SMR2-Fujimicho-station-platform-2020031）
- st00973 根岸 保留现状：runner 判定可替换（JR 根岸駅罐车货场），同上未回传且原图不可达；且该图主体为货运罐车非站舍站台，保留现挂图。
- st01387 富士フイルム前 接受 c1「File:Izuhakone-railway-Daiyuzan-line-Fuji-film-mae-station-platform-20140310-141146.jpg」isc 6.78（替换原错挂图 File:Izuhakone-railway-Daiyuzan-line-Fuji-film-mae-station-b）
- st01423 こどもの国 接受 c2「File:Kodomonokuni Station -83318.jpeg」isc 6.74（替换原错挂图 File:MT-Kodomonokuni Station-Platform 3.jpg）
- st01614 海老名 保留现状：三张候选均为海老名站前广场 / 列车照，非站舍站台主体；且与 st01615 完全共享同一组三张图（第三查 intra-batch dup），两站都不接受，保留现挂图。
- st01615 海老名 保留现状：同上：与 st01614 共享同一组三张图，重复图风险 + 无合格站景，保留现挂图。
- st01647 黒川 保留现状：三张均为小田急 5000/1000/3000 系车辆照（OCR「Odakyu / Shinjuku」），非黒川駅站景，保留现挂图。
- st01896 中山 保留现状：runner 判定可替换（JR横浜線中山駅站台），但 Step 10 Commit & push 因 head 变动失败，候选图未随 artifact 回传；Wikimedia 原图在本环境连接超时无法补回，保留现挂图不倒退。
- st01910 新杉田 接受 c3「File:Kanazawa-seaside-line-Shin-sugita-station-platform.jpg」isc 6.85（替换原错挂图 File:Seaside-line Shin-Sugita-STA Platform1-2.jpg）
- st02148 入谷 接受 c2「File:JR Sagami Line Iriya Station Platform.jpg」isc 7.81（替换原错挂图 File:入谷駅周辺.jpg）
- st02161 藤が丘 接受 c2「File:藤が丘駅, Fujigaoka Sta. - panoramio - xezna.jpg」isc 5.70（替换原错挂图 File:Tokyu Fujigaoka Station Platform 02.jpg）
- st03128 新綱島 接受 c2「File:新綱島駅改札口.jpg」isc 6.00（替换原错挂图 File:Tokyu-railway-SH02-Shin-tsunashima-station-platform-202）
- st03352 長谷 保留现状：runner 判定可替换（江ノ電長谷駅站舍），同上未回传且原图不可达，保留现挂图，留待下一轮重捕。
- st03836 横須賀 接受 c3「File:JR Yokosuka sta 001.jpg」isc 5.49（替换原错挂图 File:Yokosuka Station on a rainy day July 2 2021 various 05 ）
- st04392 大倉山 接受 c1「File:Okurayama Station -01.jpg」isc 6.92（替换原错挂图 File:Ōkurayama Sta platform 20201228 155344.jpg）
- st04398 新高島 保留现状：runner 判定可替换（新高島駅周边），同上未回传且原图不可达；站周边景亦非站主体，保留现挂图。
- st05062 市大医学部 接受 c2「File:Shidai-Igakubu-STA Gate.jpg」isc 7.68（替换原错挂图 File:Shidai-Igakubu-STA Platform.jpg）
- st05681 中川 保留现状：runner skipped（not_review_or_unknown）；该站已在 WS17-C04 确认 missing+bsc，不重复处理。
- st05736 小涌谷 接受 c3「File:Hakone-tozan-railway-OH55-Kowakidani-station-platform-20171230-120456.jpg」isc 5.98（替换原错挂图 File:Kowakidani station building.jpg）
- st06459 南橋本 接受 c1「File:JR Sagami Line Minami-Hashimoto Station Platform.jpg」isc 6.88（替换原错挂图 File:JR南橋本駅旧駅舎跡地.JPG）
- st06711 扇町 接受 c2「File:JREast-Tsurumi-line-JI10-Ogimachi-station-platform-20240203-142146.jpg」isc 7.34（替换原错挂图 File:JR Tsurumi Line Ōgimachi Station Platform.jpg）
- st06769 相模湖 接受 c1「File:JREast-Chuo-main-line-JC25-Sagamiko-station-platform-20220730-062444.jpg」isc 6.21（替换原错挂图 File:Sagamiko station platform 2-3 20211121 111425.jpg）
- 合计 ACCEPT 16 / MISSING_BSC 0 / REVIEW 0 / RETRY 0 / NOOP 9；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## ws17 below-spec replace WS17-MISS04 — 2026-11-09T08:28:08Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=3 staged=16 confirmed=5 skipped=0
- reject_dist={"resolution_low_lt_1600": 65, "quality_reject_low_color": 13, "no_author_metadata": 3, "title_names_other_station": 135, "hard_excluded": 21, "mime_unsupported": 55, "duplicate_title": 13, "license_unclear": 2, "near_duplicate": 1, "title_non_station_scene": 34}


## WS17-MISS04 本地裁决 — 2026-11-09T08:34:49Z（runner 42584813882）
- st01958 ラクテンチ上 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st02003 法界院 撤图置 missing+bsc：3 张「Hokaiin 02/03/05」放大后为法界院寺院山门/堂宇（石柱刻「法界院」），非津山線法界院駅站景，全部拦截。
- st02036 彦根口 接受 c1「File:HikoneGuchiEki KokokuBus 20070701.jpg」isc 5.69（替换原错挂图 None）
- st02056 水口城南 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st02188 蒲池 接受 c1「File:Nishitestu kamachi 2026.jpg」isc 6.53（替换原错挂图 None）
- st02193 三潴 撤图置 missing+bsc：c1「Mizuma Railway Mikeyamaguchi」三ヶ山口駅、c2 水間鉄道 0km 标、c3 放大后匾额「驛間水 / 水間観音駅」——整组为大阪府水間鉄道，与目标福岡県西鉄三潴同名异县异社，全部拦截。
- st02201 古賀茶屋 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st02231 塩塚 接受 c1「File:Nishitetsu Shiotsuka Station01.jpg」isc 6.61（替换原错挂图 None）
- st02232 徳益 撤图置 missing+bsc：2 张候选为「有明海沿岸道路 徳益IC」高速公路交流道（OCR「有明海沿岸道路」），不是车站，拦截。
- st02265 金山 接受 c2「File:Fukuoka Kanayama-STA Entrance2.jpg」isc 7.44（替换原错挂图 None）
- st02317 萩原 撤图置 missing+bsc：3 张「MT-Hagiwara Station」OCR「萩原駅 MEITETSU HAGIWARA STATION」为愛知県名鉄萩原駅，与目标福岡県筑豊電気鉄道線萩原同名异县异社，拦截。
- st02517 川路 接受 c3「File:Kawaji-eki2.JPG」isc 4.92（替换原错挂图 None）
- st02559 船尾 撤图置 missing+bsc：3 张「Hankai Funao」OCR「HN28/29 ふなお 船尾 FUNAO 石津 浜寺駅前」为大阪府阪堺電軌船尾，与目标福岡県後藤寺線船尾同名异县异社，拦截。
- st02668 学園前 撤图置 missing+bsc：c1「Keisei KS63 Gakuemmae」为千葉県京成千原線学園前（OCR「おゆみ野 がくえんまえ」），c2/c3 为奈良県近鉄学園前駅站内 FamilyMart 便利店（非站景），目标北海道東豊線学園前，全部拦截。
- st02692 今津 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st02732 高砂 撤图置 missing+bsc：c1 为高砂駅跡空地、c2「JR Hakodate-Main-Line Takasago Station」为北海道函館本線高砂駅、c3 为锦绘；目标兵庫県山陽電鉄高砂，同名异县异社，拦截。
- st02752 大阪梅田 保留现状：runner 已替换并随 ac54ad4b 入库；回读放大为阪急大阪梅田駅站内地下通道+扶梯，标题「阪急大阪梅田駅エスカレーター」线路/运营者/都道府県一致，虽取景为站内通道但无错站风险，保留现挂图。
- st02777 洗馬 接受 c3「File:JR Seba sta 001.jpg」isc 6.63（替换原错挂图 None）
- st02801 広小路 撤图置 missing+bsc：c1「Osaki-Hirokoji」OCR 含「TOKYUポイント / 立正大学」为東急池上線大崎広小路（東京）；c2 放大为三重県伊賀線「広小路駅 HIROKOJI STATION」木造站舍+红色 763 号车，c3 亦非万葉線电停；目标富山県高岡軌道線広小路，全部拦截。
- st02802 広小路 保留现状：runner 已替换并入库；回读为三重県伊賀線広小路駅木造站舍+单线站台+售货机，与基线一致，第四查无冲突，保留。
- st02903 中田 接受 c3「File:Yokohama-municipal-subway-B04-Nakada-station-platform-20230708-150302.jpg」isc 7.74（替换原错挂图 None）
- st03036 城下 保留现状：runner 已替换并入库；回读为岡山電気軌道東山本線城下电停（路面电车+岛式电停），与基线一致，保留。
- st03126 星川 接受 c3「File:SG-Hoshikawa Station-Building.jpg」isc 7.10（替换原错挂图 None）
- st03225 丹波大山 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- 合计 ACCEPT 8 / MISSING_BSC 13 / REVIEW 0 / RETRY 0 / NOOP 3；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## ws17 below-spec replace WS17-MISS05 — 2026-11-09T08:48:30Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=0 staged=14 confirmed=10 skipped=0
- reject_dist={"hard_excluded": 30, "resolution_low_lt_1600": 86, "duplicate_title": 8, "title_non_station_scene": 6, "title_names_other_station": 88, "quality_reject_low_color": 17, "mime_unsupported": 105, "license_unclear": 2, "quality_reject_blurry": 1, "no_author_metadata": 1, "license_forbidden": 4}


## WS17-MISS05 本地裁决 — 2026-11-09T08:56:18Z（runner 42587368140）
- st03236 吹田 接受 c3「File:阪急吹田駅西口.jpg」isc 6.24（替换原错挂图 None）
- st03261 古市 转 review：3 张候选「Furuichi station - Ssayama, Hyogo 福知山線古市駅 篠山市」确为兵庫県福知山線古市駅站舍/站台，但基线 lines 记为「JR東西線 / 東海道本線」，与候选线路不符；第二查同名簇线路比对存在冲突，既不误接受也不判无图，转人工复核（本就无现挂图）。
- st03280 小杉 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st03318 徳田 接受 c1「File:Tokuda Station 2020.jpg」isc 6.64（替换原错挂图 None）
- st03421 戸田 撤图置 missing+bsc：第四查 FLAG（jr_region_mismatch）：c1/c2 为埼玉県 JR 埼京線戸田駅（OCR「埼京線 Saikyo Line / 武蔵浦和・大宮・川越方面」），与目标山口県山陽本線戸田同名异县异线；c3 为锦绘。且与 st03422 共享同两张图，全部拦截。
- st03422 戸田 撤图置 missing+bsc：c1「Toda No.1 Railroad Crossing on the Kintetsu Nagoya Line」为铁路踏切+骑车人，非站舍/站台景；c2/c3 为埼玉県埼京線戸田駅（第四查 FLAG，JR東日本 vs 目标近鉄名古屋線），且与 st03421 批内重复同图，全部拦截。
- st03600 いこいの村 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st03646 朝菜町 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st03648 大泉 接受 c1「File:CT-Oizumi Station-Platform.jpg」isc 6.39（替换原错挂图 None）
- st03649 大泉 撤图置 missing+bsc：c1/c2 与 st03648 共享同一组「CT-Oizumi」富山地方鉄道大泉駅图（第三查 intra dup），不能重复挂图；独占的 c3「Img Oizumihigashi-station」站名「大泉東」≠目标「大泉」，且无站名牌证据，拦截。
- st03765 鹿児 撤图置 missing+bsc：2 张候选为「かごバス」加古川巴士车辆（OCR「西加古川駅 / 姫路200」），属兵庫県巴士，目标为高知県とさでん交通伊野線/桟橋線鹿児，异县异社且非站景，拦截。
- st03782 伊野駅前 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04544 下天津 接受 c1「File:Shimoamazu Station 20200301.jpg」isc 6.12（替换原错挂图 None）
- st04561 守内かさ神 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04564 椋野 撤图置 missing+bsc：3 张为椋神社鸟居/社殿与湖中鸟居风景，非錦川清流線椋野駅站景，拦截。
- st04575 高水 撤图置 missing+bsc：3 张「Ikusabata Station @ Mount Takamizu hike」为東京都青梅線軍畑駅登山途中的山景/山路，非山陽本線高水駅站景，拦截。
- st04585 柿ケ島 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04602 六条 撤图置 missing+bsc：c1 为 Toyota 86 / Subaru Impreza 汽车店，c2 为神戸六条八幡神社，均非ハピラインふくい線六条駅站景，拦截。
- st04604 山田西町 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04642 豊永 撤图置 missing+bsc：3 张均为歌川国贞等浮世绘锦绘（Recueil d'estampes），非土讃線豊永駅站景，拦截。
- st04643 土佐岩原 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04808 山鼻19条 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04819 西線6条 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st04955 薬水 接受 c1「File:Kusurimizu Station platform in 20150718.jpg」isc 6.65（替换原错挂图 None）
- 合计 ACCEPT 5 / MISSING_BSC 18 / REVIEW 1 / RETRY 0 / NOOP 0；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## ws17 below-spec replace WS17-MISS06 — 2026-11-09T09:09:45Z
- queue: 24 站（review/below_spec 高分替换）
- replaced=4 staged=13 confirmed=7 skipped=0
- reject_dist={"resolution_low_lt_1600": 82, "mime_unsupported": 73, "title_names_other_station": 97, "hard_excluded": 16, "oversize_gt_25mb": 1, "no_author_metadata": 7, "title_non_station_scene": 11, "duplicate_title": 6, "license_unclear": 3, "quality_reject_low_color": 7}


## WS17-MISS06 本地裁决 — 2026-11-09T09:15:47Z（runner 42589960235）
- st05004 自衛隊前 接受 c1「File:Namboku-line Jieitaimae-sta Platform.jpg」isc 6.57（替换原错挂图 None）
- st05086 伊勢鎌倉 保留现状：本轮唯一候选「Meisho-Line Tea-plantation」为名松線沿线茶园风景，非駅景；但该站 state=missing 与 index=done 分歧且仓库实际有现挂 photo，故不撤图、不判 bsc，NOOP 保留现挂图。
- st05087 伊勢八知 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st05169 国見 撤图置 missing+bsc：第四查 3 FLAG（jr_region_mismatch）：c1/c2/c3 均为宮城県 JR 仙山線国見駅（OCR「仙山線 / 愛子・作並・山寺・山形方面 / 仙台方」），目标高知県中村線・宿毛線国見（JR四国/土佐くろしお），同名异县异地区，全部拦截。
- st05277 宇島 保留现状：3 张候选为丰前警察署 / 河口湖鹈岛 / 丰前 IC 高速出入口，均非駅景；该站同属 state/index 分歧且实际有现挂 photo，NOOP 保留现挂图。
- st05365 安芸長浜 撤图置 missing+bsc：唯一候选「USMC-091214-M-1298M-026」为美国海军陆战队人员合影，第一查 foreign 且非駅景，拦截。
- st05908 嵐山 保留现状：runner 已替换并随 c7231438 入库；回读放大为阪急嵐山駅木造站台+复古灯笼，与京都府嵐山本線基线一致，保留。
- st05977 東開聞 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st06053 中福良 撤图置 missing+bsc：3 张均为中福良小学校 / 旧中福良中学校舍，非駅景，拦截。
- st06057 鶴丸 撤图置 missing+bsc：3 张均为「刀剣乱舞 鶴丸国永」cosplay 与加拿大 UFV 大学毕业展合影，站名同音误命中，非駅景，拦截。
- st06247 新西脇 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st06253 青野ケ原 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st06506 新木屋瀬 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st06539 大和田 撤图置 missing+bsc：c1/c2 为北海道留萌本線大和田駅（OCR「JR 大和田駅」），c3 为京阪大和田駅；目标静岡県大井川本線大和田，同名异县异社。且 c1/c2 与 st07190 批内重复同图，全部拦截。
- st06540 大和田 保留现状：runner 已替换并入库；回读为京阪本線大和田駅站前（京阪巴士+蓝色駅名標），与大阪府京阪本線一致，保留。
- st06541 大和田 保留现状：runner 已替换并入库；放大后駅名標两侧为「TD 04」（東武アーバンパークライン/野田線站号）、站内 PASMO ATM，确为埼玉県大和田駅而非京阪大和田，同名簇已辨明，保留。
- st06696 美濃川合 撤图置 missing+bsc：唯一候选「Minokawai power station」为美濃川合发电站/水坝，power station 非 railway station，拦截。
- st06710 扇町 保留现状：runner 已替换并入库；回读为大阪 Metro 堺筋線扇町駅地下站台（屏蔽门+8号車标识），与大阪府基线一致，保留。
- st06754 寿 撤图置 missing+bsc：第四查 FLAG：c1「Fuji-kyuko-Kotobuki」为富士急行寿駅（obs=東武，与 JR 目标冲突）；c2/c3「Cishousi Station」为中国北京地铁慈寿寺站（OCR「To Subway / 10号线」），第一查 foreign。全部拦截。
- st07002 下ノ江 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st07039 吉富 撤图置 missing+bsc：3 张为吉富町役场与 Japan Cup 赛马 paddock 骑师照，非駅景，拦截。
- st07138 東青原 撤图置 missing+bsc：runner confirmed：整批无任何候选回传，确认无可用图。
- st07190 大輪田 撤图置 missing+bsc：候选为留萌本線大和田駅站舍（与 st06539/1 同图）、大阪/京阪大和田站台（与 st06539/2 同图）；目标为奈良県田原本線「大輪田」（非「大和田」），站名亦不符，全部拦截。
- st07456 船岡 撤图置 missing+bsc：3 张为宮城県東北本線船岡駅站台/隧道水路/木造站舍，目标京都府山陰本線船岡，同名异县，全部拦截。
- 合计 ACCEPT 1 / MISSING_BSC 17 / REVIEW 0 / RETRY 0 / NOOP 6；四道门禁 + OCR + GPS + 放大目检后逐条裁决。


## ws17 below-spec replace WS17-MISS07 — 2026-11-09T09:35:28Z
- queue: 20 站（review/below_spec 高分替换）
- replaced=1 staged=9 confirmed=10 skipped=0
- reject_dist={"resolution_low_lt_1600": 65, "title_names_other_station": 63, "duplicate_title": 8, "mime_unsupported": 138, "hard_excluded": 17, "license_unclear": 12, "quality_reject_low_color": 7, "title_non_station_scene": 5, "no_author_metadata": 2, "quality_reject_white_screenshot": 1}

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

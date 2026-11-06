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

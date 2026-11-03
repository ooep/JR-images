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


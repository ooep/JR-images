# JR-images 可复用资产说明（ASSETS）

> 目标：**换一份目标站清单就能直接复跑**。本文件描述抓取/校验流水线、判定规则、
> 断点格式与云端模板。目标站清单是输入参数，任何口径（印章站 / 全站 / 核心站）
> 都走同一条流水线。

## 1. 组件清单

| 文件 | 作用 |
|---|---|
| `scripts/make_station_list.py` | 由源数据生成目标站清单（归并同名站、主键、same_as、线路/客流富化） |
| `scripts/batch_fetch.py` | 核心流水线：Commons 候选 → 许可过滤 → 规格过滤 → 下载 → 数值质检 → 落盘 → 索引/状态 |
| `scripts/verify_local.py` | 批后一致性校验（sha256/尺寸/体积/许可文件/撞图） |
| `.github/workflows/batch-fetch.yml` | 云端 `workflow_dispatch` 模板（runner 上跑整批并提交） |
| `data/stations_<tag>.json` | 目标站清单（可替换输入） |
| `state.json` | 断点续跑状态（逐站写，崩溃/重跑自动跳过已完成站） |
| `index.json` | 顶层索引（站点 → 图/许可/指标，站点数字 ID 为主键） |
| `stations/<slug>/photo.<ext>` | 照片原图（原始字节，不重压缩） |
| `licenses/<slug>.txt` | 每站一份许可档案 |
| `PROGRESS.md` | 每批自动追加的进度块 |

## 2. 目标站清单格式（可替换输入）

`make_station_list.py` 生成，`batch_fetch.py --stations <path>` 消费：

```json
{
  "meta": {"tag": "stamp1089", "source": "stamp_scenes", "canonical": 964,
           "policy": "primary_key=numeric_station_id(1001-10096); ..."},
  "stations": [
    {"id": 1001, "slug": "st01001", "name": "東室蘭駅", "name_key": "東室蘭",
     "name_en": null, "lat": 42.34888, "lon": 141.02543, "pref": "北海道",
     "scene": "雪国/北海道", "lines": ["室蘭線"], "riders": 2730, "same_as": []}
  ]
}
```

两种源口径：

- `--source stamp_scenes`：印章盘点口径（1,089 条记录 → 964 唯一站）。
  主键 = 站点数字 ID（1001–10096），slug `st{id:05d}`；同名站最小 ID 为主，
  其余进 `same_as`（共享一张图 + sha256 去重）。
- `--source station_map`：全站名表口径（8,928 站名）。无数字 ID，按站名排序
  分配 900001+ 临时 ID（`st%06d`），**最终口径待全集对账后可整体替换**。

`--geojson` 可选：从主站 `stations.geojson`（8,532 站）合并线路与客流，
将来"核心站优先"口径可直接按 `riders` 排序切片。

## 3. 许可判定规则（硬纪律）

只收许可清晰的图，逐张在 `licenses/<slug>.txt` 记录
作者 / 许可名 / 许可 URL / 原页面 URL / 抓取时间 / sha256：

- **允许**（Commons `extmetadata.LicenseShortName` 归一化后匹配）：
  `CC0`、`CC BY x.x`、`CC BY-SA x.x`、`Public domain`、`No restrictions`。
- **拒收**：含 `NC` / `ND` / `GFDL` 的；许可字段缺失的；无法归类的（`license_unclear`）。
- **署名完整性**：`CC BY*` 必须能取到作者（`Artist`），否则拒收（`no_author_metadata`）；
  CC0/PD 允许无作者。
- 许可不清 → 该候选拒收并计入拒因分布；全站无可用候选 → 状态 `missing` + 原因，
  绝不收图抵赖。

## 4. 构图/主体判定规则（数值化，无 AI、无图片类工具）

先硬规格，后数值质检（在长边缩到 1024 的副本上计算，Pillow+numpy）：

| 指标 | 拒收阈值 | 存疑(review)阈值 | 含义 |
|---|---|---|---|
| 原图长边 | <1600px | — | 不够清晰就找更大原图，不放大 |
| 文件体积 | >25MB | — | 超限选次优，不压缩抵赖 |
| 拉普拉斯方差 | <45 | <75 | 清晰度（模糊拒收） |
| 色彩丰富度(Hasler-Süsstrunk) | <18 | <25 | 过低=地图/文字/灰度图嫌疑 |
| 纯白占比(灰度>245) | >0.55 | >0.42 | 过高=文字/截图嫌疑 |
| 边缘密度<0.03 且色彩>90 | — | map_like | 地图/图形嫌疑 |

**车站本体判定**（教训：旧批把「広島港・宇品」配了车厢内部照）：

- 候选来自该站的 Commons 分类（Category:X駅 / X Station / Wikidata P373）
  → 分类本身即主题证据；
- 候选来自自由文本搜索 → 文件名必须含车站关键词（駅/station/eki/駅舎/ホーム/改札…），
  否则标 `subject_unverified`；
- 文件名含车厢内部关键词（車内/interior/運転台/rolling stock…）且无车站关键词
  → 标 `subject_doubtful`；
- 任何存疑标记 → 状态 `review`（文件保留待人工复核，但不算合格命中，
  站点前端只应使用 `status=done` 的图）。**不硬塞。**

候选排序：分类来源 +2、站名关键词 +2、车厢关键词 −3、分辨率加成（上限 +3）、
JPEG +0.5。按分取前 `--max-download`（默认 5）张逐张下载验证，
遇到第一张全绿的即采用；全带存疑标记则取分最高者标 `review`。

## 5. state.json 断点格式

```json
{
  "schema": 1,
  "stations_path": "data/stations_stamp1089.json",
  "batch_index": 0, "batch_size": 500, "updated_at": "…Z",
  "entries": {
    "st01001": {
      "status": "done|review|missing|failed",
      "attempts": 1, "ts": "…Z",
      "file": "stations/st01001/photo.jpg", "sha256": "…", "bytes": 123,
      "width": 2400, "height": 1600,
      "license": "CC BY-SA 4.0", "reasons": [], "reject_dist": {"license_unclear": 3}
    }
  }
}
```

- 每处理完一站立即原子写盘（`tmp`+`rename`），崩溃不丢进度；
- 重跑时 `done`/`review` 自动跳过（`skipped_resume` 计数）；
- `missing`/`failed` 站重跑会重试（用于补充候选策略后二次打捞）。

## 6. 云端模板（.github/workflows/batch-fetch.yml）

- `workflow_dispatch` 输入：`batch_index`、`batch_size`（默认 500）、
  `stations_path`（默认 `data/stations_stamp1089.json`，**可换成任何清单**）；
- runner：ubuntu-latest，`pip install pillow numpy requests`；
- 跑 `batch_fetch.py` → `verify_local.py` → `git add/commit/push`
  （GITHUB_TOKEN，`force:false`，冲突 `pull --rebase` 重试 3 次）；
- 统计走 artifact（`batch-<N>-stats`），进度追加进仓库内 `PROGRESS.md`；
- 图片只在 runner 流转，**本地磁盘不碰图**。

触发示例（令牌走 `git credential fill` → 环境变量 → `curl --config -` stdin）：

```
POST /repos/ooep/JR-images/actions/workflows/batch-fetch.yml/dispatches
{"ref":"main","inputs":{"batch_index":"0","batch_size":"500",
 "stations_path":"data/stations_stamp1089.json"}}
```

## 7. 速率与纪律

- 单域名并发 ≤2、相邻请求间隔 ≥1.05s（`DomainLimiter` 强制），429 按
  `Retry-After` 退避；明确 UA（含仓库地址与用途）；只走公开 API，不绕鉴权；
- 临时下载在 `.tmp_fetch/`，批结束由调用方清理（云端随 runner 销毁）；
- 本地回落跑法：同一脚本 `--workdir <repo checkout>`，磁盘闸门
  （可用 <8GB 或预估总量 >3GB 即停）由调度方监控。

## 8. 换口径复跑步骤（SOP）

1. 拿到新口径源数据 → `python scripts/make_station_list.py --source … --tag <新tag> --out data/stations_<新tag>.json`；
2. 推清单进仓库（Git Data API，`force:false`）；
3. `workflow_dispatch` 触发，`stations_path` 指向新清单，`batch_size` 按需；
4. 每批跑完看 `PROGRESS.md` + artifact；`missing` 站攒到批末统一处置；
5. 全部完成后跑 `verify_local.py` 总校验，README 注明旧批次替换情况。

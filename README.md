# JR-images

日本铁路车站高清照片仓库（试点阶段）。目标：为 [jr.suki.ing](https://jr.suki.ing) 收录的全部 **8,928 个车站**每站收集一张可公开再分发的高清照片；当前为 **500 站试点**。

## 方案参数（试点）

| 项 | 值 |
|---|---|
| 图片规格 | 长边 **1200px**，JPEG，质量 82；单张 ≤ **400 KB**（超出则自动降质量至达标，manifest 记录实际值） |
| 目录 | `img/<都道府县>/<station_id>.jpg`（县目录为 JIS 码+县名，如 `13_東京都`；无县信息归 `99_その他`） |
| 命名 | 稳定 `station_id`（`st00001`…`st08928`，全站映射见 `data/station_ids.json`），**不用站名** |
| 索引 | `manifest.json` 每站一条；缺图记 `"file": null` + `reason` |
| 许可 | **白名单只收** CC0 / Public domain / CC-BY / CC-BY-SA；其余一律拒收 |

## 许可与署名

- 只收录许可可验证（`LicenseShortName` + `Artist` 元数据齐全）的图片；作者缺失视为不合规并拒收。
- 每图的署名信息（`author` / `license` / `license_url` / `source_url`）同时记录在 `manifest.json`，供页面展示按 TASL 格式渲染：`「标题」 by 作者, via Wikimedia Commons, 许可`。
- CC-BY-SA 图片的衍生作品（本仓库的缩放/转码版本）继续以 CC-BY-SA 提供。

## 仓库结构

```
├── .github/workflows/pilot-fetch.yml   # 抓取流水线（GitHub Actions 内运行）
├── scripts/fetch_commons.py            # 检索→许可校验→下载→重编码→提交（可断点续跑）
├── scripts/validate_manifest.py        # manifest ↔ 图片一致性校验（sha256/尺寸/体积/许可）
├── data/station_ids.json               # 全部 8928 站的稳定 id 映射
├── data/pilot500.json                  # 试点 500 站（县分层 + 半高价值半随机）
├── data/pref_codes.json                # 都道府县 JIS 码 / 目录 slug
├── manifest.json                       # 主索引（每站一条）
├── reports/pilot_report.{json,md}      # 验收报告（覆盖率/合规率/体积分布/失败分类）
└── img/<pref>/<station_id>.jpg
```

## 运行方式

抓取在 **GitHub Actions** 中执行（本地网络不可达上游图站）：

1. Actions → `pilot-fetch` → Run workflow；
2. 工作流逐站处理，**每 50 站自动提交一次**，中断后重新运行会跳过已完成站（断点续跑）；
3. 结束前做全量一致性自检（sha256/尺寸/体积/许可），通过后才最终提交；
4. 工作流末尾再跑一次独立校验门槛（`validate_manifest.py`）。

日志脱敏：运行日志不出现上游域名/接口。

## 验收标准（试点）

- 覆盖率 ≥ 85%（有图站 / 500）；
- 许可合规率 = 100%（每张入库图的 `license` 与 `author` 均可验证）；
- 单张 ≤ 400 KB，报告给出 p50 / p95 / max；
- manifest 字段完整、sha256 全局唯一。

## 全量计划（仅计划，暂不执行）

试点验收通过后，按每周约 1,000 站、共 9 批的节奏扩展到全部 8,928 站：

1. 批序按县站数从多到少（东京 → 大阪 → 爱知 → 北海道 → …）；
2. 每批一次 workflow 运行 + 一次验收报告；
3. `station_map` 更新产生的新站走增量队列（manifest 中 `file: null` 的站优先补齐）；
4. 全量完成后评估仓库体积，若超过 GitHub 建议的 1 GB 再讨论分仓或对象存储迁移。

## 状态

- 2026-11-03：**试点 500 站完成**。覆盖率 100%（500/500），许可合规率 100%，无重复图、无缺图。
  - 体积：总 94.0 MB；p50=190 KB / p95=296 KB / max=399 KB（均 ≤400 KB）。
  - 许可分布：CC-BY-SA-4.0 ×274、CC-BY-3.0 ×46、CC0 ×45、CC-BY-4.0 ×43、CC-BY-SA-3.0 ×34、CC-BY-SA-2.0 ×21、PD ×17、CC-BY-2.0 ×14、CC-BY-2.5 ×6。
  - 本地独立复验（逐张拉取核对 sha256/尺寸/体积/格式）：0 问题。
  - 详见 `reports/pilot_report.json`。

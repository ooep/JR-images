# PIPELINE 台账（按 commit 的性质）

一条改动一个性质。本台账按 sha 记录每笔 commit 的实际内容，避免把不同性质的改动合并记账。

## 更正记录（审计指出的三笔）

| sha | 实际性质 | 实际内容 |
|---|---|---|
| `a68cff68` | 选图代码补丁 | 站点风景选图（hard-exclude + 评分排序 + sha/title 去重 + final_dead），**不是地理闸门** |
| `8587b12d` | 数据回填 | 为 2,456 张已推图回填 dHash + 29 条近重复二次副本入重抓队列，**不是地理闸门** |
| `a53d3c40` | 地理闸门（唯一一笔） | `geo-audit.yml` + `scripts/batch_fetch.py`（>20km 拒、同名簇 >10km 拒）+ `scripts/geo_audit.py` 回溯体检 |

## 全量台账（新→旧）

| sha | 日期 | 性质 | 一句话内容 |
|---|---|---|---|
| 157b9205 | 11-04 | data | batch 5 图像组 23（累计 2300 站） |
| ab672bf9 | 11-04 | data | batch 5 图像组 22 |
| abf665ed | 11-04 | data | batch 5 图像组 21 |
| 8b368d70 | 11-04 | data | batch 5 图像组 20 |
| 9ff0e24f | 11-04 | data | batch 5 图像组 19 |
| 1fc1f25f | 11-04 | data | batch 5 图像组 18 |
| 4671b7eb | 11-04 | data | batch 5 图像组 2 |
| 919a1eaa | 11-04 | data | batch 5 图像组 1 |
| 76913c1e | 11-04 | data | batch 5 元数据（state/index/progress/stats/dead） |
| 8ca1ddb6 | 11-04 | patch | 站名判据只计数不硬拒（误杀待核 18.8%>2%）；县名+地理硬拒 |
| 0542ec6b | 11-04 | patch | 县名/站名判据加固（罗马字长音不敏感、JR 前缀、线路名白名单） |
| 63b13405 | 11-04 | patch | rules-audit 为无 source_title 的老条目从 source URL 反推标题 |
| 8b3f6c86 | 11-04 | patch | 县名/站名硬判据（不依赖坐标）+ rules-audit 回溯 + 7 错配站入重抓队列 |
| a53d3c40 | 11-04 | patch | 地理闸门（见更正记录） |
| 8587b12d | 11-03 | data | dHash 回填 2,456 图 + 29 近重复重抓队列（见更正记录） |
| f17c93e4 | 11-03 | patch | sha-audit 安装 pillow 以跑 dHash 通道 |
| 97177f14 | 11-03 | patch | maxlag 是服务器延迟非限流：等待+重试、不熔断（run #10 复盘） |
| 2fbc56bd | 11-03 | patch | 合规提速（串行 API + maxlag=5、下载层 x2 + 熔断）、限流计数 |
| 3c0e4fe1 | 11-03 | data | batch 4 图像组 18 |
| 345fdc37 | 11-03 | data | batch 4 图像组 17 |
| 9dc2058d | 11-03 | data | batch 4 图像组 16 |
| bb92bb6c | 11-03 | data | batch 4 图像组 15 |
| d4209ba4 | 11-03 | data | batch 4 图像组 14 |
| 104d4083 | 11-03 | data | batch 4 图像组 13 |
| 1054a17c | 11-03 | data | batch 4 图像组 12 |
| 363cc8de | 11-03 | data | batch 4 图像组 6 |
| f8abb489 | 11-03 | data | batch 4 图像组 5 |
| 60a64a68 | 11-03 | data | batch 4 图像组 4 |
| 979df2d1 | 11-03 | data | batch 4 图像组 2 |
| 579f6b25 | 11-03 | data | batch 4 元数据 |
| 6de04664 | 11-03 | patch | rebase-safe push（stash）、元数据失败回退、重复图复检不加 attempts |
| 38ba4834 | 11-03 | data | batch 3 图像组 12 |
| fd8ce272 | 11-03 | data | batch 3 图像组 11 |
| e6b07a61 | 11-03 | data | batch 3 图像组 10 |
| 93dfdcac | 11-03 | data | batch 3 图像组 9 |
| ed0ce297 | 11-03 | data | batch 3 图像组 8 |
| 3a273b87 | 11-03 | data | batch 3 图像组 7 |
| 7b733b95 | 11-03 | data | batch 3 图像组 6 |
| d46bb3d6 | 11-03 | data | batch 3 图像组 1 |
| 2f832d0a | 11-03 | data | batch 3 元数据 |
| a68cff68 | 11-03 | patch | 选图评分/去重补丁（见更正记录） |
| 16812421 | 11-03 | patch | 同上（重推） |
| bb3e865a | 11-03 | data | batch 2 图像组 10 |
| 1612c70b | 11-03 | data | batch 2 图像组 6 |
| 333d3f69 | 11-03 | data | batch 2 图像组 5 |
| 038ee80e | 11-03 | data | batch 2 图像组 4 |
| 6557f196 | 11-03 | data | batch 2 图像组 3 |
| eeff53ee | 11-03 | data | batch 2 图像组 2 |
| 5ad8fdba | 11-03 | data | batch 2 图像组 1 |
| 092afcad | 11-03 | data | batch 2 元数据 |
| e198cea8 | 11-03 | data | batch 1 图像组 10（尾组） |
| 8ebb8026 | 11-03 | data | batch 1 图像组 9 |
| 871544df | 11-03 | data | batch 1 图像组 8 |
| 530a58be | 11-03 | data | batch 1 图像组 7 |
| 3bc1161b | 11-03 | data | batch 1 图像组 6 |
| dea82ffa | 11-03 | data | batch 1 图像组 1 |
| e7e2daea | 11-03 | data | batch 1 元数据 |
| 420cc7b5 | 11-03 | pipeline | 归一化改 1800px/q85（体积 -30%）+ dead 重试/校验入册 + 质检失败不静默 |
| b0a636a9 | 11-03 | data | batch 0 图像组 5（尾组） |
| 1da8b161 | 11-03 | data | batch 0 图像组 4 |
| 3cb5e008 | 11-03 | data | batch 0 图像组 3 |
| fe59e89e | 11-03 | data | batch 0 图像组 2 |
| d0653fbb | 11-03 | data | batch 0 图像组 1 |
| e5442d80 | 11-03 | data | batch 0 元数据 |
| 1756b4e3 | 11-03 | workflow | 修复重复 env 键 |
| 8bc26953 | 11-03 | pipeline | 归一化 2048 + 分块推送（100 站/块）+ 自动派发下一批 |
| a29d2d2f | 11-03 | patch | 分类猜测使用 name_en（Category:X Station） |
| eae97e9f | 11-03 | fullset | stations_all.json（8,909 物理站，C 优先）+ 顺序执行 + universe 源 + i18n |
| ca5fd0c5 | 11-03 | assets | 可复用流水线（抓取/校验/推送）+ workflow 模板 + stamp1089 清单 + legacy 索引 |
| 1a363562 | 11-03 | docs | 更新试点完成状态（500/500） |
| b7c26a87 | 11-03 | pilot | 试点完成 500 站（500 图） |
| 628bed88 | 11-03 | pilot | 试点 500/500 处理 |
| 49b7d365 | 11-03 | pilot | 试点 450/500 |
| 816a80e1 | 11-03 | pilot | 试点 400/500 |
| 10910803 | 11-03 | pilot | 试点 350/500 |
| 1f670b10 | 11-03 | pilot | 试点 300/500 |
| b1e69b92 | 11-03 | pilot | 试点 250/500 |
| 150ddeb4 | 11-03 | pilot | 试点 200/500 |
| 00d2a9a9 | 11-03 | pilot | 试点 150/500 |
| 28d06ff5 | 11-03 | pilot | 试点 100/500 |
| 80986e94 | 11-03 | pilot | 试点 50/500 |
| d2b283fa | 11-03 | fix | 许可串归一化（CC BY-SA 4.0 空格写法）+ 撞图规避/重试 + 被拒许可审计 |
| d8a469d9 | 11-03 | pilot | 试点首轮完成 500 站（392 图） |
| 7ed86579 | 11-03 | pilot | 试点首轮 500/500 处理 |
| 32498a4e | 11-03 | pilot | 试点首轮 450/500 |
| 4f3cf6d8 | 11-03 | pilot | 试点首轮 400/500 |
| a40bef94 | 11-03 | pilot | 试点首轮 350/500 |
| 75f0b0d7 | 11-03 | pilot | 试点首轮 300/500 |
| 74db8f68 | 11-03 | pilot | 试点首轮 250/500 |
| 81d5e424 | 11-03 | pilot | 试点首轮 200/500 |
| d0910e9c | 11-03 | pilot | 试点首轮 150/500 |
| 77659c50 | 11-03 | pilot | 试点首轮 100/500 |
| e071d9b0 | 11-03 | pilot | 试点首轮 50/500 |
| 263462cc | 11-03 | fix | 批次提交只 add 已存在目录（reports 末尾才生成） |
| 251d398f | 11-03 | init | 仓库骨架：试点 500 站抓取流水线 + 稳定 id + manifest schema |

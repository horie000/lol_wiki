---
title: Riotランク戦試合データ：試合時間帯別チャンピオン勝率
type: source
status: active
source_path: raw/sources/riot-ranked-matches
ingested: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
tags:
  - league-of-legends
  - ranked-match
  - descriptive-statistics
---

# Riotランク戦試合データ：試合時間帯別チャンピオン勝率

## 要約

`raw/sources/riot-ranked-matches/` に収集されたLeague of Legendsのランク戦Match-v5データを、キュー420（ランク戦）に限定して集計した。2024-09-25から2026-09-14までの4,677ファイル、6,672レコードを読み込み、同一試合IDを統合した結果、4,672件の完全試合を得た。

この要約では、試合時間を「〜20分」「20〜25分」「25〜30分」「30〜35分」「35分〜」に分け、チャンピオンごとの勝率を比較した。分析実行の詳細なCSV・JSON・Markdownレポートは、`reports/riot-ranked-match-analysis/run-20260915T010911Z/` に保存している。

## 主要な観測

- 試合時間の中央値は29分18秒、P10〜P90は16分48秒〜39分45秒だった。
- 時間帯別の試合数は、〜20分758、20〜25分665、25〜30分1,084、30〜35分1,091、35分〜1,074だった。
- 各時間帯15試合以上を満たすチャンピオンについて、最も勝率が高い帯と端点との差が8ポイント以上ある場合に、序盤寄り・中盤寄り・終盤寄りとして整理した。
- 173チャンピオンの内訳は、序盤寄り11、中盤寄り22、終盤寄り14、明瞭な傾向なし75、分母不足51だった。

## データ品質と限界

2,000件の重複レコードは試合ID単位で統合し、競合する試合本体は0件、完全試合でない試合は0件だった。観測ランク帯の重複を避けるため `tier_mode=all` としたが、観測ランク帯は試合時点の全参加者のランクではない。

データは48パッチ、複数ロール、複数の収集経路を含む。試合時間は勝敗後に確定するため、時間帯別勝率はパワースパイクの因果効果、購入時点の強さ、または推奨ビルドを示さない。Timelineデータがないため、15分時点のゴールド差、レベル到達、購入時刻、スタック獲得速度も復元していない。

## 派生分析：ロール別ゴールド獲得率

同じ `raw/sources/riot-ranked-matches/` を後続スナップショットで再集計し、9,971件の完全試合について `goldEarned / (timePlayed / 60)` をロール別に比較した。平均GPMはBOTTOM 423.4、JUNGLE 405.1、MIDDLE 384.1、TOP 384.0、UTILITY 291.2で、チーム内の最終ゴールド比率もBOTTOM 22.4%、UTILITY 15.5%などの差を示した。この結果は、時間帯別勝率をロール混合のまま読む際の資源配分上の交絡を確認するための派生分析であり、既存の4,672試合のパワースパイク分類を置き換えない。

## 関連ページ

- [[wiki/syntheses/champion-power-spikes-match-duration|チャンピオンのパワースパイク：試合時間帯別勝率の見直し]] — 原典ベースの分類と実戦データの観測を分けて統合する。
- [[wiki/syntheses/role-gold-acquisition-rate|ロール別ゴールド獲得率：ランク戦最終スコアの集計]] — 最終ゴールド/分とチーム内配分を、パワースパイク分析の交絡確認として整理する。
- [[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]] — Data Dragon由来の能力シグナルによる既存分類。

## 未解決の問い

- パッチとロールを固定した場合にも、同じ時間帯傾向が再現するか。
- Timelineデータを用いて、勝敗ではなく一定時点のゴールド・経験値・装備完成と関連付けられるか。
- 観測ランク帯別に分けた場合、全体集計で見える傾向が維持されるか。

## 出典

- 原典：[[raw/sources/riot-ranked-matches|riot-ranked-matches]]
- 解析レポート：`reports/riot-ranked-match-analysis/run-20260915T010911Z/report.md`
- 解析条件：`reports/riot-ranked-match-analysis/run-20260915T010911Z/manifest.json`
- 派生ロール別解析：`reports/riot-ranked-match-analysis/run-20260915T061543Z/report.md`
- 派生解析条件：`reports/riot-ranked-match-analysis/run-20260915T061543Z/manifest.json`

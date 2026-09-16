---
title: Riotランク戦試合データ：観測ランク帯別特徴
type: source
status: active
source_path: raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - league-of-legends
  - ranked-match
  - tier-analysis
  - descriptive-statistics
---

# Riotランク戦試合データ：観測ランク帯別特徴

## 要約

`raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5/` に保存された、IRON、BRONZE、SILVER、GOLD、PLATINUM、EMERALD、DIAMOND、MASTER、GRANDMASTER、CHALLENGERの各 `matches.jsonl` を、キュー420に限定して比較した。10帯の各1,000レコード、合計10,000レコードを読み込み、同一試合IDを統合した結果、9,761件のユニーク試合を得た。完全試合は9,761件、不完全試合と競合する試合本体は0件だった。

これは試合結果を収集時の観測ランク帯ごとに比較する派生分析である。`observed_tier` は、その試合を発見したプレイヤーの収集時点の所属帯であり、試合に参加した10人全員の試合時ランクではない。

## 主要な観測

- 観測帯ごとの試合時間中央値は26分52秒（CHALLENGER）から29分59秒（GOLD）だった。IRONは28分33秒だった。
- 平均GPMはIRON 373.6からGRANDMASTER 420.7、CHALLENGER 420.4、平均CS/分は5.19から6.12へ増えた。ただし、これは最終 `goldEarned` と `timePlayed` からの記述統計である。
- 各帯で173チャンピオンが少なくとも一度登場したが、全帯のピック数上位10件に共通するチャンピオンはなかった。
- すべての帯で、ロール別の最終GPMはBOTTOMが最高、UTILITYが最低だった。UTILITYはCS/分が低く、視界スコアが高いという構造も共通した。
- 全帯のキーストーン上位5に共通して入るのは、征服者、リーサルテンポ、秘儀の彗星、電撃だった。サモナースペル構成上位5には、フラッシュ＋イグナイト、フラッシュ＋スマイト、フラッシュ＋テレポート、フラッシュ＋バリア、フラッシュ＋ヒールが共通して入った。

## データ品質と限界

入力は20ファイル（各帯のmanifestとmatches.jsonl）で、10件のmanifest JSONは試合本体ではないため無視した。同じ試合IDの重複レコードは239件あり、観測帯をまたいで重複する試合は229件だった。帯別比較では同一試合を観測された各帯へ一度ずつ割り当てるため、帯ごとの試合は独立ではない。

データの取得期間は帯によって異なり、全体では2026-01-27〜2026-09-15、含まれるパッチ数も帯ごとに5〜17だった。パッチ、プレイヤー、チャンピオン構成、試合時間を調整していないため、観測帯の差を技能差やランクの因果効果として解釈できない。Timelineデータがないため、固定時点のゴールド・経験値・購入時刻・イベント進行は含めていない。

## 関連ページ

- [[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]] — 観測帯ごとの特徴、共通構造、追加の解釈を統合する。
- [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate|Riotランク戦試合データ：試合時間帯別チャンピオン勝率]] — 同じ収集系統の試合時間分析。
- [[wiki/sources/src-2026-09-15-riot-ranked-match-role-gold-share|Riotランク戦試合データ：ロール別ゴールド獲得シェア]] — 最終ゴールドのロール内配分を詳しく扱う。

## 出典

- 原データ：[[raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5|ranked-solo-5x5]]
- 解析スクリプト：`scripts/riot_ranked_tier_analyzer.py`
- 解析仕様：`docs/riot-ranked-match-analysis-spec.md`（観測ランク帯別比較）
- 解析レポート：`reports/riot-ranked-tier-analysis/run-20260916T083219Z/report.md`
- 解析条件：`reports/riot-ranked-tier-analysis/run-20260916T083219Z/manifest.json`
- 品質情報：`reports/riot-ranked-tier-analysis/run-20260916T083219Z/quality.json`

---
title: アイテム金銭効率の基準単価
type: synthesis
status: active
created: 2026-09-15
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency]]"
  - "[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency]]"
tags:
  - league-of-legends
  - item
  - gold-efficiency
---

# アイテム金銭効率の基準単価

## 問い

アイテムの金銭効率を計算する際、各ステータスを何ゴールドとして換算するか。

## 結論

金銭効率は、アイテムの基礎ステータスを「1単位あたりのゴールド価値（gold/stat）」へ換算した理論価格を、実購入価格で割って求める比較指標である。

```text
理論価格 = Σ（ステータス量 × 基準単価）
金銭効率 = 理論価格 ÷ 実購入価格 × 100
```

以下は、このWikiの現行算定に採用している基準単価である。割合ステータスはすべて1%あたりの値である。基準単価そのものと、計算後の「金銭効率（%）」は別の概念である。

## 現行の基準単価

| 分類 | ステータス | 1単位あたりの価値 | 根拠 |
| --- | --- | ---: | --- |
| 攻撃 | 攻撃力 | 35G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 魔力 | 20G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 攻撃速度 | 25G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | クリティカル率 | 40G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | ライフスティール | 53.57G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 脅威 | 30G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 物理防御貫通（割合） | 41.67G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 魔法防御貫通（割合） | 46.15G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 魔法防御貫通（固定） | 46.67G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 攻撃 | 固定通常攻撃時追加ダメージ | 25G / 1ダメージ | [[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency\|FirstBloodStats]]（補助根拠） |
| 防御・資源 | 体力 | 2.67G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 防御・資源 | マナ | 1G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 防御・資源 | 物理防御 | 20G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 防御・資源 | 魔法防御 | 20G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 防御・資源 | 基本体力自動回復 | 3G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 防御・資源 | 基本マナ自動回復 | 4G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| 防御・資源 | 行動妨害耐性 | 10.33G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| ユーティリティ | スキルヘイスト | 50G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| ユーティリティ | 移動速度（固定） | 12G | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| ユーティリティ | 移動速度（割合） | 62.5G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |
| ユーティリティ | 回復効果・シールド量 | 50G / 1% | [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency\|レッド＆ふぉー]] |

## 算定例

計算によると、行動妨害耐性20%の理論価格は `20 × 10.33 = 206.60G` である。攻撃力50の理論価格は `50 × 35 = 1,750G` である。両方を持つアイテムなら、ほかの算定対象ステータスも同様に合算してから実購入価格で割る。

## 根拠と不確実性

- 現行の主要な基準単価は、パッチ26.4を前提とした[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|レッド＆ふぉーの記事]]に基づく。アイテム個別ページはData Dragon v16.18.1を原典にしているため、両者の版・アイテム状態には差があり得る。
- 固定通常攻撃時追加ダメージだけは、現行記事に単価がないため、[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|FirstBloodStatsの記事]]の25Gを補助的に使う。
- クリティカルダメージ、オムニヴァンプ、アルティメットヘイスト、条件付き・動的な固有効果や発動効果には、現行の根拠資料で直接適用できる単価がないため含めない。
- 100%未満のアイテムが弱い、または100%超のアイテムが常に強いとは限らない。これは基礎ステータス部分の比較であり、固有効果、状況、チャンピオンとの相性は別途評価する必要がある。

## 関連ページ

- [[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]] — 算定対象となる868件のアイテム個別ページ。
- [[wiki/syntheses/gold-efficiency-high-low-examples|アイテム金銭効率の高低例と総合評価]] — サモナーズリフトで購入できるアイテムの上位・下位10例と、効果を含めた解釈。
- [[wiki/entities/items/item-3053|ステラックの籠手]] — 行動妨害耐性20%を含む算定例。
- [[wiki/entities/items/item-3036|ドミニク リガード]] — 割合物理防御貫通を含む算定例。

## 未解決の問い

- 現行ゲーム仕様に対応した、クリティカルダメージ、オムニヴァンプ、アルティメットヘイストの再現可能な基準単価は何か。
- Data Dragon v16.18.1とパッチ26.4の差分を、金銭効率の比較にどこまで反映すべきか。

## 出典

- [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|アイテムの金銭効率ランキング：ファイター編【LoL】]] — 現行の主要な基準単価。
- [[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|アイテムのゴールド効率について改めてまとめた]] — 固定通常攻撃時追加ダメージの補助単価と指標の説明。

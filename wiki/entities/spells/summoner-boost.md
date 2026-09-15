---
title: "クレンズ（SummonerBoost）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerBoost"
spell_key: "1"
spell_name: "クレンズ"
data_version: "16.18.1"
modes:
  - "ARAM"
  - "TUTORIAL"
  - "KIWI"
  - "ULTBOOK"
  - "FIRSTBLOOD"
  - "SWIFTPLAY"
  - "CLASSIC"
  - "PRACTICETOOL"
  - "RUBY"
  - "RUBY_TRIAL_1"
  - "BRAWL"
  - "URF"
  - "KIWI_JADE"
  - "RUBY_TRIAL_3"
  - "ONEFORALL"
  - "ARSR"
  - "NEXUSBLITZ"
  - "DOOMBOTSTEEMO"
  - "RUBY_TRIAL_2"
---

# クレンズ（SummonerBoost）

## 概要

- **日本語名：** クレンズ
- **レコードID：** `SummonerBoost`
- **キー：** `1`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード（特殊モード: ULTBOOK）

## 効果

行動妨害(サプレッションとノックアップを除く)やサモナースペルによるデバフをすべて解除し、行動妨害耐性が増加する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
行動妨害系デバフ(<keyword>サプレッション</keyword>と<keyword>ノックアップ</keyword>を除く)やサモナースペルによるデバフをすべて除去し、{{ tenacityduration }}秒間、行動妨害耐性が{{ tenacityvalue*100 }}増加する。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `ARAM`、`TUTORIAL`、`KIWI`、`ULTBOOK`、`FIRSTBLOOD`、`SWIFTPLAY`、`CLASSIC`、`PRACTICETOOL`、`RUBY`、`RUBY_TRIAL_1`、`BRAWL`、`URF`、`KIWI_JADE`、`RUBY_TRIAL_3`、`ONEFORALL`、`ARSR`、`NEXUSBLITZ`、`DOOMBOTSTEEMO`、`RUBY_TRIAL_2` |
| 解禁レベル | 9 |
| 最大ランク | 1 |
| クールダウン | 240（cooldownBurn: `240`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 200（rangeBurn: `200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerBoost.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerBoost` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

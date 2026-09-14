---
title: "フラッシュ（SummonerFlash）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
  - data-dragon
spell_id: "SummonerFlash"
spell_key: "4"
spell_name: "フラッシュ"
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
  - "WIPMODEWIP4"
  - "URF"
  - "SNOWURF"
  - "KIWI_JADE"
  - "RUBY_TRIAL_3"
  - "ONEFORALL"
  - "ARSR"
  - "NEXUSBLITZ"
  - "DOOMBOTSTEEMO"
  - "RUBY_TRIAL_2"
---

# フラッシュ（SummonerFlash）

## 概要

- **日本語名：** フラッシュ
- **レコードID：** `SummonerFlash`
- **キー：** `4`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード（特殊モード: ULTBOOK、SNOWURF）

## 効果

自身のチャンピオンを短い距離、指定した方向に瞬間移動させる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自身のチャンピオンを短い距離、指定した方向に瞬間移動させる。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `ARAM`、`TUTORIAL`、`KIWI`、`ULTBOOK`、`FIRSTBLOOD`、`SWIFTPLAY`、`CLASSIC`、`PRACTICETOOL`、`RUBY`、`RUBY_TRIAL_1`、`BRAWL`、`WIPMODEWIP4`、`URF`、`SNOWURF`、`KIWI_JADE`、`RUBY_TRIAL_3`、`ONEFORALL`、`ARSR`、`NEXUSBLITZ`、`DOOMBOTSTEEMO`、`RUBY_TRIAL_2` |
| 解禁レベル | 7 |
| 最大ランク | 1 |
| クールダウン | 300（cooldownBurn: `300`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 425（rangeBurn: `425`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerFlash.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerFlash` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

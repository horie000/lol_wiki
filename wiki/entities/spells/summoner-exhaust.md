---
title: "イグゾースト（SummonerExhaust）"
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
spell_id: "SummonerExhaust"
spell_key: "3"
spell_name: "イグゾースト"
data_version: "16.18.1"
modes:
  - "URF"
  - "PRACTICETOOL"
  - "CLASSIC"
  - "ULTBOOK"
  - "DOOMBOTSTEEMO"
  - "ARAM"
  - "RUBY_TRIAL_3"
  - "NEXUSBLITZ"
  - "SWIFTPLAY"
  - "ONEFORALL"
  - "TUTORIAL"
  - "RUBY"
  - "WIPMODEWIP"
  - "RUBY_TRIAL_2"
  - "WIPMODEWIP3"
  - "RUBY_TRIAL_1"
  - "ARSR"
---

# イグゾースト（SummonerExhaust）

## 概要

- **日本語名：** イグゾースト
- **レコードID：** `SummonerExhaust`
- **キー：** `3`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード（特殊モード: ULTBOOK）

## 効果

敵チャンピオンにスロウ効果を付与し、与ダメージを低下させる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
敵チャンピオンに{{ slow }}%の<keyword>スロウ効果</keyword>を付与し、{{ debuffduration }}秒間にわたって与ダメージを{{ damagereduction }}%低下させる。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `URF`、`PRACTICETOOL`、`CLASSIC`、`ULTBOOK`、`DOOMBOTSTEEMO`、`ARAM`、`RUBY_TRIAL_3`、`NEXUSBLITZ`、`SWIFTPLAY`、`ONEFORALL`、`TUTORIAL`、`RUBY`、`WIPMODEWIP`、`RUBY_TRIAL_2`、`WIPMODEWIP3`、`RUBY_TRIAL_1`、`ARSR` |
| 解禁レベル | 4 |
| 最大ランク | 1 |
| クールダウン | 240（cooldownBurn: `240`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 650（rangeBurn: `650`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerExhaust.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerExhaust` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

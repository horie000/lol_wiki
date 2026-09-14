---
title: "バリア（SummonerBarrier）"
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
spell_id: "SummonerBarrier"
spell_key: "21"
spell_name: "バリア"
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
  - "ASSASSINATE"
  - "ARSR"
  - "NEXUSBLITZ"
  - "DOOMBOTSTEEMO"
  - "RUBY_TRIAL_2"
---

# バリア（SummonerBarrier）

## 概要

- **日本語名：** バリア
- **レコードID：** `SummonerBarrier`
- **キー：** `21`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード（特殊モード: ULTBOOK）

## 効果

一時的にシールドを獲得する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
{{ shieldduration }}秒間、<shield>耐久値{{ shieldstrength }}のシールド</shield>を獲得する。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `ARAM`、`TUTORIAL`、`KIWI`、`ULTBOOK`、`FIRSTBLOOD`、`SWIFTPLAY`、`CLASSIC`、`PRACTICETOOL`、`RUBY`、`RUBY_TRIAL_1`、`BRAWL`、`URF`、`KIWI_JADE`、`RUBY_TRIAL_3`、`ONEFORALL`、`ASSASSINATE`、`ARSR`、`NEXUSBLITZ`、`DOOMBOTSTEEMO`、`RUBY_TRIAL_2` |
| 解禁レベル | 4 |
| 最大ランク | 1 |
| クールダウン | 180（cooldownBurn: `180`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 1200（rangeBurn: `1200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerBarrier.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerBarrier` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

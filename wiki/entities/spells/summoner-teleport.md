---
title: "テレポート（SummonerTeleport）"
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
spell_id: "SummonerTeleport"
spell_key: "12"
spell_name: "テレポート"
data_version: "16.18.1"
modes:
  - "CLASSIC"
  - "SWIFTPLAY"
  - "ULTBOOK"
  - "WIPMODEWIP4"
  - "DOOMBOTSTEEMO"
  - "PRACTICETOOL"
  - "ONEFORALL"
  - "RUBY"
  - "ARSR"
  - "RUBY_TRIAL_2"
  - "TUTORIAL"
  - "ASSASSINATE"
  - "RUBY_TRIAL_3"
  - "RUBY_TRIAL_1"
---

# テレポート（SummonerTeleport）

## 概要

- **日本語名：** テレポート
- **レコードID：** `SummonerTeleport`
- **キー：** `12`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード（特殊モード: ULTBOOK）

## 効果

短い詠唱後、対象指定不可になって味方ユニットの位置まで移動する。「真テレポート」にアップグレードされると移動速度が大幅に増加する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
{{ channelduration }}秒間の詠唱後、<keyword>対象指定不可</keyword>になり、指定した味方の建造物、ミニオン、ワードのいずれかに移動する。 <br /><br />{{ upgrademinute }}分で「真テレポート」にアップグレードされて、移動速度が大幅に増加する。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `CLASSIC`、`SWIFTPLAY`、`ULTBOOK`、`WIPMODEWIP4`、`DOOMBOTSTEEMO`、`PRACTICETOOL`、`ONEFORALL`、`RUBY`、`ARSR`、`RUBY_TRIAL_2`、`TUTORIAL`、`ASSASSINATE`、`RUBY_TRIAL_3`、`RUBY_TRIAL_1` |
| 解禁レベル | 7 |
| 最大ランク | 1 |
| クールダウン | 300（cooldownBurn: `300`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 25000（rangeBurn: `25000`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerTeleport.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerTeleport` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

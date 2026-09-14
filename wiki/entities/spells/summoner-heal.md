---
title: "ヒール（SummonerHeal）"
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
spell_id: "SummonerHeal"
spell_key: "7"
spell_name: "ヒール"
data_version: "16.18.1"
modes:
  - "ARAM"
  - "TUTORIAL_MODULE_1"
  - "TUTORIAL"
  - "KIWI"
  - "ULTBOOK"
  - "SWIFTPLAY"
  - "CLASSIC"
  - "PRACTICETOOL"
  - "RUBY"
  - "RUBY_TRIAL_1"
  - "BRAWL"
  - "URF"
  - "KIWI_JADE"
  - "RUBY_TRIAL_3"
  - "TUTORIAL_MODULE_2"
  - "ONEFORALL"
  - "ASSASSINATE"
  - "ARSR"
  - "NEXUSBLITZ"
  - "DOOMBOTSTEEMO"
  - "RUBY_TRIAL_2"
---

# ヒール（SummonerHeal）

## 概要

- **日本語名：** ヒール
- **レコードID：** `SummonerHeal`
- **キー：** `7`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード（特殊モード: ULTBOOK）

## 効果

自身および対象の味方チャンピオンの体力を回復し、移動速度を増加させる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自身およびカーソルに最も近い味方チャンピオンの<healing>体力を{{ totalheal }}</healing>回復し、{{ movespeedduration }}秒間、<speed>移動速度を{{ movespeed*100 }}%</speed>上昇させる。<br /><br /><rules>対象が指定されない場合、効果範囲内でもっとも瀕死の味方チャンピオンに作用する。<br />直前にサモナースペル「ヒール」の効果を受けた味方に対しては、体力の回復量が半減する。</rules>
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `ARAM`、`TUTORIAL_MODULE_1`、`TUTORIAL`、`KIWI`、`ULTBOOK`、`SWIFTPLAY`、`CLASSIC`、`PRACTICETOOL`、`RUBY`、`RUBY_TRIAL_1`、`BRAWL`、`URF`、`KIWI_JADE`、`RUBY_TRIAL_3`、`TUTORIAL_MODULE_2`、`ONEFORALL`、`ASSASSINATE`、`ARSR`、`NEXUSBLITZ`、`DOOMBOTSTEEMO`、`RUBY_TRIAL_2` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 240（cooldownBurn: `240`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 875（rangeBurn: `875`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerHeal.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerHeal` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

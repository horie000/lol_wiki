---
title: "スマイト（SummonerSmite）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerSmite"
spell_key: "11"
spell_name: "スマイト"
data_version: "16.18.1"
modes:
  - "DOOMBOTSTEEMO"
  - "PRACTICETOOL"
  - "CLASSIC"
  - "SWIFTPLAY"
  - "URF"
  - "NEXUSBLITZ"
  - "ONEFORALL"
  - "TUTORIAL"
  - "ARSR"
---

# スマイト（SummonerSmite）

## 概要

- **日本語名：** スマイト
- **レコードID：** `SummonerSmite`
- **キー：** `11`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード

## 効果

モンスターまたはミニオンに確定ダメージを与える。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
対象の大型モンスターまたはレーンミニオンに<trueDamage>{{ smitebasedamage }}の確定ダメージ</trueDamage>を与える。<br /><br />チャンピオンのペットには<trueDamage>{{ firstpvpdamage }}の確定ダメージ</trueDamage>を与える。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `DOOMBOTSTEEMO`、`PRACTICETOOL`、`CLASSIC`、`SWIFTPLAY`、`URF`、`NEXUSBLITZ`、`ONEFORALL`、`TUTORIAL`、`ARSR` |
| 解禁レベル | 3 |
| 最大ランク | 1 |
| クールダウン | 15（cooldownBurn: `15`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 500（rangeBurn: `500`） |
| 最大弾薬 | 2 |
| 画像ファイル | `SummonerSmite.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerSmite` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

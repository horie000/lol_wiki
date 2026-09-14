---
title: "クレンズ（SummonerBoost_Jade）"
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
spell_id: "SummonerBoost_Jade"
spell_key: "71"
spell_name: "クレンズ"
data_version: "16.18.1"
modes:
  - "JADE"
---

# クレンズ（SummonerBoost_Jade）

## 概要

- **日本語名：** クレンズ
- **レコードID：** `SummonerBoost_Jade`
- **キー：** `71`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

敵からの行動妨害やサモナースペルによる効果をすべて解除し、その後、一時的に敵から受ける行動妨害の効果時間を短縮する。サモナーの決意: 行動妨害耐性バフの効果時間を延長する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
行動妨害やサモナースペルによるデバフをすべて解除し、その後{{ tenacitydurationfinalcalc }}秒間、自身への行動妨害効果時間を65%短縮する。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 210（cooldownBurn: `210`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 200（rangeBurn: `200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerBoost_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerBoost_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

---
title: "ゴースト（SummonerHaste_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerHaste_Jade"
spell_key: "76"
spell_name: "ゴースト"
data_version: "16.18.1"
modes:
  - "JADE"
---

# ゴースト（SummonerHaste_Jade）

## 概要

- **日本語名：** ゴースト
- **レコードID：** `SummonerHaste_Jade`
- **キー：** `76`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

移動速度が増加し、効果時間中はユニットの衝突判定が無視できるようになる。サモナーの激憤: 「ゴースト」によって付与される移動速度が増加する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
{{ duration }}秒間、<speed>移動速度が{{ movespeedmodfinal }}</speed>増加して<keyword>ゴースト化</keyword>する。<br /><br /><keyword>ゴースト</keyword>: 他のユニットをすり抜けて移動する。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 240（cooldownBurn: `240`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 200（rangeBurn: `200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerHaste_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerHaste_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

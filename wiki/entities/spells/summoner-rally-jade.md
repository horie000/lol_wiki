---
title: "ラリー（SummonerRally_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerRally_Jade"
spell_key: "709"
spell_name: "ラリー"
data_version: "16.18.1"
modes:
  - "JADE"
---

# ラリー（SummonerRally_Jade）

## 概要

- **日本語名：** ラリー
- **レコードID：** `SummonerRally_Jade`
- **キー：** `709`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

一時的にかがり火を焚き、範囲内の味方の攻撃力を増加させる。サモナーの激憤: 「ラリー」によってさらに魔力も増加させる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
15秒間、<scaleHealth>{{ hpcalc }}の体力</scaleHealth>を持つかがり火を焚き、味方の<scaleAD>攻撃力を{{ adcalc }}</scaleAD>増加させるオーラを発生させる。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 270（cooldownBurn: `270`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 25000（rangeBurn: `25000`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerRally_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerRally_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

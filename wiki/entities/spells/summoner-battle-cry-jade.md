---
title: "サージ（SummonerBattleCry_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerBattleCry_Jade"
spell_key: "716"
spell_name: "サージ"
data_version: "16.18.1"
modes:
  - "JADE"
---

# サージ（SummonerBattleCry_Jade）

## 概要

- **日本語名：** サージ
- **レコードID：** `SummonerBattleCry_Jade`
- **キー：** `716`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

一時的に自身を強化して、攻撃速度と魔力を増加させる。サモナーの激憤: 攻撃速度ボーナスが5%、 魔力ボーナスが10%増加する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自身を強化して、12秒間<attackSpeed>攻撃速度を{{ totalasactual }}</attackSpeed>、<scaleAP>魔力を{{ totalapactual }}</scaleAP>増加させる。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 180（cooldownBurn: `180`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 200（rangeBurn: `200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerBattleCry_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerBattleCry_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

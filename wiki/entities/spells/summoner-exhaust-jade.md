---
title: "イグゾースト（SummonerExhaust_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerExhaust_Jade"
spell_key: "73"
spell_name: "イグゾースト"
data_version: "16.18.1"
modes:
  - "JADE"
---

# イグゾースト（SummonerExhaust_Jade）

## 概要

- **日本語名：** イグゾースト
- **レコードID：** `SummonerExhaust_Jade`
- **キー：** `73`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

敵チャンピオンにスロウ効果を付与し、攻撃速度と与ダメージを低下させる。サモナーの激憤: 「イグゾースト」が対象の物理防御と魔法防御も10低下させる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
指定した敵チャンピオンを疲弊させて、2.5秒間、対象の移動速度と与ダメージを{{ damagereduction }}%低下させ、効果時間中は攻撃速度を{{ attackspeedreduction }}%低下させる。<br /><br />
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
| 射程 | 550（rangeBurn: `550`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerExhaust_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerExhaust_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

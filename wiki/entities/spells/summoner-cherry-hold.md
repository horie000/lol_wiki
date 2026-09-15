---
title: "逃亡（SummonerCherryHold）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerCherryHold"
spell_key: "2201"
spell_name: "逃亡"
data_version: "16.18.1"
modes:
  - "CHERRY"
---

# 逃亡（SummonerCherryHold）

## 概要

- **日本語名：** 逃亡
- **レコードID：** `SummonerCherryHold`
- **キー：** `2201`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** CHERRY専用

## 効果

短時間、移動速度が大幅に増加する。敵チャンピオンと逆方向に走っている間は、移動速度がさらに増加する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
<keywordMajor>発動スペルスロット:</keywordMajor> サモナースペルを付与するオーグメントがこのスロットと置き換わる。<br /><br />{{ duration }}秒間、<moveSpeed>移動速度が{{ basems*100 }}%</moveSpeed>増加し、さらに自身の後ろにいる敵1体につき{{ bonusmsperenemybehind*100 }}%増加する。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `CHERRY` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 45（cooldownBurn: `45`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 25000（rangeBurn: `25000`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerCherryHold.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerCherryHold` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

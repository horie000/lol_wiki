---
title: "リバイブ（SummonerRevive_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerRevive_Jade"
spell_key: "777"
spell_name: "リバイブ"
data_version: "16.18.1"
modes:
  - "JADE"
---

# リバイブ（SummonerRevive_Jade）

## 概要

- **日本語名：** リバイブ
- **レコードID：** `SummonerRevive_Jade`
- **キー：** `777`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

自身のチャンピオンを即座にスタート地点上に復活させ、移動速度を短時間増加させる。サモナーの慧眼: 「リバイブ」を使用すると、一時的に220 - 560の体力を獲得する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自陣のスタート地点で瞬時に蘇生し、短時間移動速度が<speed>{{ spell.summonerrevive_jade:bonusmovespeed*100 }}%</speed>増加する。増加した移動速度はその後12秒かけて減衰する。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 510（cooldownBurn: `510`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 200（rangeBurn: `200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerRevive_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerRevive_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

---
title: "クラリティ（SummonerMana）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerMana"
spell_key: "13"
spell_name: "クラリティ"
data_version: "16.18.1"
modes:
  - "KIWI"
  - "FIRSTBLOOD"
  - "ARAM"
  - "KIWI_JADE"
---

# クラリティ（SummonerMana）

## 概要

- **日本語名：** クラリティ
- **レコードID：** `SummonerMana`
- **キー：** `13`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** 複数モード

## 効果

自身および味方チャンピオンのマナを回復する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自身の最大マナの{{ e1 }}%、周囲の味方の最大マナの{{ e2 }}%を回復する。
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `KIWI`、`FIRSTBLOOD`、`ARAM`、`KIWI_JADE` |
| 解禁レベル | 6 |
| 最大ランク | 1 |
| クールダウン | 240（cooldownBurn: `240`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 600（rangeBurn: `600`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerMana.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerMana` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

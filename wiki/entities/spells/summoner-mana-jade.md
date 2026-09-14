---
title: "クラリティ（SummonerMana_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerMana_Jade"
spell_key: "713"
spell_name: "クラリティ"
data_version: "16.18.1"
modes:
  - "JADE"
---

# クラリティ（SummonerMana_Jade）

## 概要

- **日本語名：** クラリティ
- **レコードID：** `SummonerMana_Jade`
- **キー：** `713`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

自身および味方チャンピオンのマナを回復する。サモナーの慧眼: マナがより多く回復する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自身のチャンピオンは<scaleMana>{{ selfmanaactual }}マナ</scaleMana>を、周囲の味方は<scaleMana>最大マナの{{ allymanaactual }}</scaleMana>を回復する。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 135（cooldownBurn: `135`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 600（rangeBurn: `600`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerMana_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerMana_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

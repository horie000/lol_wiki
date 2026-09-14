---
title: "クレアボヤンス（SummonerClairvoyance_Jade）"
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
spell_id: "SummonerClairvoyance_Jade"
spell_key: "75"
spell_name: "クレアボヤンス"
data_version: "16.18.1"
modes:
  - "JADE"
---

# クレアボヤンス（SummonerClairvoyance_Jade）

## 概要

- **日本語名：** クレアボヤンス
- **レコードID：** `SummonerClairvoyance_Jade`
- **キー：** `75`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

少しの間、指定した範囲の視界を獲得する。サモナーの慧眼: 「クレアボヤンス」で可視化されたユニットの視界を5秒間維持する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
指定した範囲の視界を5秒間獲得する。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 60（cooldownBurn: `60`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 25000（rangeBurn: `25000`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerClairvoyance_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerClairvoyance_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

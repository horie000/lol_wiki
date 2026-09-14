---
title: "プレースホルダー（Summoner_UltBookPlaceholder）"
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
spell_id: "Summoner_UltBookPlaceholder"
spell_key: "54"
spell_name: "プレースホルダー"
data_version: "16.18.1"
modes:
  - "ULTBOOK"
---

# プレースホルダー（Summoner_UltBookPlaceholder）

## 概要

- **日本語名：** プレースホルダー
- **レコードID：** `Summoner_UltBookPlaceholder`
- **キー：** `54`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** ULTBOOK専用

## 効果

このスロットは試合開始時に選択された別のチャンピオンのアルティメットスキルに置き換わる。30秒以内にアルティメットスキルを選択する必要がある。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
選択したアルティメットサモナースペルと置き換わる。{{ spellmodifierdescriptionappend }}
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `ULTBOOK` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 0（cooldownBurn: `0`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | &nbsp; |
| リソース | &nbsp; |
| 射程 | 400（rangeBurn: `400`） |
| 最大弾薬 | -1 |
| 画像ファイル | `Summoner_UltBookPlaceholder.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `Summoner_UltBookPlaceholder` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

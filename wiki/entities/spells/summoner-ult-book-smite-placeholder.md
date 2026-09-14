---
title: "プレースホルダー＆アタックスマイト（Summoner_UltBookSmitePlaceholder）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "Summoner_UltBookSmitePlaceholder"
spell_key: "55"
spell_name: "プレースホルダー＆アタックスマイト"
data_version: "16.18.1"
modes:
  - "ULTBOOK"
---

# プレースホルダー＆アタックスマイト（Summoner_UltBookSmitePlaceholder）

## 概要

- **日本語名：** プレースホルダー＆アタックスマイト
- **レコードID：** `Summoner_UltBookSmitePlaceholder`
- **キー：** `55`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** ULTBOOK専用

## 効果

このスロットは別のチャンピオンのアルティメットスキルに置き換わり、「アタックスマイト」を獲得する。30秒以内にアルティメットスキルを選択する必要がある。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
選択したアルティメットサモナースペルと置き換わる。<br /><br />「アタックスマイト」を獲得。「アタックスマイト」は味方のバフモンスター、エピックモンスター、スカトルクラブにとどめを刺す。<br /><br /><attention>「アタックスマイト」にクールダウンはない。</attention>{{ spellmodifierdescriptionappend }}
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
| 画像ファイル | `Summoner_UltBookSmitePlaceholder.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `Summoner_UltBookSmitePlaceholder` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

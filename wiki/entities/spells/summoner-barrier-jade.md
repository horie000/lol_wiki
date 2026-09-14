---
title: "バリア（SummonerBarrier_Jade）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerBarrier_Jade"
spell_key: "721"
spell_name: "バリア"
data_version: "16.18.1"
modes:
  - "JADE"
---

# バリア（SummonerBarrier_Jade）

## 概要

- **日本語名：** バリア
- **レコードID：** `SummonerBarrier_Jade`
- **キー：** `721`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

短時間シールドを獲得する。サモナーの決意: 「バリア」のシールド量が増加する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
{{ shieldduration }}秒間、<shield>耐久値{{ shieldstrengthfinal }}のシールド</shield>を獲得する。<br /><br />
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
| 射程 | 1200（rangeBurn: `1200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerBarrier_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerBarrier_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

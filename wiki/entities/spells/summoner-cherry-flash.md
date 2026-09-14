---
title: "フラッシュ（SummonerCherryFlash）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerCherryFlash"
spell_key: "2202"
spell_name: "フラッシュ"
data_version: "16.18.1"
modes:
  - "CHERRY"
---

# フラッシュ（SummonerCherryFlash）

## 概要

- **日本語名：** フラッシュ
- **レコードID：** `SummonerCherryFlash`
- **キー：** `2202`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** CHERRY専用

## 効果

自身のチャンピオンを短い距離、指定した方向に瞬間移動させる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
自身のチャンピオンを短い距離、指定した方向に瞬間移動させる。<br /><br />一度発動すると、1ラウンド経過するまで発動できなくなる<rules>(購入フェーズと戦闘フェーズの両方を合わせて1ラウンド)。</rules>
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `CHERRY` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 0.25（cooldownBurn: `0.25`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 425（rangeBurn: `425`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerCherryFlash.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerCherryFlash` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

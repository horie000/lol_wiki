---
title: "ポロトス（SummonerPoroThrow）"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - summoner-spell
  - game-data
spell_id: "SummonerPoroThrow"
spell_key: "31"
spell_name: "ポロトス"
data_version: "16.18.1"
modes:
  - "KINGPORO"
---

# ポロトス（SummonerPoroThrow）

## 概要

- **日本語名：** ポロトス
- **レコードID：** `SummonerPoroThrow`
- **キー：** `31`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** KINGPORO専用

## 効果

敵にポロを投げつける。命中すると、その対象まで素早く移動することができる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
ポロを遠くまで投げ、最初に命中した敵に{{ f2 }}の確定ダメージを与え、対象の<span class="coloree91d7">真の視界</span>を得る。<br /><br />敵に命中すると3秒以内に再発動することができ、その敵までダッシュして{{ f2 }}の追加確定ダメージを与える。ダッシュを発動すると「ポロトス」のクールダウンが{{ e4 }}秒短縮される。<br /><br />ポロは動物であり呪文ではないので、スペルシールドや「風殺の壁」ではガードできない。<br /><br /><span class="colorFDD017">「ポロはルーンテラにおける航空力学モデルである」</span></mainText>
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `KINGPORO` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 20（cooldownBurn: `20`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 2500（rangeBurn: `2500`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerPoroThrow.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerPoroThrow` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

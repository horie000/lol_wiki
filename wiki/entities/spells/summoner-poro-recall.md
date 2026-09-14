---
title: "王のために！（SummonerPoroRecall）"
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
spell_id: "SummonerPoroRecall"
spell_key: "30"
spell_name: "王のために！"
data_version: "16.18.1"
modes:
  - "KINGPORO"
---

# 王のために！（SummonerPoroRecall）

## 概要

- **日本語名：** 王のために！
- **レコードID：** `SummonerPoroRecall`
- **キー：** `30`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** KINGPORO専用

## 効果

ポロキングの側へ素早く移動する。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
<span class="colorFFE076">自動効果:</span> 敵チャンピオンにポロが命中すると、自分のチームにポロ・マークがつく。ポロ・マークが10個たまるとポロキングを召喚し、チームと共に戦ってくれる。ポロキングが召喚されている間、どちらのチームにもポロ・マークはつかない。<br /><br /><span class="colorFFE076">発動効果:</span> ポロキングのお側へ素早く駆けつける。自分のチームがポロキングを召喚している間のみ発動可能。<br /><br /><span class="colorFDD017">「ポロには人の心を惹きつけるものがある。それ以外の者はなんとなくついて来ているだけだ」</span></mainText>
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `KINGPORO` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 10（cooldownBurn: `10`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 200（rangeBurn: `200`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerPoroRecall.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerPoroRecall` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

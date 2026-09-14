---
title: "マーク（SummonerSnowURFSnowball_Mark）"
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
spell_id: "SummonerSnowURFSnowball_Mark"
spell_key: "39"
spell_name: "マーク"
data_version: "16.18.1"
modes:
  - "SNOWURF"
---

# マーク（SummonerSnowURFSnowball_Mark）

## 概要

- **日本語名：** マーク
- **レコードID：** `SummonerSnowURFSnowball_Mark`
- **キー：** `39`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** SNOWURF専用

## 効果

直線上の敵に向かって雪玉を投げる。敵に当たるとマークを残し、真の視界を得て、マークをつけたチャンピオンはこの対象まで素早く飛ぶことができる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
雪玉を遠くまで投げ、最初に命中した敵ユニットに{{ tooltipdamagetotal }}の確定ダメージを与えて、対象の<span class="coloree91d7">真の視界</span>を得る。敵に命中すると{{ e3 }}秒以内に再発動することができ、その敵までダッシュして{{ tooltipdamagetotal }}の追加確定ダメージを与える。対象に向かってダッシュすると、マークのクールダウンが{{ e4 }}%短縮される。<br /><br /><span class="colorFFFF00">「マーク」によって飛ばされる雪玉は、スペルシールドや飛翔物軽減効果の影響を受けない。</span>
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `SNOWURF` |
| 解禁レベル | 6 |
| 最大ランク | 1 |
| クールダウン | 80（cooldownBurn: `80`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 8000（rangeBurn: `8000`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerSnowURFSnowball_Mark.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerSnowURFSnowball_Mark` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

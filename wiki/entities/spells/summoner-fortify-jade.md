---
title: "フォティファイ（SummonerFortify_Jade）"
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
spell_id: "SummonerFortify_Jade"
spell_key: "705"
spell_name: "フォティファイ"
data_version: "16.18.1"
modes:
  - "JADE"
---

# フォティファイ（SummonerFortify_Jade）

## 概要

- **日本語名：** フォティファイ
- **レコードID：** `SummonerFortify_Jade`
- **キー：** `705`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

6秒間、自陣のすべてのタワーが無敵状態になり、その攻撃速度が100%増加する。サモナーの決意: タワーが対象の周囲に範囲ダメージを与える。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
<spellPassive>自動効果</spellPassive>: 「フォティファイ」がクールダウン中でない場合、ミニオンに通常攻撃時効果で<scaleAD>{{ bonusminiondamage }}の追加ダメージ</scaleAD>を与える。<br /><br /><spellActive>発動効果</spellActive>: {{ duration }}秒間、自陣のすべてのタワーが無敵状態になり、その攻撃速度が{{ attackspeed*100 }}%増加する。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 180（cooldownBurn: `180`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 25000（rangeBurn: `25000`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerFortify_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerFortify_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

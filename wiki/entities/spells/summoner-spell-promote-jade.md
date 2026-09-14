---
title: "プロモート（SummonerSpell_Promote_Jade）"
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
spell_id: "SummonerSpell_Promote_Jade"
spell_key: "720"
spell_name: "プロモート"
data_version: "16.18.1"
modes:
  - "JADE"
---

# プロモート（SummonerSpell_Promote_Jade）

## 概要

- **日本語名：** プロモート
- **レコードID：** `SummonerSpell_Promote_Jade`
- **キー：** `720`
- **データversion：** `16.18.1`
- **分類（利用モードに基づく整理）：** JADE専用

## 効果

ミニオン1体を昇格させて、そのパラメーターを増加させ、強化オーラを付与して、そのミニオンが敵を倒すと自身がゴールドを獲得する。サモナーの激憤: 砲撃ミニオンの増加攻撃力オーラが、チャンピオンにも影響を与えるようになる。

### ツールチップ（原典の表示テンプレート）

数値プレースホルダーと表示用タグは、原典の表現を保つためそのまま記録している。

```text
味方のミニオン1体を<keywordMajor>砲撃ミニオン</keywordMajor>に昇格させる。この砲撃ミニオンの<healing>体力は{{ unithealth }}</healing>、<physicalDamage>攻撃力は{{ unitdamage }}</physicalDamage>となる。このミニオンが敵をキルすると自身がゴールドを獲得する。<br /><br /><keywordMajor>砲撃ミニオン</keywordMajor>はオーラをまとっており、周囲のミニオンの<physicalDamage>攻撃力を{{ damageaura }}</physicalDamage>、<scaleArmor>物理防御を{{ armoraura }}</scaleArmor>増加させる。<br /><br />
```

## 使用条件・パラメータ

| 項目 | 原典値 |
| --- | --- |
| 利用可能モード | `JADE` |
| 解禁レベル | 1 |
| 最大ランク | 1 |
| クールダウン | 270（cooldownBurn: `270`） |
| コスト | 0（costBurn: `0`） |
| コスト種別 | コスト無し |
| リソース | コスト無し |
| 射程 | 4294967295（rangeBurn: `4294967295`） |
| 最大弾薬 | -1 |
| 画像ファイル | `SummonerSpell_Promote_Jade.png` |

## 未展開フィールド

- `datavalues`、`effect`、`effectBurn`、`vars` は、実行時計算または内部配列のため、このページでは表形式に展開していない。
- `tooltip` 内のプレースホルダー（`{{ ... }}`）は、同版の追加仕様がないため数値へ置換していない。

## 出典

- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `16.18.1/data/ja_JP/summoner.json` の `SummonerSpell_Promote_Jade` レコード。
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]

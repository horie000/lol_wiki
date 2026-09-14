---
title: "サミーラ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-assassin
  - data-dragon
champion_id: "Samira"
champion_key: "360"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Samira.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Samira.png"
---

# サミーラ

![[raw/assets/champions/Samira.png|128]]

## 基本情報

- **英字ID：** `Samira`
- **キー：** `360`
- **称号：** 砂漠の薔薇
- **データversion：** `16.18.1`

## 紹介

サミーラはゆるぎない自信を浮かべた目で死を見つめ、行く先々でスリルを探し求める。幼少期にシュリーマの家が破壊された後、サミーラはノクサスで天職を見つけた。そこで彼女は危険な任務を請け負い、クールなスタイルの命知らずとしての評判を築いた。黒色火薬の拳銃と特注の剣を携え、サミーラは立ちはだかる者は誰であろうと排除し、生きるか死ぬかの状況を切り抜ける。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 108 |
| `mp` | 349 |
| `mpperlevel` | 38 |
| `movespeed` | 335 |
| `armor` | 26 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — デアデビルインパルス：** 直前に命中したものとは異なる通常攻撃またはスキルを命中させることでコンボが増加していく。近接攻撃射程の通常攻撃は追加魔法ダメージを与える。移動不能効果を受けた敵に通常攻撃を行うと、自身の射程内までダッシュする。敵がノックアップしていた場合は、少しの間だけノックアップさせたままにする。

- **Q — フレア：** 銃を発砲するか、剣を振ってダメージを与える。「ワイルドラッシュ」中に使用した場合は、ダッシュ後に通り道にいたすべての敵を攻撃する。
- **W — ブレードワール：** 周囲を斬りつけて敵にダメージを与え、敵の飛翔物を破壊する。
- **E — ワイルドラッシュ：** 敵(建造物を含む)を通り抜けるようにダッシュし、接触した敵を斬りつけて、攻撃速度が増加する。敵チャンピオンをキルすると、このスキルのクールダウンが解消される。
- **R — インフェルノトリガー：** 銃から弾丸を高速で連射し、周囲のすべての敵に攻撃を行う。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Samira` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Samira.png)

---
title: "ヤスオ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-assassin
champion_id: "Yasuo"
champion_key: "157"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "つむじ風"
image_path: "raw/assets/champions/Yasuo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yasuo.png"
---

# ヤスオ

![[raw/assets/champions/Yasuo.png|128]]

## 基本情報

- **英字ID：** `Yasuo`
- **キー：** `157`
- **称号：** 赦されざる者
- **データversion：** `16.18.1`

## 紹介

固い信念を持つアイオニア人のヤスオは風を操って戦う俊敏な剣士だ。高慢な若者だった彼は師匠殺しの濡れ衣を着せられ、無実を証明できぬまま、身を守るために兄を殺めることを余儀なくされた。師匠の死にまつわる真実が明らかとなってもなお、ヤスオが自らの過ちを赦すことはできなかった。自分の剣を導く風だけを頼りに、彼は今も祖国の地を放浪し続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** つむじ風

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 4 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 110 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.697 |

## アビリティ

- **パッシブ — 浪人道：** クリティカル率が増加する。また、移動距離に応じてシールドがチャージされ、敵チャンピオンおよび中立モンスターからダメージを受けると発動する。

- **Q — 抜刀：** 指定方向に突きを放ち、直線上の敵すべてにダメージを与える。 このスキルが命中するとヤスオは「つむじ風」のスタックを数秒間得る。スタックが2つたまるとヤスオは風を身にまとい、次の「抜刀」と同時に「つむじ風」を放つ。「つむじ風」は指定方向に吹き抜け、触れた敵ユニットをノックアップさせる。 「抜刀」は通常攻撃扱いのため、通常攻撃と同じように強化される。
- **W — 風殺の壁：** 4秒間持続し、少しずつ前進する風の壁を生み出す。敵のあらゆる発射物は、この壁に触れると消滅する。
- **E — 風薙ぎ：** 指定した敵を通り過ぎるようにダッシュし、魔法ダメージを与える。発動ごとに、その後のダッシュで与えるダメージが増加する(上限あり)。 同一の敵に対しては数秒間、このスキルを再発動できない。 このスキルのダッシュ中に「抜刀」を発動すると、円状に斬撃を繰り出す。
- **R — 鬼哭啾々：** ノックアップ状態の敵チャンピオンのもとへブリンクし、空中で斬撃を繰り出して物理ダメージを与える。また、範囲内のノックアップ中の敵をさらにノックアップさせる。発動と同時に波動ゲージが満タンになるが「つむじ風」のスタックをすべて消費する。 少しの間、クリティカル時に対象の物理防御増加分を大きく貫通する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yasuo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yasuo.png)

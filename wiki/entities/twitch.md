---
title: "トゥイッチ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-assassin
champion_id: "Twitch"
champion_key: "29"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Twitch.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Twitch.png"
---

# トゥイッチ

![[raw/assets/champions/Twitch.png|128]]

## 基本情報

- **英字ID：** `Twitch`
- **キー：** `29`
- **称号：** 黒死のドブネズミ
- **データversion：** `16.18.1`

## 紹介

トゥイッチは汚物を漁ることに情熱を持つ、生まれながらの疫病ネズミで、そのためなら前足を汚すことも恐れはしない。化学物質によって強化されたクロスボウを豊かなピルトーヴァーの中心部に向けて、上にある都市に住む者たちに彼らが本当はいかに汚れた存在であるかを示してやろうと誓っている。常に忍び足で歩き回り、下層でゴミを漁っていない時は、他人のゴミの山の中に潜り込んでお宝を探している…カビたサンドイッチでも見つかれば御の字だ。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 98 |
| `mp` | 300 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 27 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — スゴイ毒ダ！：** 通常攻撃で対象を毒%i:OnHit%通常攻撃時効果に侵し、毎秒確定ダメージを与える。

- **Q — オイラだヨ！：** 数秒間カモフラージュ状態になり、その間移動速度が増加する。カモフラージュの解除時に短時間攻撃速度が増加する。 「スゴイ毒ダ！」でチャンピオンを倒すと、「オイラだヨ！」のクールダウンがリセットされる。
- **W — コイツを食らエ！：** 毒物が入った容器を投げて破裂させ、効果範囲内の敵ユニットをスロウ状態にし、猛毒効果をかける。
- **E — ボーン！：** 猛毒状態にした敵を病原菌に侵し、さらにダメージを与える。
- **R — ヒャッハー！：** クロスボウの最大威力を引き出し、射程距離を大幅に拡大する。発射した矢は命中した敵ユニットを貫通してダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Twitch` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Twitch.png)

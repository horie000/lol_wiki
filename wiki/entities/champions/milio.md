---
title: "ミリオ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-support
  - role-mage
  - data-dragon
champion_id: "Milio"
champion_key: "902"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Milio.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Milio.png"
---

# ミリオ

![[raw/assets/champions/Milio.png|128]]

## 基本情報

- **英字ID：** `Milio`
- **キー：** `902`
- **称号：** やさしき炎
- **データversion：** `16.18.1`

## 紹介

イシュタル出身の心あたたかい少年。わずか12歳にして火のアクシオムを使いこなし、「癒やしの炎」という未知なる力を発見した。この新たな力を用い、ミリオはかつての祖母のように、ユン・タルの一員となることを目指す。それがかなえば、現在流謫の身にある故郷の家族を、正当な地位に引き上げることができるからだ。イシュタルのジャングルを抜け、首都イシャオカンまではるばる旅をしてきたミリオは、ユン・タルの座に就くため、ヴィダリオンの試練に備えて修練を積んでいる。その試練の内容も、それに伴う危険についても知らずに。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 88 |
| `mp` | 365 |
| `mpperlevel` | 43 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 48 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ファイヤーアップ！：** ミリオのスキルに触れた味方は、次の攻撃で追加のバーストダメージを与え、対象を炎上させる。

- **Q — ウルトラメガファイヤーキック：** 敵1体をノックバックさせるボールをキックする。ボールは敵に命中すると、跳ね上がってから対象に向かって落下し、着地時に範囲内の敵にダメージとスロウ効果を与える。
- **W — 癒しの焚き火：** 範囲内の味方の体力を回復し、その射程距離を延長するゾーンを作り出す。このゾーンは発動地点から一番近い味方を追従する。
- **E — 抱擁のぬくもり：** 味方1体にシールドを付与し、一時的に対象の移動速度を上昇させる。このスキルは2回までチャージできる。
- **R — 生命の息吹：** 穏やかな炎の波動を放ち、範囲内の味方の体力を回復して、行動妨害効果を除去する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Milio` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Milio.png)

---
title: "ハイマーディンガー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
  - role-support
  - data-dragon
champion_id: "Heimerdinger"
champion_key: "74"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Heimerdinger.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Heimerdinger.png"
---

# ハイマーディンガー

![[raw/assets/champions/Heimerdinger.png|128]]

## 基本情報

- **英字ID：** `Heimerdinger`
- **キー：** `74`
- **称号：** 誉れ高き発明王
- **データversion：** `16.18.1`

## 紹介

変わり者のセシル・B・ハイマーディンガー教授は、史上稀にみる革新的な発明家の一人として称賛される存在だ。ピルトーヴァーの評議会でも最古参となる彼は、飽くなき進歩を求めるこの都市の良い部分のみならず、悪しき部分もまた等しく見てきた。それでも天才的な科学者であり教師としての顔も持つ彼は、自らの風変わりな装置を使って人々の生活を向上させるべくその身を捧げ続けている。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 558 |
| `hpperlevel` | 105 |
| `mp` | 385 |
| `mpperlevel` | 20 |
| `movespeed` | 340 |
| `armor` | 19 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ヘクステックの親和性：** 味方のタワーまたは自身が配置した砲台の近くにいると移動速度が増加する。

- **Q — H-28G革新砲：** 砲台を設置する。砲台は通常攻撃だけでなく、一定時間ごとに貫通レーザーを発射する(タワーに対して与えるダメージは半減する)。
- **W — ヘクステック小型ロケット：** 指定地点へ向け、長射程のロケット弾を5発発射する。
- **E — CH-2超電磁グレネード：** 指定地点にグレネード弾を投げ、敵ユニットにダメージを与える。さらに中心で直撃した敵をスタンさせ、周囲の敵にスロウを与える。
- **R — アップグレード！！！：** 天才的なひらめきによってアップグレードを開発し、次に発動するスキルを強化できる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Heimerdinger` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Heimerdinger.png)

---
title: "ビクター"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
champion_id: "Viktor"
champion_key: "112"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Viktor.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viktor.png"
---

# ビクター

![[raw/assets/champions/Viktor.png|128]]

## 基本情報

- **英字ID：** `Viktor`
- **キー：** `112`
- **称号：** アーケインの先触れ
- **データversion：** `16.18.1`

## 紹介

かつての姿から完全なる生物力学的な進化を遂げたビクターは、輝ける進化を受け入れ、彼の支持者にとって救世主となる何かへと変わった。彼は感情を排除することで苦痛を排除できるという論理に基づき、自らの人間性を犠牲にして、ヘクスコアの啓示を世界に与えようとしている──その恩恵が誰にも理解されなかったとしても。このアーケインの達人にとっては、暴力は究極の方程式を解くために必要な変数でしかないのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 10 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 100 |
| `mp` | 405 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4.4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — グロリアス・エヴォリューション：** 敵を倒すたびに「ヘクス フラグメント」を獲得する。「ヘクス フラグメント」を100個獲得するごとに、発動効果スキルが1つ恒久的に強化される。すべての通常スキルをアップグレードすると、「ヘクス フラグメント」を100個獲得してアルティメットスキルが強化できる。

- **Q — パワーブラスト：** 敵ユニットを狙い撃って魔法ダメージを与え、自身にシールドを張り、次の通常攻撃のダメージが強化される。 強化: 「パワーブラスト」のシールドが60%増加し、このスキルを発動後、移動速度が増加する。
- **W — グラビティフィールド：** 強力な重力場を発生させる装置を展開し、範囲内の敵にスロウ効果を付与する。 また、装置から抜け出せなかった敵にスタン効果を付与する。 強化: スキルが敵にスロウ効果を付与する。
- **E — ヘクステック レイ：** バイオメカニカルアームから「ヘクステック レイ」を発射し、一直線にフィールドを焼き払いながら、命中した敵ユニットにダメージを与える。 強化: 「ヘクステック レイ」が焼き払った地面が爆発し、魔法ダメージを与える。
- **R — アーケインストーム：** フィールド上に「アーケインストーム」を召喚し、魔法ダメージを与えて、敵の詠唱を中断させる。嵐は一定時間ごとに周囲のすべての敵に魔法ダメージを与え、ビクターが移動方向を変えられる。 強化: 「アーケインストーム」の移動速度が25%増加し、嵐でダメージを受けたチャンピオンが倒されるたびに嵐が大きくなり、効果時間が延長される。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Viktor` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viktor.png)

---
title: "ドクター・ムンド"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "DrMundo"
champion_key: "36"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "なし"
image_path: "raw/assets/champions/DrMundo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/DrMundo.png"
---

# ドクター・ムンド

![[raw/assets/champions/DrMundo.png|128]]

## 基本情報

- **英字ID：** `DrMundo`
- **キー：** `36`
- **称号：** ゾウンの狂人
- **データversion：** `16.18.1`

## 紹介

完全に正気を失った、おぞましい紫色の悲しき殺人鬼。ゾウン市民の多くが闇の深い夜に外を出歩かないのは、ドクター・ムンドがいるためだ。今では“医者”を名乗っているが、以前はゾウンでも特に評判の悪い、とある医療院の患者だった。そこの職員を一人残らず“治療”したのち、ドクター・ムンドはかつて自身が処置を受けていた無人の病棟に診察室を構え、その身で何度も味わってきた非人道的な医療行為を、見よう見まねで行うようになった。棚に入った大量の薬物と、素人以下の医療知識を手に、ドクター・ムンドは今、注射を打つことで自身を...

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 103 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.5 |
| `spellblock` | 29 |
| `spellblockperlevel` | 2.3 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 気ままな往診：** 最初に受ける移動不能効果を無効化する。その際、代わりに体力を失い、近くに薬品の入った容器を落とす。落とした容器の上を歩いて回収すると体力が回復し、このスキルのクールダウンが短縮される。 また、ドクター・ムンドは極めて高い体力自動回復能力を持っている。

- **Q — 骨切りノコギリ：** 骨切りノコギリを投げ、最初に命中した敵に対象の現在体力に応じたダメージを与えて、スロウ効果を付与する。
- **W — 心臓ビリビリ：** 自身を感電させて、周囲の敵に継続的にダメージを与え、受けたダメージの一部を蓄える。効果時間の最後か再発動時に、周囲の敵に大ダメージを与える。これが敵に命中した場合は、それまでに蓄えていたダメージの一定割合を体力として回復する。
- **E — 野蛮な痛み：** 自動効果 - 自身の最大体力に応じて増加する、増加攻撃力を獲得する。 発動効果 - “往診用”バッグを敵に叩きつけ、自身の減少体力に応じた追加ダメージを与える。対象をキルした場合はその敵を弾き飛ばし、接触した敵にダメージを与える。
- **R — マキシマム投与：** 自身に薬品を注入し、減少体力の一定割合を瞬時に回復する。さらに移動速度が増加し、長い時間をかけて最大体力の一部を自動回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - Eの自動効果で最大体力に応じた増加攻撃力を得る。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.DrMundo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/DrMundo.png)

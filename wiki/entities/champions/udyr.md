---
title: "ウディア"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Udyr"
champion_key: "77"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Udyr.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Udyr.png"
---

# ウディア

![[raw/assets/champions/Udyr.png|128]]

## 基本情報

- **英字ID：** `Udyr`
- **キー：** `77`
- **称号：** 精霊と歩む者
- **データversion：** `16.18.1`

## 紹介

現存するスピリットウォーカーの中でも最大の力を持つウディアは、フレヨルドのあらゆる精霊と心を通わせることができる。彼らの欲求に共感して理解を示したり、その霊的なエネルギーを変換して、自身の原始的な戦闘法に取り入れることができるのだ。自らの心が周囲の心の声に埋もれてしまわないように、ウディアは内なる均衡を求めているが、外の世界についても均衡を欲している──フレヨルドの神秘的な風景は、対立と争いから生まれる成長によってのみ、繁栄することができるのだ。ウディアは、平和という停滞を避けるためには、犠牲を払うこ...

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 7 |
| `magic` | 4 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 664 |
| `hpperlevel` | 92 |
| `mp` | 271 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.65 |

## アビリティ

- **パッシブ — 精霊の繋ぎ手：** 4つの通常スキルで「型」を切り替え、スキルを再発動すると「型」がリフレッシュされて究極の効果を得る。さらに、スキル使用後、次の2回の通常攻撃の攻撃速度が増加する。

- **Q — 野性の爪：** 攻撃速度が増加し、次の2回の通常攻撃が追加物理ダメージを与える。 再発動: 攻撃速度がさらに増加し、次の2回の通常攻撃が対象に電撃を放つようになる。
- **W — 鉄の外皮：** シールドを獲得し、次の2回の通常攻撃で自身の体力を回復する。 再発動: より耐久値の高いシールドを獲得し、数秒間かけて最大体力の一定割合を回復する。
- **E — 焔の猛進：** 移動速度が増加し、各対象への最初の通常攻撃が対象をスタンさせる。 再発動: 少しの間、移動速度がさらに増加し、移動不能効果を受けなくなる。
- **R — 氷翼の嵐：** 極寒の嵐に身を包み、周囲の敵にダメージとスロウ効果を与える。 再発動: 嵐を強化して解き放ち、敵を追跡させて追加ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中15位（上位15%）。体力664、物理防御31、攻撃力62、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Udyr` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Udyr.png)

---
title: "ミス・フォーチュン"
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
  - role-mage
  - data-dragon
champion_id: "MissFortune"
champion_key: "21"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/MissFortune.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MissFortune.png"
---

# ミス・フォーチュン

![[raw/assets/champions/MissFortune.png|128]]

## 基本情報

- **英字ID：** `MissFortune`
- **キー：** `21`
- **称号：** 美貌の賞金稼ぎ
- **データversion：** `16.18.1`

## 紹介

美貌で名高く、容赦のなさで恐れられるビルジウォーターの船長サラ・フォーチュンは、面の皮の厚い港町の犯罪者たちの中でも一線を画して不屈である。子供の頃、略奪王のガングプランクに家族を殺されるのを目撃した彼女だが、数年後に彼を船ごと爆破して無慈悲な復讐を遂げた。彼女の力を侮る者は、魅力的で予測不能な彼女と対峙し…腹に銃弾を喰らうことになるだろう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 5 |
| `difficulty` | 1 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 100 |
| `mp` | 300 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 25 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — ラブタップ：** 新しい対象に通常攻撃するたびに追加物理ダメージを与える。

- **Q — ダブルアップ：** 指定した敵に発砲しダメージを与える。対象の背後に敵がいた場合、跳弾して後ろの敵にもダメージを与える。弾丸はどちらも「ラブタップ」の効果が適用される。
- **W — ストラット：** 攻撃を受けずにいると、自動効果により移動速度が増加するようになる。発動すると、短時間攻撃速度が増加する。クールダウン中は、「ラブタップ」によってクールダウンが短縮される。
- **E — レイニングバレット：** 一定範囲内に弾丸の雨を降らせて視界を確保するとともに、範囲内の敵に継続ダメージを与えてスロウ効果を付与する。
- **R — バレットタイム：** 前方の扇状範囲に大量の銃弾を放ち、範囲内にいる敵に大量のダメージを与える。波状に発射される弾丸の各ウェーブ毎にクリティカル判定を持つ。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.MissFortune` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MissFortune.png)

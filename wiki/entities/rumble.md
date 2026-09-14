---
title: "ランブル"
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
  - role-mage
champion_id: "Rumble"
champion_key: "68"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "ヒート"
image_path: "raw/assets/champions/Rumble.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rumble.png"
---

# ランブル

![[raw/assets/champions/Rumble.png|128]]

## 基本情報

- **英字ID：** `Rumble`
- **キー：** `68`
- **称号：** 戦慄の機甲兵
- **データversion：** `16.18.1`

## 紹介

ランブルは若くて気性の荒い発明家だ。この気骨のあるヨードルは、ガラクタの山を使って、たった一人の力で電撃ハープーンと焼夷ロケット弾を搭載した巨大なメカスーツを作り出した。廃品置き場で作り出された彼の発明品を冷笑する者がいても、ランブルは気にしない──いざとなれば、火炎放射器で黙らせてやればいいだけだ。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** ヒート

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 105 |
| `mp` | 150 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.85 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ポンコツタイタン：** スキルを使用するたび、ヒートが溜まっていく。ヒートゲージが50%に達すると「デンジャーゾーン」に突入し、すべての通常スキルに追加効果が付与される。100%に達すると「オーバーヒート」し、攻撃速度が増加して通常攻撃に追加ダメージがつくが、数秒間スキルを使えなくなる。

- **Q — スピットファイア：** 扇状の範囲を3秒間にわたって焼き払い魔法ダメージを与える。「デンジャーゾーン」突入時はダメージが増加する。
- **W — ジャンクシールド：** シールドを発生させてダメージを防ぎ、さらに移動速度が一瞬増加する。「デンジャーゾーン」突入時はシールド耐久値と、増加移動速度が増加する。
- **E — エレクトロハープーン：** 銛を発射し、対象を感電させて魔法ダメージとスロウ効果を与え、魔法防御を低下させる。2発まで発射できる。「デンジャーゾーン」突入時はダメージとスロウ効果が増加する。
- **R — イコライザー：** 複数のロケット弾を投下し、その地点を炎上させて敵にダメージとスロウ効果を与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rumble` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rumble.png)

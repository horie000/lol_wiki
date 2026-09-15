---
title: "ニーコ"
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
  - role-support
champion_id: "Neeko"
champion_key: "518"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Neeko.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Neeko.png"
---

# ニーコ

![[raw/assets/champions/Neeko.png|128]]

## 基本情報

- **英字ID：** `Neeko`
- **キー：** `518`
- **称号：** 不思議のカメレオン
- **データversion：** `16.18.1`

## 紹介

遥か昔に途絶えたヴァスタヤ部族の末裔であるニーコは、他者の風貌を拝借してどんな集団にでも溶け込むことができる。彼女は相手の感情を吸収し、即座に敵か味方かを判別することができるのだ。ニーコがどこにいるのか、あるいはニーコの正体が何者なのか、確信を持てる者はいない。だが彼女に害をなそうという者は、やがてその真の力を目の当たりにするだろう。そして原初の霊的魔法の威力を身をもって知ることになるのだ。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 1 |
| `magic` | 9 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 104 |
| `mp` | 450 |
| `mpperlevel` | 30 |
| `movespeed` | 340 |
| `armor` | 21 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 48 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 駆け巡る色彩：** 味方チャンピオンまたはマップ上の他のユニットの姿に化けることができる。行動妨害効果を受けるか、ダメージスキルを詠唱するか、チャンピオン以外のユニットに擬態した状態で敵タワーにダメージを与えるか、擬態したユニットの体力バーと同量のダメージを受けると擬態が解除される。

- **Q — 弾ける花弁：** 魔法ダメージを与える種を投げる。種はチャンピオンに当たるか敵ユニットをキルすると再度爆発する。
- **W — シェイプスプリッター：** 自動効果により通常攻撃3回ごとに追加魔法ダメージを与え、少しの間、移動速度が増加する。発動すると指定方向にクローンを送り出し、再発動するとクローンの進行方向を変えられる。
- **E — からまれ！：** 輪を飛ばして当たった敵すべてにダメージとスネア効果を与える。輪は敵をキルするかチャンピオンに触れると大きくなり、速度とスネア効果時間が増加する。
- **R — ポップブロッサム：** 少しの間準備してから宙に舞い上がり、周囲のすべての敵をノックアップさせる。さらに着地時に周囲の敵にダメージを与えてスタンさせる。擬態中は密かに準備を行える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Neeko` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Neeko.png)

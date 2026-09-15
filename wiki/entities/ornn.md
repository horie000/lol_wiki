---
title: "オーン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
champion_id: "Ornn"
champion_key: "516"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Ornn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ornn.png"
---

# オーン

![[raw/assets/champions/Ornn.png|128]]

## 基本情報

- **英字ID：** `Ornn`
- **キー：** `516`
- **称号：** 山の下の焔
- **データversion：** `16.18.1`

## 紹介

オーンは鍛冶と技巧を司る、フレヨルドの半神半人だ。彼は“炉床の家”と呼ばれる、火山の地下にある溶岩の洞窟をハンマーで叩いて造った巨大な鍛冶場で独り仕事に打ち込んでいる。そこで大釜を火にかけ、鉱石を溶かして精製し、比類なき武具を鍛造しているのだ。他の半神半人たち──特にボリベア──が大地を歩き定命の者たちの営みに干渉を始める時、オーンは立ち上がる。彼の信頼するハンマーと山脈の炎の力を手に、そういった問題児どもを元いた場所に帰すために。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 9 |
| `magic` | 3 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 660 |
| `hpperlevel` | 109 |
| `mp` | 341 |
| `mpperlevel` | 65 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 歩く鍛冶場：** オーンが獲得するあらゆる追加物理防御と追加魔法防御は、獲得量が増加する。 オーンはどこにいても、ゴールドを消費して消費アイテム以外のアイテムを作り出せる。 さらに、自身と味方のために名匠アイテムを作り出せる。

- **Q — 溶岩隆起：** 地面を叩きつけて裂け目を発生させ、敵ユニットにダメージを与えて移動速度を低下させる。少ししてから、裂け目の終端に溶岩の柱が発生する。
- **W — ふいごの息：** 前進し、炎を吐き出す。炎の最後の塊が当たった敵は「脆弱」状態になる。
- **E — 灼熱の突撃：** ダッシュして当たった敵ユニットにダメージを与える。ダッシュ中に地形にぶつかると周囲に衝撃波が発生し、敵ユニットにダメージを与えてノックアップする。
- **R — 鍛冶神の呼び声：** 指定地点に巨大な精霊を呼び出す。精霊はどんどん速度を上げながらオーンがいる方向に進んでくる。精霊にぶつかった敵ユニットはダメージを受けて移動速度が低下し、「脆弱」状態になる。スキルを再使用するとオーンが精霊に向かって突撃し、彼がぶつかった方向に精霊の進行方向を変える。この精霊に当たった敵ユニットはノックアップされて、最初と同量のダメージを受け、再び「脆弱」が適用される。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ornn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ornn.png)

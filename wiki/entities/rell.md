---
title: "レル"
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
  - role-support
champion_id: "Rell"
champion_key: "526"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Rell.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rell.png"
---

# レル

![[raw/assets/champions/Rell.png|128]]

## 基本情報

- **英字ID：** `Rell`
- **キー：** `526`
- **称号：** 鋼鉄の乙女
- **データversion：** `16.18.1`

## 紹介

黒薔薇団による残酷な実験の産物であるレルは、ノクサスの打倒を胸に誓った、反逆の生きた兵器である。レルの幼少期は、惨めで恐ろしいものだった。魔力を完成させ、兵器化するために、彼女は口にするのも憚られるような処置に耐えてきた──暴力的な逃亡を成し遂げ、自分を捕らえようとした者たちの多くを殺めてしまうまでは。犯罪者の烙印を押されたレルは、ノクサス兵を目にした瞬間に攻撃する。かつてのアカデミーの生存者を探す彼女は、従順な者たちを守りながら、かつての教師たちには無慈悲な死を与えている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 0 |
| `magic` | 0 |
| `difficulty` | 0 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 104 |
| `mp` | 320 |
| `mpperlevel` | 40 |
| `movespeed` | 315 |
| `armor` | 30 |
| `armorperlevel` | 4 |
| `spellblock` | 28 |
| `spellblockperlevel` | 1.8 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## データ品質上の注意

- `info` の4項目がすべて `0` である。未収録値か実値かは原典だけでは判定できない。

## アビリティ

- **パッシブ — 革新の鬨：** 通常攻撃またはスキルを命中させると追加で魔法ダメージを与え、対象から物理防御と魔法防御を奪う。

- **Q — 破鋼撃：** 直線上のユニットに魔法ダメージを与え、対象のシールドを破壊してスタンさせる。
- **W — フェロマンシー: 装着：** 騎馬形態: 「騎馬解除」をして、鎧をまとって突撃し、敵をノックアップさせて大量のシールドを獲得する。騎馬解除中は物理防御、魔法防御、攻撃速度、射程距離が増加するが、移動速度が低下する。 騎馬解除中: 鋼鉄の馬を形成して「騎馬形態」となり、瞬間的に移動速度が増加して、次に通常攻撃を行った敵をノックアップさせる。
- **E — 重槍突貫：** 自動効果: 非戦闘時の移動速度が増加する。 発動効果: 自身と味方1体の移動速度が徐々に増加する。敵またはお互いの方向に移動する場合、この増加量は2倍になる。次の通常攻撃で爆発を引き起こし、魔法ダメージを与える。
- **R — 磁気嵐流：** 猛烈な磁場を発生させ、周囲の敵を自身の方向に引き寄せる。その後も少しの間、継続的に周囲の敵を自身の方向に引き付け、効果時間をかけて魔法ダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rell` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rell.png)

---
title: "マルファイト"
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
  - role-mage
champion_id: "Malphite"
champion_key: "54"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Malphite.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malphite.png"
---

# マルファイト

![[raw/assets/champions/Malphite.png|128]]

## 基本情報

- **英字ID：** `Malphite`
- **キー：** `54`
- **称号：** モノリスの欠片
- **データversion：** `16.18.1`

## 紹介

マルファイトは混沌とした世界に祝福の秩序をもたらそうと苦闘する、生きた岩石の巨大な生物だ。モノリスとして知られる異世界のオベリスクに奉仕するかけらとして生まれた彼は、自らの強大な元素の力を使って先祖を何とか守ろうとしたが、その願いは果たせなかった。その後に続いた爆発で唯一の生き残りとなったマルファイトは、今ではルーンテラの移り気で柔らかい者たちの間で暮らしながら、種族の最後の生き残りにふさわしい新たな役割を見つけようとしている。

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 9 |
| `magic` | 7 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 665 |
| `hpperlevel` | 104 |
| `mp` | 280 |
| `mpperlevel` | 60 |
| `movespeed` | 335 |
| `armor` | 40 |
| `armorperlevel` | 4.95 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.3 |
| `mpregenperlevel` | 0.55 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.736 |

## アビリティ

- **パッシブ — グラナイトシールド：** 自身の最大体力の10%までのダメージを吸収する岩のシールドを生成する。このシールドは数秒間攻撃を受けないと再生する。

- **Q — サイズミックシャード：** 指定した敵に向かって岩の円盤を転がし、衝突時にダメージを与えて3秒間移動速度を奪う。
- **W — サンダークラップ：** 大きな力で攻撃してソニックブームを発生させる。その後数秒間、通常攻撃で自身の前方に余波が発生する。
- **E — グラウンドスラム：** 地面を強打して衝撃波を起こし、自身の物理防御に応じた魔法ダメージを与える。衝撃波に当たった敵は、攻撃速度が短時間低下する。
- **R — アンストッパブル・フォース：** 指定地点に勢いよく跳躍し、敵ユニットにダメージを与えてノックアップさせる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Malphite` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malphite.png)

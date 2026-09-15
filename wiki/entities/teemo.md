---
title: "ティーモ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-mage
champion_id: "Teemo"
champion_key: "17"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Teemo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Teemo.png"
---

# ティーモ

![[raw/assets/champions/Teemo.png|128]]

## 基本情報

- **英字ID：** `Teemo`
- **キー：** `17`
- **称号：** 俊足の斥候
- **データversion：** `16.18.1`

## 紹介

どのような恐ろしい危険や脅威が待っていようとも、ティーモは底知れぬ情熱と陽気さで世界を偵察し続ける。揺らぐことなき道徳観を持ったこのヨードルは、誇りを持ってひたむきに「バンドルの偵察兵の掟」を守っている。時には自らの行動が周囲に与える影響に気づかないこともあるが…。そもそも偵察兵の必要性自体を疑問視する声もある中、ひとつだけはっきりしていることがある──ティーモの強い信念を侮る者は、痛い目を見ることになる。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 3 |
| `magic` | 7 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 615 |
| `hpperlevel` | 104 |
| `mp` | 334 |
| `mpperlevel` | 25 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 500 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 9.6 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.38 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — やぶからヨードル：** 短時間行動せずにいると無限にインビジブル状態になる。茂みの中であれば移動中でもインビジブル状態になり、動き回っても解除されない。インビジブル状態が解除されると「奇襲モード」になり、攻撃速度が数秒間増加する。

- **Q — 目つぶしダーツ：** 強力な毒で敵1体の視力を低下させる。攻撃を受けた敵はダメージを受け、一定時間ブラインド状態になる。
- **W — 駆け足！：** 移動速度が増加。ただし、敵チャンピオンまたはタワーから攻撃を受けると効果が消滅する。数秒間、移動速度が増加。この間は、攻撃を受けても効果が持続する。
- **E — 毒たっぷり吹き矢：** 通常攻撃のたびに、対象を毒状態%i:OnHit%通常攻撃時効果にする。攻撃を受けた対象は命中時にダメージを受け、さらにその後4秒にわたって毎秒ダメージを受ける。
- **R — 毒キノコ：** バックパックに収納した「毒キノコ」を1つ取り出し、破裂性の毒トラップを仕掛ける。敵がトラップを踏むと毒霧が放出され、近くにいる敵ユニットをスロウ状態にし、継続ダメージを与える。毒キノコを他の毒キノコに投げつけると、バウンドしてさらに遠くに飛んでいく。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Teemo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Teemo.png)

---
title: "カリスタ"
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
  - data-dragon
champion_id: "Kalista"
champion_key: "429"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Kalista.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kalista.png"
---

# カリスタ

![[raw/assets/champions/Kalista.png|128]]

## 基本情報

- **英字ID：** `Kalista`
- **キー：** `429`
- **称号：** 復讐の槍
- **データversion：** `16.18.1`

## 紹介

報復を誓い、復讐を司る亡霊カリスタは、偽り人や裏切りし者を狩るためシャドウアイルから召喚される。裏切られた者が血にまみれて復讐を乞い叫んでも、カリスタはそのために自らの魂を代償として支払う覚悟がある者の呼びかけにしか応えない。そしてひとたび彼女の憤怒を向けられた者は決して破滅から逃れることはできない。非情なる狩手が交わした契約は常に、彼女の魂が放つ冷たい槍で完了の印を捺されるのだ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 4 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 114 |
| `mp` | 300 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 5.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 6.3 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4.5 |
| `attackspeed` | 0.694 |

## アビリティ

- **パッシブ — 戦の所作：** 通常攻撃または「貫魂の一投」の準備アクション中に移動指示を出すと、攻撃時にその方向へ跳躍して移動する。

- **Q — 貫魂の一投：** 高速で飛ぶ槍を投げる。命中した敵の体力がゼロになると、槍がその敵を貫通する。
- **W — 執念の霊魂：** カリスタと「魂盟の同志」が同じ対象を攻撃すると追加ダメージを与える。 スキルを発動すると霊魂を飛ばして周辺を偵察させ、霊魂の前方エリアを可視状態にする。
- **E — 引き裂く遺恨：** 通常攻撃するたびに、対象に槍の幻影が残る。発動すると槍の幻影が炸裂し、対象に刺さった槍の本数に比例するダメージを与え、スロウ効果を付与する。
- **R — 宿命の呼び声：** 「魂盟の同志」を強制的に自身の近くに吸い寄せる。カリスタの元に吸い寄せられた「魂盟の同志」は自分で指定した地点に突撃でき、範囲内にいる敵ユニットをわずかにノックバックさせる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kalista` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kalista.png)

---
title: "ザーヘン"
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
  - data-dragon
champion_id: "Zaahen"
champion_key: "904"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Zaahen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zaahen.png"
---

# ザーヘン

![[raw/assets/champions/Zaahen.png|128]]

## 基本情報

- **英字ID：** `Zaahen`
- **キー：** `904`
- **称号：** 沈まぬ者
- **データversion：** `16.18.1`

## 紹介

光と闇、相反する力の両方を操る堕ちし者、ザーヘンは、己を蝕もうとする穢れに抗い続けながら、同胞であるダーキンたちを狩る。かつては狂気を抑えるため、自ら望んでグレイヴの中に封印された。しかし今、彼は解き放たれ、心は高貴でありながらも、その目的において容赦はない。ザーヘンの戦いは永遠に続く内なる闘争だ。それでも彼が耐え抜く限り、ルーンテラを滅ぼさんとする者の上に、彼は再び立ち上がる。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 1 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 114 |
| `mp` | 350 |
| `mpperlevel` | 55 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8.15 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 戦威修養：** 敵チャンピオンに対する攻撃およびスキルで「不退転」のスタックを獲得し、スタックごとに攻撃力が増加する。「不退転」が最大スタックになると、攻撃力が増加し、復活できるようになる。

- **Q — ダーキングレイヴ：** 次の通常攻撃で2回斬りつけ、追加ダメージを与え、自身を回復する。スキルを再使用すると、次の通常攻撃で追加ダメージを与え、対象をノックアップさせる。
- **W — 戦慄の再臨：** 指定方向を突き刺し、命中した敵にダメージを与えた後、自身の方向へ引き寄せる。
- **E — 絢爛たる進撃：** 前方に突進し、周囲を斬りつける。
- **R — 無慈悲なる裁き：** 上昇した後、下方へ突き刺し、敵にダメージを与え、与えたダメージの一定割合の体力を回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中20位（上位15%）。体力640、物理防御36、攻撃力63、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zaahen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zaahen.png)

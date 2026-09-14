---
title: "ノクターン"
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
  - role-assassin
  - data-dragon
champion_id: "Nocturne"
champion_key: "56"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Nocturne.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nocturne.png"
---

# ノクターン

![[raw/assets/champions/Nocturne.png|128]]

## 基本情報

- **英字ID：** `Nocturne`
- **キー：** `56`
- **称号：** 終わりなき悪夢
- **データversion：** `16.18.1`

## 紹介

知覚を持つあらゆる生物が見る悪夢が融合してできたノクターンとして知られるこの恐ろしい存在は、純悪の根源的な力である。混沌として明確な姿は持たず、顔の無い影の中に冷たい目が浮かんでおり、複数の不気味な刃を持っている。霊的領域から脱したノクターンは、目覚め始めた世界に降り立ち、真の闇にしか存在しない恐怖を糧にして生きている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 109 |
| `mp` | 275 |
| `mpperlevel` | 35 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.721 |

## アビリティ

- **パッシブ — 夢幻斬：** 数秒ごとに次の攻撃が範囲攻撃になり、周囲の敵に追加物理ダメージを与えて自身の体力を回復する。 通常攻撃するたびにクールダウンが短縮する。

- **Q — 闇の手：** 指定方向に影の刃を投げてダメージを与える。刃の軌跡や命中した敵チャンピオンが残す影の上にいる間はユニットをすり抜けられ、移動速度と攻撃力が増加する。
- **W — 漆黒の帳：** 自動効果: 刃に念が送られ、攻撃速度が増加する。 発動効果: 魔法のバリアを張って敵のスキルを一度だけ無効化する。無効化成功後は自動効果による攻撃速度の増加率が倍になる。
- **E — 底知れぬ恐怖：** 対象におぞましい悪夢を見せ、毎秒ダメージを与える。効果終了までに範囲内から抜け出せなかった対象にはフィアー効果を与える。
- **R — パラノイア：** すべての敵チャンピオンの視界が悪化し、自分以外の視界を失う。効果中、指定した近くの敵チャンピオンに突撃して攻撃できる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中24位（上位15%）。体力640、物理防御36、攻撃力62、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nocturne` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nocturne.png)

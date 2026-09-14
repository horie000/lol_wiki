---
title: "ノーチラス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-support
  - data-dragon
champion_id: "Nautilus"
champion_key: "111"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Nautilus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nautilus.png"
---

# ノーチラス

![[raw/assets/champions/Nautilus.png|128]]

## 基本情報

- **英字ID：** `Nautilus`
- **キー：** `111`
- **称号：** 深海の巨人
- **データversion：** `16.18.1`

## 紹介

ビルジウォーターに最初の桟橋ができたころからすでに伝説となっていた孤独な男──「ノーチラス」の名で知られる防具に包まれた大男は、ブルーフレイム・アイルの沖の暗い海域をさまよっている。大昔の裏切りに突き動かされている彼は何の前触れもなく攻撃を仕掛け、巨大な錨を振り回しては、不運な者を助け、強欲な者を破滅へと引きずり込む。「ビルジウォーターの供物」を払わなかった者のもとに現れては、彼らを道連れにして波間へと沈むのだという。そうして「何人たりとも深海から逃れることはできない」という鉄の掟を知らしめているのだ。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 6 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 646 |
| `hpperlevel` | 100 |
| `mp` | 400 |
| `mpperlevel` | 47 |
| `movespeed` | 325 |
| `armor` | 39 |
| `armorperlevel` | 4.95 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.65 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.706 |

## アビリティ

- **パッシブ — 鉄の錨：** 対象に最初に行う通常攻撃は与える物理ダメージが増加し、短時間スネア効果を与える。

- **Q — 錨投げ：** 前方に錨を投げる。敵に命中すると自身と対象を同時に引き寄せ、魔法ダメージを与える。錨が地形に命中した場合、自身を錨の地点まで引き寄せる。
- **W — 大海の激憤：** 一時的にシールドを獲得する。シールドが持続している間は通常攻撃が対象と周囲の敵に継続ダメージを与える。
- **E — 粉砕水：** 自身の周囲に3回爆発する衝撃波を発生させる。爆発のたびに敵にダメージとスロウ効果を与える。
- **R — 爆雷発射：** 錨を地面にたたきつけ、狙った敵チャンピオンを追尾する爆雷を発射する。爆雷は対象を追尾しながら、通った場所に衝撃波を引き起こし、巻き込んだ敵ユニットに魔法ダメージとノックアップを与える。爆雷が対象に命中すると爆発がおき、対象にノックアップとスタンを付与する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nautilus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nautilus.png)

---
title: "レオナ"
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
champion_id: "Leona"
champion_key: "89"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Leona.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leona.png"
---

# レオナ

![[raw/assets/champions/Leona.png|128]]

## 基本情報

- **英字ID：** `Leona`
- **キー：** `89`
- **称号：** 暁光の戦士
- **データversion：** `16.18.1`

## 紹介

太陽の熱をもって闘志を燃やすレオナは、天陽の剣と暁の盾をもって霊峰ターゴンを守るソラリの騎士だ。彼女の肌は星の火のように煌めき、その瞳は内なる天の神髄の力で燃えている。黄金の鎧に身を包み、太古の真実という重責を背負う彼女は、ある者には啓示を、またある者には死をもたらす。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 646 |
| `hpperlevel` | 101 |
| `mp` | 302 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 43 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.9 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — サンライト：** 攻撃スキルが命中した敵に1.5秒間「サンライト」の効果を付与する。この状態の対象に味方チャンピオンがダメージを与えると「サンライト」を消費して追加魔法ダメージを与える。

- **Q — シールド・オブ・デイブレイク：** 次の通常攻撃時に盾を使って攻撃し、追加魔法ダメージを与えて対象にスタン効果を付与する。
- **W — エクリプス：** 自身の体を盾で保護し、ダメージ軽減率、物理防御、魔法防御を増加させる。効果時間終了時に近くに敵がいる場合は、その全員に魔法ダメージを与え、さらにシールドの効果時間が延長される。
- **E — ゼニスブレード：** 剣から太陽のエネルギーを放ち、直線上のすべての敵に魔法ダメージを与える。最後に命中した敵チャンピオンに一時的なスネア効果を付与し、レオナが近くまで素早く移動する。
- **R — ソーラーフレア：** 指定地点に太陽の力を呼び寄せ、効果範囲内の敵ユニットにダメージを与える。範囲の中心部にいる敵にスタン効果を与え、外側にいる敵にはスロウ効果を与える。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Leona` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leona.png)

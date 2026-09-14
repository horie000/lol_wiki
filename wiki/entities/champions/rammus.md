---
title: "ラムス"
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
  - data-dragon
champion_id: "Rammus"
champion_key: "33"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Rammus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rammus.png"
---

# ラムス

![[raw/assets/champions/Rammus.png|128]]

## 基本情報

- **英字ID：** `Rammus`
- **キー：** `33`
- **称号：** アーマージロ
- **データversion：** `16.18.1`

## 紹介

ラムス──謎に包まれたこの生き物を、聖なる存在と崇拝してやまない者は多い。一方で、ただの動物に過ぎないと見る者もいる。その素性は誰にも分からない。人々は棘の付いた甲羅を持つラムスについて様々な説を打ち立てる。ラムスの姿が確認された場所では、半神だ、いや神聖なる神の遣いだ、魔術で姿を変えられたただの獣だ、などと論争が巻き起こる。真実がどうであれラムスは沈黙を守り、独り砂漠を彷徨って、他者と関わろうとはしない。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 10 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 100 |
| `mp` | 310 |
| `mpperlevel` | 33 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.85 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.215 |
| `attackspeed` | 0.7 |

## アビリティ

- **パッシブ — トゲトゲ：** 自身の物理防御と魔法防御に応じて攻撃力が増加する。

- **Q — ころころ：** 体を丸めて高速回転し、移動速度が増加する。衝突した敵に突進してダメージを与え、スロウ効果を付与する。
- **W — かたくなる：** 防御体勢を取って物理防御と魔法防御を大幅に増加させ、通常攻撃を行ってきた相手にダメージを跳ね返す。
- **E — ぴりぴり：** 敵チャンピオンまたは中立モンスターをタウントし、固い甲羅に無謀な攻撃をさせる。
- **R — どーんどーん：** ジャンプしてから指定地点に勢いよく着地し、敵に魔法ダメージとスロウ効果を与える。「ころころ」発動中に使用した場合、範囲の中心付近にいる敵にはノックアップも与える。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rammus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rammus.png)

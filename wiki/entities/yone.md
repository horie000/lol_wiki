---
title: "ヨネ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-assassin
champion_id: "Yone"
champion_key: "777"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "つむじ風"
image_path: "raw/assets/champions/Yone.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yone.png"
---

# ヨネ

![[raw/assets/champions/Yone.png|128]]

## 基本情報

- **英字ID：** `Yone`
- **キー：** `777`
- **称号：** 忘られざる者
- **データversion：** `16.18.1`

## 紹介

生前、ヨネはヤスオの腹違いの兄であり、村の剣術道場で名を知られた生徒だった。しかし弟の手で殺されたヨネは、霊界の邪悪な存在に狙われ、その悪しき者が持っていた刀を使って殺すことを余儀なくされた。そして悪魔の仮面を被る呪いにかけられたヨネは、自らが何者に変わったのかを理解するために、そうした邪悪な存在を飽くことなく狩り続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** つむじ風

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 4 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 105 |
| `mp` | 500 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 狩鬼道：** 通常攻撃2回ごとに魔法ダメージを与える。さらに、クリティカル率が増加する。

- **Q — 斬命刀：** 前方に突きを放ち、直線上の敵すべてにダメージを与える。 このスキルが命中すると「つむじ風」のスタックを数秒間得る。2スタックになると、「斬命刀」を使用した際、一陣の風をまとって前方にダッシュし、敵をノックアップさせる。
- **W — 霊断刀：** 前方をなぎ払い、扇状の範囲内にいるすべての敵にダメージを与え、シールドを獲得する。シールド量はなぎ払いが命中したチャンピオンの数に応じて増加する。 攻撃速度が増加すると「霊断刀」のクールダウンと詠唱時間が短縮される。
- **E — 縛魂の解放：** 自身の霊魂が肉体を離れ、移動速度が増加する。スキル終了時にこの霊魂は肉体に強制的に戻り、霊魂として与えたダメージの一部をもう一度与える。
- **R — 冥封一閃：** 直線上の最後にいるチャンピオンの背後に強力な斬撃を与えてブリンクし、当たった敵すべてを自身の方向に引き寄せる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yone` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yone.png)

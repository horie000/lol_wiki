---
title: "サイラス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
  - role-assassin
champion_id: "Sylas"
champion_key: "517"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Sylas.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sylas.png"
---

# サイラス

![[raw/assets/champions/Sylas.png|128]]

## 基本情報

- **英字ID：** `Sylas`
- **キー：** `517`
- **称号：** 解き放たれし者
- **データversion：** `16.18.1`

## 紹介

デマーシアの貧しい地域に育ったドレグボーンのサイラスは、この大都の闇を象徴する存在となった。少年期の彼には隠れた魔力を発見する才能があり、それゆえに悪名高きメイジ狩りに重用されていた。だがある時、その力をメイジ狩りたちに向けて用いたために投獄されてしまった。やがて脱獄に成功した彼は、今では強硬派の革命家となり、周囲の魔力を盗み取って自分がかつて仕えた王国を破壊しようとしている──そして彼に従う追放されたメイジたちの数は、日を追うごとに増えているのだ。

## 分類

- **役割タグ：** `Mage`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 122 |
| `mp` | 400 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 29 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.55 |
| `attackrange` | 175 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.645 |

## アビリティ

- **パッシブ — ペトリサイトバースト：** スキル使用後、「ペトリサイトバースト」がチャージされる。通常攻撃でチャージを解放し、魔力のこもった鎖を旋回させて当たった敵に追加魔法ダメージを与える。「ペトリサイトバースト」のチャージを保持している間は攻撃速度が増加する。

- **Q — 鎖の鞭：** 指定地点で交わるように2本の鎖を叩きつけ、敵にダメージとスロウ効果を与える。 少ししてから交差地点で魔法エネルギーが爆発し、ダメージを与える。
- **W — 王殺し：** 魔法エネルギーを纏って敵に突進し、ダメージを与える。対象がチャンピオンの場合は自身の体力を回復する。
- **E — 逃亡/拉致：** 指定地点にダッシュする。再発動で鎖を投げつけて命中した敵に向かって自身を引き寄せる。
- **R — 乗っ取り：** 敵のアルティメットスキルを奪い、自由に発動できる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sylas` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sylas.png)

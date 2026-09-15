---
title: "ルブラン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-assassin
  - role-mage
champion_id: "Leblanc"
champion_key: "7"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Leblanc.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leblanc.png"
---

# ルブラン

![[raw/assets/champions/Leblanc.png|128]]

## 基本情報

- **英字ID：** `Leblanc`
- **キー：** `7`
- **称号：** 幻惑の奇術師
- **データversion：** `16.18.1`

## 紹介

黒薔薇団の他のメンバーにとっても謎に包まれた存在であるルブランだが、その名前ですら、ノクサス建国初期からあらゆる人々や出来事を操ってきた色白な女が持つ複数の名前のひとつにすぎない。自らの分身を発生させる魔法を使い、この魔術師はいつでもどこにでも姿を現すことが可能で、複数の場所に同時に存在することもできる。その正体と同じく、常に裏で画策を続けるルブランの真の動機は誰にもわからない。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 4 |
| `magic` | 10 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 598 |
| `hpperlevel` | 108 |
| `mp` | 400 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 鏡像：** 自身の体力が40%を下回ると1秒間インビジブル状態になり、「鏡像」を発生させる。「鏡像」はダメージを与えず、最大8秒間持続する。

- **Q — シジルマリス：** 刻印を飛ばし、対象にダメージを与えて3.5秒間マークする。マークした対象にスキルでダメージを与えると、刻印が爆発して追加ダメージを与える。どちらかのダメージで対象をキルした場合、マナコストが回復して、このスキルの残りクールダウンの一部が短縮される。
- **W — ディストーション：** 指定地点にすばやく移動し、周囲の敵にダメージを与える。4秒以内にこのスキルを再使用すると、最初の位置に戻ることができる。
- **E — エーテルチェイン：** 鎖の幻影を放ち、最初に当たった敵を鎖で繋ぐ。1.5秒間繋いだままにすると、追加ダメージとスネアを与える。
- **R — 再演：** 選択した通常スキルの偽バージョンを使用する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Leblanc` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Leblanc.png)

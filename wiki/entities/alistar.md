---
title: "アリスター"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-support
champion_id: "Alistar"
champion_key: "12"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Alistar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Alistar.png"
---

# アリスター

![[raw/assets/champions/Alistar.png|128]]

## 基本情報

- **英字ID：** `Alistar`
- **キー：** `12`
- **称号：** ミノタウロスの戦士
- **データversion：** `16.18.1`

## 紹介

屈強な戦士として恐れられるアリスターは自分の部族を滅ぼしたノクサス帝国に復讐を誓っている。彼は奴隷となり、闘士として戦わされていたものの、不屈の意思の強さで理性を維持し、ただの獣に成り下がってしまうことは免れた。かつての主人たちの鎖から解放された今、彼は虐げられた者や不遇の者たちのために、己の角と蹄と怒りを武器にして戦っている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 9 |
| `magic` | 5 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 685 |
| `hpperlevel` | 120 |
| `mp` | 350 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 40 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.125 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 戦士の咆哮：** 敵チャンピオンをスタンさせるか弾き飛ばした時、または周囲で敵ユニットが倒されると「咆哮」をチャージする。最大までチャージされると自身および近くにいるすべての味方チャンピオンの体力を回復する。

- **Q — 圧砕：** 地面をたたきつけ、周囲にいる敵ユニットにダメージを与えてノックアップする。
- **W — 頭突き：** 対象に「頭突き」を食らわせてダメージを与え、ノックバックさせる。
- **E — 踏破：** 周囲の敵を踏みつけてユニットをすり抜けるようになる。これでチャンピオンにダメージを与えた場合、スタックを1つ獲得。スタックが最大になるとチャンピオンに対する次の通常攻撃に追加魔法ダメージとスタン効果を付与する。
- **R — 不屈の意志：** 荒々しい雄叫びをあげ、自身に付与された行動妨害効果をすべて解除する。効果時間中は自身が受ける物理ダメージと魔法ダメージを軽減する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Alistar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Alistar.png)

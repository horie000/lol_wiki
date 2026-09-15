---
title: "トリンダメア"
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
champion_id: "Tryndamere"
champion_key: "23"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "フューリー"
image_path: "raw/assets/champions/Tryndamere.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tryndamere.png"
---

# トリンダメア

![[raw/assets/champions/Tryndamere.png|128]]

## 基本情報

- **英字ID：** `Tryndamere`
- **キー：** `23`
- **称号：** 孤高の蛮王
- **データversion：** `16.18.1`

## 紹介

決して鎮まることのない激しい怒りに駆り立てられたトリンダメアは、かつては暗雲のかかる未来に備えるために北部で最強の戦士たちに次々と戦いを挑み、フレヨルド中に知られる存在だった。この激怒する蛮族は何年も同胞を滅ぼした者への復讐を果たそうとしていたが、最近になってアヴァローサンの戦母、アッシュの仲間となり、彼女の部族と共に生活するようになった。彼の人間離れした腕力と精神力は伝説となっており、幾度となく絶対的に不利な状況を乗り越えて新たな仲間たちに勝利をもたらしている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 696 |
| `hpperlevel` | 108 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 戦場の咆哮：** 通常攻撃やクリティカル発生、敵にとどめを刺した際に「フューリー」がたまっていく。 自動効果: たまった「フューリー」の量に応じてクリティカル率が増加する。 たまった「フューリー」を消費して「血の欲望」を強化して発動できる。

- **Q — 血の欲望：** 戦闘で負傷するほど攻撃力が増加する。発動させるとたまっている「フューリー」を消費し、体力を回復する。
- **W — 嘲りの叫び：** 敵を嘲る言葉を叫び、周囲にいる敵チャンピオンの攻撃力を低下させる。トリンダメアに背を向けている敵は、移動速度も低下する。
- **E — スピンスラッシュ：** 指定地点へ回転しながら移動し、移動中に当たった敵ユニットにダメージを与える。
- **R — 不死の憤激：** 戦い続けたいという強い欲望に取りつかれ、一定時間はどれだけダメージを受けても体力がゼロにならない。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Tryndamere` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tryndamere.png)

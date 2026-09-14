---
title: "フィズ"
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
  - role-fighter
champion_id: "Fizz"
champion_key: "105"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Fizz.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fizz.png"
---

# フィズ

![[raw/assets/champions/Fizz.png|128]]

## 基本情報

- **英字ID：** `Fizz`
- **キー：** `105`
- **称号：** 波間のトリックスター
- **データversion：** `16.18.1`

## 紹介

フィズはビルジウォーターを囲む岩礁の間に住む水陸両性のヨードルだ。彼は迷信深い船長が海に投げる捧げものをくすめては返して遊んでいるが、どんな荒くれの船乗りでも彼を敵に回そうとはしない。というのも、このすばしこい生き物の恐ろしさを侮った者たちの話が数多く伝わっているからだ。気まぐれな海の精霊だと勘違いされがちだが、彼は深海の獣どもを操ることもできるらしく、敵も味方もなく、人々をからかっては楽しんでいる。

## 分類

- **役割タグ：** `Assassin`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 7 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 106 |
| `mp` | 317 |
| `mpperlevel` | 52 |
| `movespeed` | 335 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.1 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — シーファイター：** ユニットをすり抜け、すべてのダメージソースから受けるダメージを一定量軽減させる。

- **Q — ウニトゲストライク：** 対象に向かって突進し反対側へ突き抜ける。命中した対象に魔法ダメージを与え、通常攻撃時効果を発動する。
- **W — シートライデント：** 自動効果で通常攻撃が敵を出血させ、数秒間かけて魔法ダメージを与える。発動すると次の通常攻撃を強化して追加ダメージを与え、少しの間だけその後の通常攻撃が強化される。
- **E — プレイ/トリックスター：** 地面に槍を突き立て飛び上がった後、槍の上に器用に乗って敵から対象指定されなくなる。この状態からその場に着地、または再度ジャンプして別の指定地点に着地し範囲内の敵にダメージを与える。
- **R — フィッシング：** 撒き餌として魚を1匹発射する。魚が命中した敵チャンピオンはスロウ状態になり周囲を魚が旋回する。短時間後、地面から巨大なサメが飛びだして対象をノックアップさせ、周囲の敵を横に跳ね飛ばす。命中した敵は全員魔法ダメージとスロウ効果を受ける。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Fizz` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fizz.png)

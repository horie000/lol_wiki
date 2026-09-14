---
title: "ヴァイ"
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
champion_id: "Vi"
champion_key: "254"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Vi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vi.png"
---

# ヴァイ

![[raw/assets/champions/Vi.png|128]]

## 基本情報

- **英字ID：** `Vi`
- **キー：** `254`
- **称号：** ピルトーヴァーの用心棒
- **データversion：** `16.18.1`

## 紹介

ゾウンの貧民街で育ったヴァイは、直情的で頭に血が上りやすく、権力者などというものをほとんど意にも介さない、恐るべき女だ。またかつては若さゆえにしばしば問題を引き起こし、スティルウォーター刑務所で過ごした時間も長いため、生き延びるための知恵に長けた存在でもある。そんな彼女だが、現在はピルトーヴァーの執行官たちと組んで、治安を乱す側ではなく維持する側に立っている。その腕に装着されたヘクステック式パワーグラブは、犯罪者だろうが頑丈な壁だろうが簡単にぶち抜いてしまうだろう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 105 |
| `mp` | 295 |
| `mpperlevel` | 65 |
| `movespeed` | 340 |
| `armor` | 30 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 10 |
| `hpregenperlevel` | 1 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ケンカの作法：** 一定時間ごとにシールドをチャージし、スキルが敵に命中した瞬間に発動する。

- **Q — 真っすぐいってぶっとばす：** ガントレットにエネルギーをチャージした後、指定方向に猛ダッシュしながらパンチを繰り出す。敵ユニットに命中するとダメージとノックバックを与える。これは「メッタ打ち」の連続攻撃回数にもカウントされる。
- **W — メッタ打ち：** ヴァイのパンチが敵の物理防御を破って追加ダメージを与え、さらに自身の攻撃速度が増加する。
- **E — 無慈悲な連撃：** ヴァイが次の通常攻撃と同時に、衝撃波を放つ。衝撃波は通常攻撃をした対象の背後に広がり、触れた敵にダメージを与える。
- **R — 突入捜査：** 進路にいる敵を跳ね飛ばしながら指定した対象に向かって突撃し、接触と同時に対象をノックアップさせ、追いかけるように自身もジャンプしてから、地面に叩きつけてフィニッシュする。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vi.png)

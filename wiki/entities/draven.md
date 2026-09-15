---
title: "ドレイヴン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
champion_id: "Draven"
champion_key: "119"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Draven.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Draven.png"
---

# ドレイヴン

![[raw/assets/champions/Draven.png|128]]

## 基本情報

- **英字ID：** `Draven`
- **キー：** `119`
- **称号：** 栄光ある処刑人
- **データversion：** `16.18.1`

## 紹介

ノクサスでは清算人として知られる戦士たちは闘技場で血を流して戦って力を競い合うが、その中でドレイヴンほどの人気を得た者はいない。元兵士である彼は、独特のドラマチックな演出と、回転する斧の類まれな手さばきで観客を魅了する。自らの厚かましいほどの完璧さに夢中になり、ドレイヴンは自身の名を呼ぶ歓声がいつまでも帝国に響くように、現れる敵すべてに勝利することを誓っている。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 675 |
| `hpperlevel` | 104 |
| `mp` | 361 |
| `mpperlevel` | 39 |
| `movespeed` | 330 |
| `armor` | 29 |
| `armorperlevel` | 4.5 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 8.05 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — リーグ・オブ・ドレイヴン：** ドレイヴンが「回転斬斧」をキャッチするか、ミニオンおよび中立モンスター、タワーを破壊すると「名声」がたまる。敵チャンピオンを倒すとドレイヴンがスポットライトと喝采を浴び、「名声」の量に応じてゴールドを獲得する。

- **Q — 回転斬斧：** 次の通常攻撃に追加物理ダメージが付与される。対象に命中した斧は空中に跳ね返り、キャッチすると次の攻撃にも「回転斬斧」の効果がつく。 「回転斬斧」は2回までスタックする。
- **W — 血の疼き：** 移動速度と攻撃速度が増加する。増加移動速度は、時間の経過とともに急速に減少する。 「回転斬斧」をキャッチすると「血の疼き」のクールダウンがリセットされる。
- **E — 薙ぎ払い：** 斧を投げ、命中した敵に物理ダメージを与えて横に弾き飛ばし、スロウ効果を付与する。
- **R — 死の車輪：** 巨大な斧を2丁投げ、命中した全ユニットに物理ダメージを与える。敵チャンピオンに命中すると斧は自身のもとへ戻ってくる。斧が飛んでいる間に再度このスキルを発動すれば、途中で呼び戻すことも可能。ユニットに命中するごとに与えるダメージが減少するが、進行方向が変わると減少はリセットされる。敵の体力が「名声」のスタック数を下回る場合はとどめを刺す。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Draven` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Draven.png)

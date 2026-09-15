---
title: "トリスターナ"
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
  - role-assassin
champion_id: "Tristana"
champion_key: "18"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Tristana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tristana.png"
---

# トリスターナ

![[raw/assets/champions/Tristana.png|128]]

## 基本情報

- **英字ID：** `Tristana`
- **キー：** `18`
- **称号：** ヨードルの主砲
- **データversion：** `16.18.1`

## 紹介

他のヨードルたちは自らのエネルギーを発見や発明、またはただのいたずらに注いでいるが、トリスターナはいつだって偉大な戦士の冒険に憧れていた。彼女はルーンテラの様々な派閥や戦争の話を聞き、自分たちヨードルだって、そこで価値のある伝説を残せるはずだと考えた。信頼する愛砲「ブーマー」とともに初めてこの世界に足を踏み入れた彼女は、断固たる勇気と楽観主義を胸に戦闘に飛び込んでいく。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 5 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 102 |
| `mp` | 300 |
| `mpperlevel` | 32 |
| `movespeed` | 325 |
| `armor` | 30 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7.2 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — ドロー＆グロー：** レベルが上がるごとに射程が増加する。

- **Q — ラピッドファイア：** 高速で連射を行い、攻撃速度が数秒間増加する。
- **W — ロケットジャンプ：** 地面を砲撃した反動で指定地点へジャンプし、着地と同時に周辺のユニット全員にダメージを与え、短時間スロウ効果を付与する。
- **E — ヨードルグレネード：** 自動効果: ユニットを倒すと砲弾が炸裂して金属片が飛び散り、周辺の敵ユニットにダメージを与える。 発動効果: 対象にグレネードを付着させる。グレネードは数秒後に起爆し、対象と周囲のユニットにダメージを与える。
- **R — バスターショット：** 敵ユニット1体へ向けて巨大な砲弾を発射し、魔法ダメージを与えてノックバックさせる。対象に「ヨードルグレネード」が付着していた場合、爆発半径が2倍になる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Tristana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tristana.png)

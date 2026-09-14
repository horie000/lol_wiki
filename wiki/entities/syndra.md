---
title: "シンドラ"
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
champion_id: "Syndra"
champion_key: "134"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Syndra.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Syndra.png"
---

# シンドラ

![[raw/assets/champions/Syndra.png|128]]

## 基本情報

- **英字ID：** `Syndra`
- **キー：** `134`
- **称号：** 暗黒の女王
- **データversion：** `16.18.1`

## 紹介

シンドラは驚異的な力を操るアイオニアの恐るべきメイジである。幼いころには荒々しく制御のきかない魔法によって村の長たちを大いに悩ませていた。彼女は能力を制御する術を学ぶため遠い地へと送られたのだが、あるとき師であるはずの人物が自分の能力を弱体化させていたことを知ってしまった。裏切られ傷ついた心を黒いエネルギー球へと変換させるシンドラは、自分を操らんとする存在を残らず破滅させることを誓ったのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 583 |
| `hpperlevel` | 100 |
| `mp` | 480 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 絶大なる魔力：** チャンピオンレベルの上昇および敵へのダメージによって「怒りの破片」を集め、スキルをアップグレードできる。 ダークスフィア: チャージ数が1増加する ダークフォース: 追加確定ダメージを与える 闇の波導: 幅が増加し、すべての対象にスロウ効果を付与する 魔力の奔流: 体力が低下している対象にとどめを刺す

- **Q — ダークスフィア：** 闇のエネルギーの球体をつくりだし、敵に魔法ダメージを与える。 球体は一定時間消滅せず、他のスキルで操作することもできる。
- **W — ダークフォース：** 発生中の「ダークスフィア」または敵ミニオンや中立モンスター1体を持ち上げて投げ飛ばす。 投げ飛ばされた「ダークスフィア」およびミニオンや中立モンスターが命中した敵は魔法ダメージを受け、移動速度が低下する。
- **E — 闇の波導：** 敵ユニットおよび発生中の「ダークスフィア」をノックバックし、魔法ダメージを与える。 このスキルでノックバックした「ダークスフィア」が敵ユニットに命中した場合は、さらにスタン効果を付与する。
- **R — 魔力の奔流：** 発生中のすべての「ダークスフィア」で敵チャンピオン1体を集中攻撃する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Syndra` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Syndra.png)

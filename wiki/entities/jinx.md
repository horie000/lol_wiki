---
title: "ジンクス"
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
champion_id: "Jinx"
champion_key: "222"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Jinx.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jinx.png"
---

# ジンクス

![[raw/assets/champions/Jinx.png|128]]

## 基本情報

- **英字ID：** `Jinx`
- **キー：** `222`
- **称号：** 暴走パンクガール
- **データversion：** `16.18.1`

## 紹介

ジンクスは地下都市出身の、常軌を逸し、衝動的な犯罪者の一人だ。彼女は自らの過去が生んだ帰結に苛まれながらも、ピルトーヴァーとゾウンに独自のやり方で破壊と混沌をもたらし続けている。自作した強力な武器を使って派手な爆発を引き起こし、銃弾の雨を降らせ、行く先々で大混乱を生み出す彼女は、持たざる者たちを感化し、抵抗と反乱へといざなう存在でもあるのだ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 4 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 105 |
| `mp` | 260 |
| `mpperlevel` | 50 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 6.7 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 超エキサイティン！：** 敵チャンピオン、エピックジャングルモンスター、建造物のキルまたは破壊に貢献すると、移動速度と攻撃速度が大幅に増加する。

- **Q — スイッチング！：** スキルを使用するたび、通常攻撃が「パウパウガン」(ミニガン)と「フィッシュボーン」(ロケットランチャー)の間で切り替わる。「パウパウガン」で敵を攻撃し続けると攻撃速度が増加する。「フィッシュボーン」は射程が長く、範囲ダメージを発生させることができるが、攻撃速度が低下してマナを消費するようになる。
- **W — シビレーザー！：** スタンガンの一種であるシビレーザーを発射する。最初に命中した敵にダメージとスロウ効果を与え、さらに可視状態にする。
- **E — パックンチョッパー！：** 一列にならんだ爆雷を3個投げる。敵チャンピオンが爆雷に触れるとトラップが起動してスネア効果を与える。爆雷は触れられなくても5秒後に自動的に爆発し、周囲にいる敵にダメージを与える。
- **R — スーパーメガデスロケット！：** 指定方向にどこまでも直進してゆくスーパーメガデスロケットを発射する。 発射したロケット弾が敵チャンピオンに命中すればその場で爆発し、周囲の敵にもダメージを与える。ダメージは敵の現在体力が少ないほど威力が増加する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jinx` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jinx.png)

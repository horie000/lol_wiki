---
title: "ヘカリム"
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
  - role-tank
champion_id: "Hecarim"
champion_key: "120"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Hecarim.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hecarim.png"
---

# ヘカリム

![[raw/assets/champions/Hecarim.png|128]]

## 基本情報

- **英字ID：** `Hecarim`
- **キー：** `120`
- **称号：** 戦場の幻影
- **データversion：** `16.18.1`

## 紹介

生者の魂を永遠に狩るという呪いを受けたヘカリムは人間と獣が融合した亡霊だ。ブレスドアイルが影に飲まれた時、この誇り高き騎士は「破滅」の破壊的エネルギーに、騎士団と騎馬とともに消し去られてしまった。「黒き霧」がルーンテラに現れる時、彼は鎧をまとった蹄で敵を踏み砕き、虐殺に悦びを感じながら破滅的な突撃を指揮している。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 4 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 106 |
| `mp` | 280 |
| `mpperlevel` | 40 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 5.45 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — ウォーパス：** 増加移動速度の一定割合と同量だけ攻撃力が増加する。

- **Q — ランページ：** 周囲の敵を斬りつけて物理ダメージを与える。1体以上の敵にダメージを与えた場合、それ以降に行う「ランページ」のダメージが増加して、クールダウンが短縮される。
- **W — ソウルドレイン：** 物理防御と魔法防御を獲得する。また、周囲にいる敵に魔法ダメージを与えて、それらの敵が受けたあらゆるダメージの一定割合を体力として回復する。
- **E — チャージ：** 移動速度が短時間増加し、ユニットを通り抜けられるようになる。さらに次の通常攻撃に対象をノックバックする効果と、スキル発動後の移動距離に応じた追加物理ダメージが付与される。
- **R — スペクターズ・オンスロート：** 亡霊の騎士たちを召喚し、指定地点まで突撃して直線上の敵ユニットに魔法ダメージを与える。ヘカリムは到着と同時に衝撃波を放ち、付近の敵を恐怖に陥れて逃走させる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Hecarim` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hecarim.png)

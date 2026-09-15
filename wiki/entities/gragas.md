---
title: "グラガス"
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
  - role-mage
champion_id: "Gragas"
champion_key: "79"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Gragas.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gragas.png"
---

# グラガス

![[raw/assets/champions/Gragas.png|128]]

## 基本情報

- **英字ID：** `Gragas`
- **キー：** `79`
- **称号：** 騒乱の飲んだくれ
- **データversion：** `16.18.1`

## 紹介

陽気で立派な巨体を持つ、荒くれた風貌のグラガスは、常に人々の気持ちを明るくさせる新たな方法を探している醸造家だ。どこの出身なのかは不明だが、彼は完璧な調合を見つけるため、フレヨルドの誰も足を踏み入れない荒野で貴重な醸造材料を探している。向こう見ずで頑固な性格で、彼が始めた喧嘩の話は広く知られ、最後はいつも朝までどんちゃん騒ぎになって建物のあちこちが破壊されることになる。グラガスの現れるところ、必ずお祭り騒ぎと破壊が巻き起こる──いつもこの順番だ。

## 分類

- **役割タグ：** `Fighter`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 115 |
| `mp` | 400 |
| `mpperlevel` | 47 |
| `movespeed` | 330 |
| `armor` | 38 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.05 |
| `attackspeed` | 0.675 |

## アビリティ

- **パッシブ — ハッピーアワー：** 一定時間ごとにスキル使用時に体力を回復する。

- **Q — タル転がし：** 指定地点にタルを転がし、4秒後に爆発させる。タルは自分で起爆させることもできる。時間経過とともに爆発の威力が増加する。爆風を浴びた敵はスロウ状態になる。
- **W — 飲みすぎ注意：** 最新の醸造酒を1秒間試飲し、飲み終えると騒々しく好戦的になる。効果時間中は受けるダメージが軽減され、次の通常攻撃で付近のすべての敵に魔法ダメージを与える。
- **E — ボディスラム：** 指定方向へ突進し、最初に衝突した敵ユニットとその周囲の敵にダメージを与え、ノックバックとスタンを付与する。
- **R — ワシの奢りじゃ！：** 指定地点にタルを放り投げる。着弾したタルは大爆発し、爆発範囲内の敵ユニットにダメージを与えてノックバックさせる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gragas` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gragas.png)

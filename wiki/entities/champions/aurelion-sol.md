---
title: "オレリオン・ソル"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
  - data-dragon
champion_id: "AurelionSol"
champion_key: "136"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/AurelionSol.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/AurelionSol.png"
---

# オレリオン・ソル

![[raw/assets/champions/AurelionSol.png|128]]

## 基本情報

- **英字ID：** `AurelionSol`
- **キー：** `136`
- **称号：** 星を創りし者
- **データversion：** `16.18.1`

## 紹介

かつて何もない巨大な虚空であった宇宙に己が生み出した煌めく驚異を散りばめ、その恩寵を授けたオレリオン・ソル。しかし彼は今、領土拡大を目論む帝国の罠にかけられ、命ぜられるがままにその凄まじい力を振りかざしている。星を創るという本来の神聖なる役目への回帰を願うオレリオン・ソルは、必要とあらば天空から星をも引き寄せる。自由を再びその手に取り戻すために。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 90 |
| `mp` | 530 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 宇宙の創造者：** 攻撃スキルを敵に命中させると、「星屑」のスタックを獲得できる。このスタックは各スキルを恒久的に強化する。

- **Q — 星炎の息吹：** 数秒間詠唱して炎を吹き出し、最初に命中した敵にダメージを与え、その周囲の敵にはそれよりも少ないダメージを与える。敵に直接炎を吹きかけている間は、毎秒追加ダメージを与える。このダメージは獲得した「星屑」の数に応じて増加する。このスキルの対象がチャンピオンだった場合、「星屑」を獲得できる。
- **W — 天空への飛翔：** 飛翔して、指定方向に地形を超えて移動する。飛翔している間も、他のスキルを発動できる。また、飛翔中は「星炎の呼吸」のクールダウンおよび最大詠唱時間がなくなり、与えるダメージが増加する。 自身がダメージを与えた敵チャンピオンがその直後に倒されるたびに、このスキルの残りクールダウンが短縮される。 獲得した「星屑」の数に応じて、このスキルの最大射程が増加する。
- **E — 特異点：** ブラックホールを召喚して敵にダメージを与え、ゆっくりとその中心に向かって引き寄せる。敵がブラックホールの範囲内で倒されるたびに、「星屑」を獲得する。また、敵チャンピオンを範囲内に捕らえている間も、毎秒「星屑」を獲得できる。ブラックホールの中心部は、体力が最大体力の一定割合を下回っている敵に、とどめを刺すことができる。「星屑」の数に応じて「特異点」の効果範囲が増加し、とどめを刺せる体力割合の基準値が上昇する。
- **R — 星の邂逅/崩れ落つ天穹：** 星の邂逅: 地上に星を降らせ、その衝撃で敵に魔法ダメージを与えて、スタンさせる。また、命中した敵チャンピオン1体ごとに「星屑」を獲得する。「星屑」を一定数獲得すると、次に使用する「星の邂逅」が「崩れ落つ天穹」に変化する。 崩れ落つ天穹: 天空から巨大な星を引き寄せる。この星は落下時の効果範囲とダメージが増加しており、敵をスタンではなくノックアップさせる。また、落下時の効果範囲の端から衝撃波が広がり、命中した敵にダメージとスロウ効果を与える。獲得した「星屑」の数に応じて、「星の邂逅」と「崩れ落つ天穹」は落下時の効果範囲が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「星屑」のスタックが各スキルを恒久的に強化する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.AurelionSol` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/AurelionSol.png)

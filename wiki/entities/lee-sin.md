---
title: "リー・シン"
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
champion_id: "LeeSin"
champion_key: "64"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/LeeSin.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/LeeSin.png"
---

# リー・シン

![[raw/assets/champions/LeeSin.png|128]]

## 基本情報

- **英字ID：** `LeeSin`
- **キー：** `64`
- **称号：** 盲目の修行僧
- **データversion：** `16.18.1`

## 紹介

アイオニアの古代の格闘技をマスターしたリー・シンは、龍の精霊のエッセンスを操ってあらゆる困難を克服する厳しい訓練を積んだ格闘家だ。何年も前に視力を失ったが、この戦闘僧は聖なる均衡を破ろうとするあらゆる脅威から故郷を守るために、自らの人生を捧げている。深い瞑想から得た彼の力を侮る敵は、彼の伝説の燃える拳と炎の回し蹴りの餌食となるだろう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 108 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.651 |

## アビリティ

- **パッシブ — 練気：** スキル使用後、次の通常攻撃2回の攻撃速度が増加し、それぞれ気を回復する。

- **Q — 響掌/共鳴撃：** 響掌: 敵の位置を探るひずんだ音波を発射して、最初に当たった敵に物理ダメージを与える。また、命中してから3秒間は「共鳴撃」を発動できる。 共鳴撃: 「響掌」が命中した敵に素早く接近し、対象の減少体力に応じた物理ダメージを与える。
- **W — 守りの型/鉄の意志：** 守りの型: 指定した味方に素早く接近し、シールドを出現させてダメージから自身を守る。接近した相手が味方チャンピオンの場合、自身と相手を両方シールドで保護する。また、使用後は「鉄の意志」を発動できる。 鉄の意志: 厳しい修行の成果により、オムニヴァンプを獲得する。
- **E — 破風/縛脚：** 破風: 地面を強打して衝撃波を発生させることで魔法ダメージを与え、命中した敵ユニットを可視状態にする。「破風」が敵に命中した場合は、「縛脚」で追撃できる。 縛脚: 「破風」でダメージを受けた敵にスロウ効果を付与する。低下した移動速度は時間の経過とともに徐々に元に戻る。
- **R — 龍の怒り：** 対象に強力な回し蹴りを食らわせ、物理ダメージを与えると同時に後方へノックバックさせ、その際に衝突した敵ユニットにも物理ダメージを与える。ノックバックした対象と接触した敵は、短時間ノックアップ状態になる(この技はジェシー・パーリングにより伝授されたものだが、リー・シンはプレイヤーをゲームからキックすることはない…きっと)。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.LeeSin` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/LeeSin.png)

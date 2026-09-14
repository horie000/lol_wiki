---
title: "アーゴット"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Urgot"
champion_key: "6"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Urgot.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Urgot.png"
---

# アーゴット

![[raw/assets/champions/Urgot.png|128]]

## 基本情報

- **英字ID：** `Urgot`
- **キー：** `6`
- **称号：** ドレッドノート
- **データversion：** `16.18.1`

## 紹介

かつてノクサスの処刑人として数多くの死体を積み上げたアーゴットは、自らが仕えた帝国に裏切られた。ゾウンの地下深くにある監獄鉱山・ドレッジに送られ、鉄の鎖に繋がれた彼は、そこで強さの本当の意味をその身に刻まれることになる。その後、街中に大混乱をもたらした災害に乗じて脱出した彼は、今や闇社会に強烈な影を落とす存在となった。かつて自らをも繋いでいた鎖に縛られる者たちを扇動しながら、自分の新たな“ホーム”から価値なき連中を間引き、苦痛の試練を与えているのだ。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 102 |
| `mp` | 340 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 36 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 350 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.75 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — エコーフレイム：** 通常攻撃時と「パージ」発動時にその方向にある脚から散発的に炎が放射され、物理ダメージを与える。

- **Q — コラプトシェル：** 指定地点に榴弾を発射する。周囲の敵に物理ダメージを与えて、移動速度を低下させる。
- **W — パージ：** 最も近くにいる敵に速射攻撃を行う。その間は移動速度が低下する。直前に他のスキルで攻撃した敵チャンピオンを優先して攻撃し、「エコーフレイム」を発動する。
- **E — ディスデイン：** 指定方向に突撃しながらシールドを展開し、チャンピオン以外の敵ユニットを横に弾き飛ばす。敵チャンピオンを捕まえるとその場で止まり、そのチャンピオンを後方に投げ飛ばす。
- **R — デスグラインダー：** ケミドリルを発射する。ドリルは最初に当たった敵チャンピオンに突き刺さる。その敵チャンピオンの体力が一定未満になると、アーゴットが弱者とみなして処刑する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Urgot` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Urgot.png)

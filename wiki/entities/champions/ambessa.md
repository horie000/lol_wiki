---
title: "アンベッサ"
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
  - role-assassin
  - data-dragon
champion_id: "Ambessa"
champion_key: "799"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/Ambessa.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ambessa.png"
---

# アンベッサ

![[raw/assets/champions/Ambessa.png|128]]

## 基本情報

- **英字ID：** `Ambessa`
- **キー：** `799`
- **称号：** 戦乱の母
- **データversion：** `16.18.1`

## 紹介

メダルダの名を知る者なら誰もが、その家長であるアンベッサに敬意と恐れを抱いている。彼女はノクサスの将軍として、戦場における非情な力と恐れ知らずの決意という恐怖の組み合わせを体現する存在だ。家長としての彼女の役割にも大きな違いはなく、メダルダ家の権力を維持するためには抜け目のない狡猾さが必要となり、失敗や慈悲を許容する余地など残されていない。狼の非情ぶりを信奉する彼女は一族の権威を守るためなら手段を厭わない──それが自らの子への愛を犠牲にするとしても。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 0 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 110 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ドレイクハウンドの猛攻：** スキルを発動中に通常攻撃または移動操作をすると、スキル発動後に短い距離をダッシュして、次の通常攻撃の射程距離、ダメージ、攻撃速度が増加し、気を回復する。

- **Q — カニングスイープ/サンダリングスラム：** 両手のドレイクハウンドを自身の前方に向かって半円状に振り回し、刃が当たった敵に追加ダメージを与える。敵に攻撃が命中すると、次に発動するこのスキルが短時間変化し、自身の前方に向かって両手のドレイクハウンドを直線状に叩きつけ、最初に命中した敵に追加ダメージを与える。
- **W — 断交：** シールドを獲得し、少しの間身構えた後地面を叩きつけて周囲の敵にダメージを与える。身構えている間にミニオン以外からのダメージをブロックしていた場合、このスキルの与えるダメージが増加する。
- **E — ラセレイト：** 両手のドレイクハウンドを自身の周囲に振り回し、付近の敵にダメージとスロウ効果を与える。このスキルから「ドレイクハウンドの猛攻」を発動すると、ダッシュ終了後にもう一度攻撃する。
- **R — 公開処刑：** 指定した直線上の最も遠い敵チャンピオンの場所までブリンクし、到着時に敵にサプレッション効果を付与する。その後、敵を地面に叩きつけ、ダメージを与えスタンさせる。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ambessa` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ambessa.png)

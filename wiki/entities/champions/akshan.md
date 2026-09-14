---
title: "アクシャン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-assassin
  - data-dragon
champion_id: "Akshan"
champion_key: "166"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Akshan.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akshan.png"
---

# アクシャン

![[raw/assets/champions/Akshan.png|128]]

## 基本情報

- **英字ID：** `Akshan`
- **キー：** `166`
- **称号：** 流浪の番人
- **データversion：** `16.18.1`

## 紹介

危機を前にしても片眉を少し上げるだけ。飄々とした伊達男のアクシャンは、正しき復讐を果たすべく、露出度高く、今日も颯爽と悪に立ち向かう。隠密戦闘に熟達している彼は敵の目から自由自在に姿をくらまし、もっとも予想外のタイミングで奇襲に転じることができる。アクシャンは、強い正義感と死を覆す伝説の武器を携え、ルーンテラの多くの悪党たちにけじめをつけさせている。「自分を許せないことはするな」という自分なりの道徳観に基づいて。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 0 |
| `magic` | 0 |
| `difficulty` | 0 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 107 |
| `mp` | 350 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4 |
| `attackspeed` | 0.638 |

## データ品質上の注意

- `info` の4項目がすべて `0` である。未収録値か実値かは原典だけでは判定できない。

## アビリティ

- **パッシブ — ダーティーファイト：** 通常攻撃かスキルを3回使用するごとに追加ダメージを与え、対象がチャンピオンだった場合はシールドを獲得する。 通常攻撃時に追加で通常攻撃を行う。ただし、その際のダメージは低下する。追加の通常攻撃をキャンセルすると、代わりに移動速度が増加する。

- **Q — 報復のブーメラン：** ブーメランを投げる。ブーメランは往路と復路でダメージを与え、敵に命中するたびに射程が増加する。
- **W — 義賊の流儀：** 自動効果で味方チャンピオンを倒した敵チャンピオンを「悪党」としてマークする。自分が「悪党」をキルすると、その「悪党」にキルされていた味方が復活し、追加ゴールドを獲得する。その際、すべてのマークが除去される。 発動するとカモフラージュ状態になり、「悪党」に向かっている間は移動速度とマナ自動回復が増加する。茂みの外に出るか地形から離れると、カモフラージュ状態がすぐに解除される。
- **E — ヒーロースイング：** 地形に向けてグラップルフックを発射し、その周囲をスイングしながら最も近い敵に繰り返し射撃を行う。チャンピオンか地形に衝突すると、その時点で飛び降りる。自ら早めに飛び降りることもできる。
- **R — 当然の報い：** 敵チャンピオンをロックオンして弾丸のチャージを開始する。チャージ終了時にすべての弾丸を発射し、最初に命中したチャンピオン、ミニオン、または建造物に減少体力に応じたダメージを与える。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Akshan` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akshan.png)

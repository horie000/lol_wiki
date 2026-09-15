---
title: "ソナ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-support
  - role-mage
  - data-dragon
champion_id: "Sona"
champion_key: "37"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Sona.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sona.png"
---

# ソナ

![[raw/assets/champions/Sona.png|128]]

## 基本情報

- **英字ID：** `Sona`
- **キー：** `37`
- **称号：** 沈黙の弦奏師
- **データversion：** `16.18.1`

## 紹介

ソナはデマーシアで随一の弦楽器エトワールの演奏家であり、その優雅な和音と活気あふれる旋律によってのみ自らの意思を伝えることができる。上品な態度で貴族たちの間で人気だが、彼女のうっとりするようなメロディーには実際に魔力が宿っており、デマーシアのタブーに触れるのではないかと考える者たちもいる。よそ者には何も聞こえないが親しい仲間だけはその旋律を理解することが可能で、彼女が爪弾くハーモニーは傷ついた味方を癒し、敵には予想もしないやり方でダメージを与える。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 2 |
| `magic` | 8 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 550 |
| `hpperlevel` | 91 |
| `mp` | 340 |
| `mpperlevel` | 45 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.3 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — パワーコード：** アッチェレランド: 通常スキルを使用し条件を満たすたびに、恒久的に通常スキルヘイストを獲得する。獲得可能な上限を超えると、スキルの使用成功時にアルティメットの残りクールダウン時間が短縮されるようになる。 パワーコード: スキルを数回発動するたびに、次の通常攻撃で追加魔法ダメージを与え、さらに最後に発動した通常スキルに応じた追加効果が発生する。

- **Q — ヒム・オブ・ヴァロー：** ソナが「ヒム・オブ・ヴァロー」を演奏し、音波を放って周囲の敵2体(チャンピオンか中立モンスターを優先)に魔法ダメージを与え、さらに一時的にオーラをまとって、接触した味方の次の攻撃に追加ダメージを付与する。
- **W — パーセヴァランス：** ソナが「パーセヴァランス」を演奏し、癒しの旋律によって自身と周囲の味方の体力を回復する。さらにしばらくオーラをまとい、接触した味方に一時的なシールドを与える。
- **E — セレリティ：** ソナが「セレリティ」を演奏して周囲の味方の移動速度を増加させる。さらに一時的にオーラをまとって、接触した味方チャンピオンの移動速度を増加させる。
- **R — クレッシェンド：** ソナが究極の和音を演奏し、触れた敵チャンピオンに魔法ダメージを与え、強制的に踊らせてスタン効果を付与する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 条件達成ごとに恒久的に通常スキルヘイストを獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 86試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 25.0%（n=12）、20〜25分 30.8%（n=13）、25〜30分 50.0%（n=18）、30〜35分 59.1%（n=22）、35分〜 52.4%（n=21）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sona` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sona.png)

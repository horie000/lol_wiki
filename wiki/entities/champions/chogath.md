---
title: "チョ＝ガス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Chogath"
champion_key: "31"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Chogath.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Chogath.png"
---

# チョ＝ガス

![[raw/assets/champions/Chogath.png|128]]

## 基本情報

- **英字ID：** `Chogath`
- **キー：** `31`
- **称号：** 未知なる恐怖
- **データversion：** `16.18.1`

## 紹介

チョ＝ガスはルーンテラの眩しい太陽の下に初めて現れた時から、純粋な飢えの衝動に突き動かされていた。チョ＝ガスはすべての生命を吸収しようとするヴォイドの欲望を完璧に具現化した存在であり、その複雑な身体機能は物質を素早く変換して自らの肉体の成長に繋げることが可能であり、筋肉は密度と大きさが増して、昆虫のような外皮は有機的なダイヤモンドのように固くなる。体が大きくなる必要がない時は、余った物質を剃刀のように鋭い槍にして吐き出し、獲物をあとで食べるために串刺しにしておく。

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 7 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 644 |
| `hpperlevel` | 94 |
| `mp` | 270 |
| `mpperlevel` | 60 |
| `movespeed` | 345 |
| `armor` | 38 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 7.2 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.44 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 暴食：** 敵ユニットを倒すたびに体力とマナが回復する。 この回復量はチョ＝ガスのレベルに応じて増加する。

- **Q — ラプチャー：** 指定地点に下から突き出るようにトゲを発生させる。効果範囲内の敵ユニットをノックアップさせてダメージを与え、スロウ効果を付与する。
- **W — スクリーム：** 扇形の範囲内にいる敵に恐ろしい叫声を浴びせ、魔法ダメージと数秒間のサイレンス効果を与える。
- **E — ヴォーパルスパイク：** 通常攻撃時に鋭いトゲを発射し、自身の前方にいる敵ユニットにダメージとスロウ効果を与える。
- **R — 捕食：** 敵ユニットを「捕食」して高い確定ダメージを与える。このスキルで敵ユニットを倒すと自身は巨大化して、最大体力が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中5位（上位15%）。体力644、物理防御38、攻撃力69、移動速度345。
  - 「捕食」で敵を倒すと巨大化し、最大体力が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Chogath` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Chogath.png)

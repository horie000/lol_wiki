---
title: "マルザハール"
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
champion_id: "Malzahar"
champion_key: "90"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Malzahar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malzahar.png"
---

# マルザハール

![[raw/assets/champions/Malzahar.png|128]]

## 基本情報

- **英字ID：** `Malzahar`
- **キー：** `90`
- **称号：** ヴォイドの予言者
- **データversion：** `16.18.1`

## 紹介

あらゆる生命の合一にすべてを捧げる熱狂的な予言者マルザハールは、新たに現れたヴォイドこそルーンテラを救済へと導く道なのだと固く信じている。シュリーマの不毛の砂漠の中、彼は心の中に囁いた声に導かれ、古代イカシアにたどり着いた。その廃墟の地で彼は、ヴォイドそのものの核たる闇を覗き込み、新たな力と目的を与えられた。今やマルザハールは己を「羊飼い」と考えており、人々にその福音を広めるための力…あるいは、地の底に棲むヴォイドの怪物たちを解き放つ力を振るうのである。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 9 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 101 |
| `mp` | 375 |
| `mpperlevel` | 28 |
| `movespeed` | 335 |
| `armor` | 18 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 500 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ヴォイドシフト：** 一定時間ダメージか行動妨害を受けていない時、マルザハールは強力なダメージ軽減と行動阻害無効を得る。この効果はダメージを受けた後も短期間継続する。

- **Q — ヴォイドコール：** ヴォイドへ繋がるゲートを2カ所に発生させる。発動から一瞬遅れてゲートからエネルギーが発射され、命中した敵ユニットに魔法ダメージを与える。敵チャンピオンに対しては、さらにサイレンス効果を与える。
- **W — ヴォイドスワーム：** 近くの敵を攻撃する「ヴォイドリング」を召喚する。
- **E — 虚性侵蝕：** 指定した対象の精神を痛みに悶え苦しむ幻覚で蝕み、継続ダメージを与える。対象に他のスペルを使用すると幻覚の効果が更新される。 幻覚に侵蝕されている敵が倒れると近くの敵ユニットに効果が伝染し、マルザハールのマナが回復する。幻覚に蝕まれている敵は、マルザハールが召喚した「ヴォイドリング」に狙われる。
- **R — ネザーグラスプ：** ダメージを与える負のエネルギーに満ちた領域上で敵チャンピオンにヴォイドのエネルギーを注ぎ込み、サプレッション効果を付与する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Malzahar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malzahar.png)

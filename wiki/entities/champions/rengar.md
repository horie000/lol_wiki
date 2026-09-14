---
title: "レンガー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-assassin
  - role-fighter
  - data-dragon
champion_id: "Rengar"
champion_key: "107"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Fighter"
resource_type: "フェロシティ"
image_path: "raw/assets/champions/Rengar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rengar.png"
---

# レンガー

![[raw/assets/champions/Rengar.png|128]]

## 基本情報

- **英字ID：** `Rengar`
- **キー：** `107`
- **称号：** 孤高のハンター
- **データversion：** `16.18.1`

## 紹介

獰猛にして卓越…ヴァスタヤのハンターであるレンガーは、危険な生物を追跡して殺す、そのスリルを味わうために生きている。彼は強く恐ろしい猛獣たち、そしてかつて彼自身の片目を奪ったヴォイドの怪物カ＝ジックスの痕跡を求めて、世界中をさまよい歩く。レンガーは食事や名誉のために狩りをすることはない。狩猟は彼にとって美であり、その美しさのためにこそ、彼は獲物を追跡し引き裂くのだ。

## 分類

- **役割タグ：** `Assassin`、`Fighter`
- **リソース種別：** フェロシティ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 104 |
| `mp` | 4 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 34 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 見えざる襲撃者：** 茂みの中にいると、通常攻撃で対象に向かって飛びつく。 スキルを使用するたびにフェロシティを獲得する。フェロシティが最大になると次に使用するスキルが強化される。 敵チャンピオンを倒すと「骨牙の首飾り」のトロフィーを獲得し、増加攻撃力を獲得する。

- **Q — 逆上：** 次の通常攻撃が追加ダメージを与える。 フェロシティボーナス: 与えるダメージと攻撃速度が増加。
- **W — 狩りの雄叫び：** レンガーが雄叫びをあげて周囲の敵にダメージを与え、直前に受けたダメージの一部を回復する。 フェロシティボーナス: 自身が受けている行動妨害効果を除去する。
- **E — 鉄球の投げ縄：** 投げ縄を投げ、最初に命中した対象に短時間スロウ効果を付与する。 フェロシティボーナス: 対象にスネア効果を付与する。
- **R — 狩猟本能：** 「狩猟本能」の覚醒によってレンガーがカモフラージュ状態となり、広範囲にわたって敵チャンピオンの位置を把握する。「狩猟本能」の覚醒中は移動速度が増加し、茂みの中にいなくても発見した敵に向かってジャンプ攻撃が可能になり、対象の物理防御を低下させる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - チャンピオン撃破時のトロフィーで増加攻撃力を獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rengar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rengar.png)

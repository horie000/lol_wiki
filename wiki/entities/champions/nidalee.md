---
title: "ニダリー"
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
  - role-mage
  - data-dragon
champion_id: "Nidalee"
champion_key: "76"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Nidalee.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nidalee.png"
---

# ニダリー

![[raw/assets/champions/Nidalee.png|128]]

## 基本情報

- **英字ID：** `Nidalee`
- **キー：** `76`
- **称号：** 半獣の狩人
- **データversion：** `16.18.1`

## 紹介

ジャングルの奥深くで育ったニダリーは凶暴なクーガーに自由に姿を変えることができる追跡の天才だ。女性でも獣でもなく、彼女は巧妙に仕掛けた罠と素早い投げ槍で、あらゆる侵入者から徹底して自分の縄張りを守っている。彼女は獲物の脚を傷つけて動けなくしてからクーガーの姿になって襲い掛かる──辛うじて襲撃を逃れて生き残った者たちの話によれば、剃刀のように鋭い本能と、さらに鋭い爪を持った野生の女だったという…

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 4 |
| `magic` | 7 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 109 |
| `mp` | 295 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.45 |
| `attackrange` | 525 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.22 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 品定め：** 茂みに入ると移動速度が2秒間10%増加する。さらに、距離1400の範囲内にいる可視状態の敵チャンピオンに向かって移動する場合は30%増加する。 敵チャンピオンまたは中立モンスターに「槍投げ」または「虎挟み」でダメージを与えると、対象に4秒間「マーキング」を付与し、真の視界を得る。この間、ニダリーの移動速度が10%増加し、さらに、「マーキング」中の対象に向かって移動する場合は30%増加する。また、対象に対する「テイクダウン」と「ジャンプ」の効果が増加する。

- **Q — 槍投げ/テイクダウン：** ヒト形態: 対象に向かって槍を投げる。ダメージ量は槍の飛距離に比例して大きくなる。 クーガー形態: 次の通常攻撃時に大量の追加ダメージを与える。ダメージ量は対象の失った体力に比例して増える。
- **W — 虎挟み/ジャンプ：** ヒト形態: 地面にトラップを仕掛ける。気づかず踏んだ敵は、ダメージを受けて可視状態になる。 クーガー形態: 指定方向にジャンプし、着地点周辺の範囲内にいる敵ユニットにダメージを与える。
- **E — 高揚/クロウ：** ヒト形態: クーガーの精霊を呼び出し、味方の体力を回復して短時間攻撃速度を増加させる。 クーガー形態: かぎ爪で攻撃し、自身の前方範囲内の敵ユニットにダメージを与える。
- **R — クーガーの心：** クーガーに変身し、特別なスキルを使用する。

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nidalee` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nidalee.png)

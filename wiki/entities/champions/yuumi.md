---
title: "ユーミ"
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
champion_id: "Yuumi"
champion_key: "350"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Yuumi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yuumi.png"
---

# ユーミ

![[raw/assets/champions/Yuumi.png|128]]

## 基本情報

- **英字ID：** `Yuumi`
- **キー：** `350`
- **称号：** マジカルキャット
- **データversion：** `16.18.1`

## 紹介

バンドルシティからやってきた魔法ネコのユーミは、かつてはノラという名のヨードル魔女の使い魔だった。ノラが謎の失踪を遂げたことで、ユーミはノラが所有していた意識を持つ本、「境界の書」の守り手となり、そのページのポータルを通って旅をしながら飼い主を探している。ノラの愛情を懐かしむユーミは、旅の連れとなる仲間を見つけては、光の盾と固い決意で彼らを守るのだった。ブックはユーミが脇道にそれないよう注意しているが、ユーミはすぐに昼寝やら魚やらの楽しそうなことに気をとられてしまう。だがそんなユーミも、最後はいつもき...

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 1 |
| `magic` | 8 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 500 |
| `hpperlevel` | 69 |
| `mp` | 440 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 25 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 425 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 10 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ネコはトモダチ：** 一定時間ごとに、通常攻撃またはスキルをチャンピオンに命中させると、自身および次にくっつく味方の体力が回復する。 くっついている間は、その味方との間に特別な絆が生まれる。絆が最も強い味方にくっついている間は、自身のスキルが強化される。

- **Q — きまぐれミサイル：** ミサイルを発射し、最初に当たった対象にダメージとスロウ効果を与える。発射後1.35秒以上経過すると、与えるダメージとスロウ効果が強化される。「ベストフレンド」にくっついている間は、ミサイルのスロウ効果が常に強化され、味方は通常攻撃時効果で追加ダメージを与えるようになる。 くっついている間は少しの間だけミサイルをマウスカーソルで操作できる。
- **W — ユー＆ミー！：** 対象の味方までダッシュして、タワー以外のすべてから対象指定不可状態になる。「ベストフレンド」にくっついている間は自身の体力回復/シールド効果が増加し、味方は通常攻撃時効果で体力が回復する。
- **E — バビューン！：** シールドを獲得して、移動速度と攻撃速度が増加する。くっついている場合は、自身ではなく味方にこの効果を与える。
- **R — ファイナルチャプター：** 詠唱してウェーブを5回発射する。ウェーブは対象が敵の場合はダメージを与えて、味方の場合は体力を回復する。詠唱中も移動と「バビューン！」の発動が可能で、味方にくっつくこともできる。「ベストフレンド」にくっついている間は、このスキルの発射方向をマウスで操作できる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 終盤寄り
- **対象試合：** 178試合、全体勝率 27.0%
- **時間帯別勝率：** 〜20分 8.7%（n=46）、20〜25分 23.3%（n=30）、25〜30分 24.3%（n=37）、30〜35分 37.1%（n=35）、35分〜 50.0%（n=30）
- **最高帯：** 35分〜（判定差 41.3ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 41.3%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yuumi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yuumi.png)

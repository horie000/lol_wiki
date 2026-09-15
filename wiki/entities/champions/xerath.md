---
title: "ゼラス"
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
  - role-mage
  - role-support
  - data-dragon
champion_id: "Xerath"
champion_key: "101"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Xerath.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Xerath.png"
---

# ゼラス

![[raw/assets/champions/Xerath.png|128]]

## 基本情報

- **英字ID：** `Xerath`
- **キー：** `101`
- **称号：** 超越魔神
- **データversion：** `16.18.1`

## 紹介

古代シュリーマの超越魔人ゼラスは、魔法の石棺の破片に封じられ、悶え苦しむ神秘のエネルギー体である。彼は数千年の間、砂漠の底に閉じ込められていたが、シュリーマが砂の中から現れたことで彼もまた古代の牢獄から解放された。力を手に入れたことで正気を失った彼は、自分のものであると信じてやまないものを自らの手で奪い取り、世界中の新しい文明を、自らが思い描いたそれで置き換えようと企んでいる。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 3 |
| `magic` | 10 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 575 |
| `hpperlevel` | 106 |
| `mp` | 400 |
| `mpperlevel` | 22 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6.85 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — マナサージ：** 一定時間ごとに、通常攻撃でダメージを与えると自身のマナを回復する。ユニットをキルするたびに、このクールダウンが短縮される。

- **Q — アルカノパルス：** 長射程のエネルギービームを発射し、命中したすべての敵ユニットに魔法ダメージを与える。
- **W — デストラクションアイ：** 神秘のエネルギーを空から撃ち落とし、範囲内の敵ユニットにスロウと魔法ダメージを与える。範囲内の中心にいる敵ユニットは、より大きなダメージとスロウを受ける。
- **E — ショックオーブ：** 敵ユニットに魔法ダメージとスタンを与える。
- **R — アーケーンライト：** 移動できなくなるかわりに、超長距離射程の攻撃を行えるようになる。

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

- **観測分類：** 序盤寄り
- **対象試合：** 501試合、全体勝率 55.5%
- **時間帯別勝率：** 〜20分 65.1%（n=86）、20〜25分 54.0%（n=63）、25〜30分 53.0%（n=100）、30〜35分 54.3%（n=127）、35分〜 52.8%（n=125）
- **最高帯：** 〜20分（判定差 12.3ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 12.3%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Xerath` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Xerath.png)

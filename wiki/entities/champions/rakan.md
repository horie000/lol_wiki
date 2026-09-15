---
title: "ラカン"
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
  - data-dragon
champion_id: "Rakan"
champion_key: "497"
data_version: "16.18.1"
roles:
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Rakan.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rakan.png"
---

# ラカン

![[raw/assets/champions/Rakan.png|128]]

## 基本情報

- **英字ID：** `Rakan`
- **キー：** `497`
- **称号：** 魅惑の翼
- **データversion：** `16.18.1`

## 紹介

気まぐれで魅力的なラカンは、ヴァスタヤの悪名高きトラブルメーカーであり、ロトラン部族史上最高のバトルダンサーだ。アイオニア高地に住む人間たちにとって、彼の名はずっと、無礼講のお祭り、どんちゃん騒ぎ、アナーキーな音楽などと同意義だった。この活力に溢れた旅芸人が反逆者ザヤのパートナーであり、彼女の大義に命を捧げているなどと考える者はまずいない。

## 分類

- **役割タグ：** `Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 99 |
| `mp` | 315 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 30 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 300 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8.75 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.635 |

## アビリティ

- **パッシブ — 神秘の翼：** ラカンは定期的にシールドを獲得する。

- **Q — キラリ羽根：** 魔法の羽根を投げて魔法ダメージを与える。敵チャンピオンかエピックモンスターに当たると、ラカンが味方を回復できる。
- **W — 華麗なる登場：** 指定地点にダッシュして、到着時に周囲の敵ユニットをノックアップさせる。
- **E — バトルダンス：** 味方チャンピオンのところまで飛びシールドを付与する。このスキルは少しの間だけコスト無しで再使用できる。
- **R — みんなオレに夢中：** 移動速度が増加して、触れた敵ユニットにチャームと魔法ダメージを与える。

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

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 175試合、全体勝率 47.4%
- **時間帯別勝率：** 〜20分 46.7%（n=30）、20〜25分 44.0%（n=25）、25〜30分 50.0%（n=40）、30〜35分 43.9%（n=41）、35分〜 51.3%（n=39）
- **最高帯：** 35分〜（判定差 7.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rakan` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rakan.png)

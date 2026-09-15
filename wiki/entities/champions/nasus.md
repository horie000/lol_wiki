---
title: "ナサス"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Nasus"
champion_key: "75"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Nasus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nasus.png"
---

# ナサス

![[raw/assets/champions/Nasus.png|128]]

## 基本情報

- **英字ID：** `Nasus`
- **キー：** `75`
- **称号：** 砂漠の司書
- **データversion：** `16.18.1`

## 紹介

ジャッカルの頭を持つ超越者ナサスは、古代シュリーマで生を受けた。威風堂々たる体躯を誇る彼を、砂漠の民は半神半人と崇めていた。頭脳明晰で学問を尊び、比類なき戦略家でもあったナサスは、その豊富な知識で古代シュリーマ帝国を何百年も続く栄華の時代へと導いた。やがて帝国が没落すると、ナサスは自ら故郷を離れ、彼の名は伝説と化した。だが今、再び古代都市シュリーマが蘇り、ナサスは故郷へと戻ってきた。二度とこの街を崩壊させはしないと、心に誓って。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 5 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 104 |
| `mp` | 326 |
| `mpperlevel` | 62 |
| `movespeed` | 350 |
| `armor` | 34 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7.45 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 67 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.48 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — ソウルイーター：** 敵の魂のエネルギーを吸い取り、自身のライフスティールが増加する。

- **Q — サイフォンストライク：** 敵を攻撃してダメージを与える。さらに、対象にとどめを刺すと「サイフォンストライク」の威力が増していく。
- **W — ウィザー：** 指定した敵チャンピオンを老化させる。効果時間中、敵の移動速度と攻撃速度が徐々に減少する。
- **E — スピリットファイア：** 指定範囲に神秘的な炎を呼び寄せ、範囲内の敵にダメージを与えて物理防御を低下させる。
- **R — アヌビスの怒り：** 巨大化して、強力な砂嵐を身にまとう。砂嵐をまとっている間は、体力と通常攻撃の射程距離が増加する。またその間は、周囲の敵にダメージを与え、「サイフォンストライク」のクールダウンが短くなり、物理防御と魔法防御が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中8位（上位15%）。体力650、物理防御34、攻撃力67、移動速度350。
  - 「サイフォンストライク」で敵を倒すたびにダメージが恒久的に増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 447試合、全体勝率 51.0%
- **時間帯別勝率：** 〜20分 52.9%（n=68）、20〜25分 43.3%（n=67）、25〜30分 53.9%（n=115）、30〜35分 55.8%（n=104）、35分〜 46.2%（n=93）
- **最高帯：** 30〜35分（判定差 12.5ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nasus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nasus.png)

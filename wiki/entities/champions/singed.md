---
title: "シンジド"
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
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Singed"
champion_key: "27"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Singed.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Singed.png"
---

# シンジド

![[raw/assets/champions/Singed.png|128]]

## 基本情報

- **英字ID：** `Singed`
- **キー：** `27`
- **称号：** マッドケミスト
- **データversion：** `16.18.1`

## 紹介

シンジドは優れた錬金術師だが、倫理観が欠如した存在でもあり、その実験は極めて残忍な犯罪者ですら吐き気をもよおすほどだ。彼は最も高い報酬を提示した者にその技術を売り、自らの有害な調合物がいかに使用されようがろくに関心を払わず、それがもたらす混沌すらをも実験の一環として見ているふしがある。彼が生み出したものの中でも最も悪名高いのが「シマー」であり、これによってケミ長者たちはゾウンを彼らの遊び場へと変貌させることとなった。それでもシンジドは狂気に突き動かされ、常に新しいなにかに取り組んでいる。堕落の一途をた...

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 96 |
| `mp` | 330 |
| `mpperlevel` | 45 |
| `movespeed` | 345 |
| `armor` | 34 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.55 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.9 |
| `attackspeed` | 0.7 |

## アビリティ

- **パッシブ — スリップストリーム：** 周囲のチャンピオンを利用して空気抵抗を減らし、通り過ぎる際に一時的に移動速度が増加する。

- **Q — 毒の軌跡：** 背中から毒ガスをまき散らし、ガスに接触した敵にダメージを与える。
- **W — 強力粘着剤：** 強力な粘着剤の入ったビンを地面に投げ、接触した敵にスロウ効果を与えて釘付けにする。
- **E — すくい投げ：** 対象の敵ユニットにダメージを与え、シンジドの背後へ投げ飛ばす。 「強力粘着剤」の上に着地した場合は、スネア状態になる。
- **R — 狂人のポーション：** 強力な調合薬を飲んで戦闘能力が一時的に強化され、「毒の軌跡」が「重傷」を付与するようになる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中23位（上位15%）。体力650、物理防御34、攻撃力63、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 259試合、全体勝率 53.3%
- **時間帯別勝率：** 〜20分 54.3%（n=35）、20〜25分 58.5%（n=41）、25〜30分 51.7%（n=58）、30〜35分 50.0%（n=62）、35分〜 54.0%（n=63）
- **最高帯：** 20〜25分（判定差 8.5ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Singed` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Singed.png)

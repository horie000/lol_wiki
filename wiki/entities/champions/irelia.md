---
title: "イレリア"
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
  - role-assassin
  - data-dragon
champion_id: "Irelia"
champion_key: "39"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Irelia.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Irelia.png"
---

# イレリア

![[raw/assets/champions/Irelia.png|128]]

## 基本情報

- **英字ID：** `Irelia`
- **キー：** `39`
- **称号：** 飛刃の舞い手
- **データversion：** `16.18.1`

## 紹介

ノクサスのアイオニア占領は数多くの英雄を生み出すことになったが、ナヴォリ出身の若きイレリアほど傑出した才能は存在しない。地域に伝わる古代舞踊の訓練を通じて戦いの技術を身に付けた彼女は、優雅かつ繊細な動きで複数の刃を宙に浮かべることができる。戦士としての実力を評価され反乱軍の指導者となった彼女は、今でも故郷を守るためにすべてを捧げて戦い続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 115 |
| `mp` | 350 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 36 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 200 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.656 |

## アビリティ

- **パッシブ — アイオニアの熱情：** 敵にスキルを当てるとスタックを獲得する。スタック数に応じて増加攻撃速度を獲得し、最大スタックになると通常攻撃時に追加ダメージを付与する。

- **Q — 瞬刃：** 前方にダッシュして対象を攻撃し、自身の体力を回復する。これによって対象をキルするか、対象がマークされていた場合は、「瞬刃」のクールダウンが解消される。
- **W — 不屈の舞：** チャージ攻撃を行う。チャージ時間が長いほど、与えるダメージが増加する。チャージ中は被物理ダメージが減少する。
- **E — 無欠の連舞：** 2枚の刃を飛ばす。これらの刃は互いの方向に飛んで収束する。2枚の刃に挟まれた敵はダメージとスタン効果を受けてマークされる。
- **R — 先陣の刃：** 大量の刃を飛ばす。刃は敵チャンピオンに当たると放射状に広がり、当たった敵はダメージを受けてマークされる。その後、刃が壁を形成し、この壁を越えた敵はダメージとスロウ効果を受ける。

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
- **対象試合：** 435試合、全体勝率 51.5%
- **時間帯別勝率：** 〜20分 50.0%（n=68）、20〜25分 53.6%（n=69）、25〜30分 54.0%（n=113）、30〜35分 47.1%（n=87）、35分〜 52.0%（n=98）
- **最高帯：** 25〜30分（判定差 6.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Irelia` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Irelia.png)

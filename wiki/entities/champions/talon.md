---
title: "タロン"
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
  - role-assassin
  - data-dragon
champion_id: "Talon"
champion_key: "91"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Talon.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Talon.png"
---

# タロン

![[raw/assets/champions/Talon.png|128]]

## 基本情報

- **英字ID：** `Talon`
- **キー：** `91`
- **称号：** 将軍の懐刀
- **データversion：** `16.18.1`

## 紹介

タロンは闇を駆ける刃であり、誰にも悟られることなく攻撃し、気付かれる前に脱出することができる非情な殺し屋だ。暴力があふれる危険なノクサスの裏路地で育った彼は、生きるために戦い、殺し、盗みを余儀なくされて、優れたナイフの使い手として知られるようになった。現在は悪名高きデュ・クートウ家の養子となり、帝国の指揮のもとに殺しの仕事を請け負い、敵側の指導者、隊長、英雄…さらには支配者の軽蔑を勝った愚かなノクサス人たちまでも暗殺し続けている。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 658 |
| `hpperlevel` | 109 |
| `mp` | 400 |
| `mpperlevel` | 37 |
| `movespeed` | 335 |
| `armor` | 30 |
| `armorperlevel` | 4.7 |
| `spellblock` | 36 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.9 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 血塗られし慈悲：** タロンのスキルは敵チャンピオンまたは大型モンスターに3回までスタックする「傷」を付与する。「傷」のスタックが3つになった敵チャンピオンに通常攻撃を行うと、そのチャンピオンは出血して継続的に大ダメージを受ける。

- **Q — ノクサスの刃：** タロンが対象を突き刺す。近接攻撃の射程内であれば、この攻撃はクリティカルダメージを与える。近接攻撃の射程外であれば、対象までジャンプしてから突き刺す。このスキルで対象を倒すと体力の一部が回復し、クールダウンの一部が解消する。
- **W — 飛燕手裏剣：** ブーメランのように戻ってくる刃を同時に複数投げる。刃は往路と復路で敵を貫通するたびに物理ダメージを与える。復路で刃が敵ユニットに命中すると、追加ダメージと短時間のスロウ効果を与える。
- **E — 暗殺者の跳躍：** タロンはどんな地形や建造物も最大距離まで飛び越えられる。このスキルのクールダウンは短いが、飛び越えた地形や建造物に対しては長いクールダウンに入る。
- **R — シャドウアサルト：** 複数の刃を全方向に投げ、インビジブル状態になって移動速度が増加する。インビジブル状態が解除されると、投げた刃がタロンのいる地点に一斉に戻ってくる。飛んでいった時と戻ってきた時のそれぞれで、刃が命中した敵に物理ダメージを与える。

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
- **対象試合：** 158試合、全体勝率 51.9%
- **時間帯別勝率：** 〜20分 58.1%（n=31）、20〜25分 36.0%（n=25）、25〜30分 52.9%（n=34）、30〜35分 58.5%（n=41）、35分〜 48.1%（n=27）
- **最高帯：** 30〜35分（判定差 22.5ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Talon` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Talon.png)

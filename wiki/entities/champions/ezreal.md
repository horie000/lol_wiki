---
title: "エズリアル"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "Ezreal"
champion_key: "81"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Ezreal.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ezreal.png"
---

# エズリアル

![[raw/assets/champions/Ezreal.png|128]]

## 基本情報

- **英字ID：** `Ezreal`
- **キー：** `81`
- **称号：** 光の冒険心
- **データversion：** `16.18.1`

## 紹介

自由奔放な冒険家で、本人は知らないながらも魔法の才能を持つエズリアルは、長らく失われていた地下墓地を暴き、古代の呪いとの格闘を乗り越え、絶体絶命と思われる状況をいとも簡単にかいくぐる。その勇気と自信はとどまる所を知らず、どんな窮地にあっても機転を利かせて脱することをよしとしているが、大抵の場合、頼りになるのは機転以上に、驚異的な破壊力の魔弾を発射する謎めいたシュリーマのガントレットである。ひとつだけ確かなことは、エズリアルが現れるところ、どこであろうと遅かれ早かれ、必ず騒動が巻き起こるということだ。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 2 |
| `magic` | 6 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 102 |
| `mp` | 375 |
| `mpperlevel` | 70 |
| `movespeed` | 325 |
| `armor` | 24 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ライジングスペルフォース：** スキルを連続で命中させるたびに攻撃速度が増加していく。最大5スタック。

- **Q — ミスティックショット：** エネルギービームを発射してダメージを与える。敵ユニットに命中すると、自身の全スキルのクールダウンが少しだけ短縮される。
- **W — エッセンスフラックス：** 最初に命中したチャンピオンまたはオブジェクトに貼り付くオーブを発射する。オーブの付いた敵を攻撃すると、オーブが爆発してダメージを与える。
- **E — アーケインシフト：** 近くの指定地点に瞬間移動してエネルギービームを発射する。このエネルギービームは最も近くにいる敵ユニットに向かって発射される。「エッセンスフラックス」のスタックを受けた敵を優先する。
- **R — トゥルーショットバラージ：** 少しチャージしてから敵を貫通する強力なエネルギービームを発射して、命中した敵ユニットに大ダメージを与える(ミニオンとエピック以外のモンスターに対してはダメージが低下)。

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
- **対象試合：** 519試合、全体勝率 48.4%
- **時間帯別勝率：** 〜20分 48.9%（n=92）、20〜25分 45.6%（n=79）、25〜30分 47.7%（n=109）、30〜35分 45.3%（n=106）、35分〜 52.6%（n=133）
- **最高帯：** 35分〜（判定差 7.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ezreal` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ezreal.png)

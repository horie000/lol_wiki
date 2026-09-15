---
title: "クレッド"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
champion_id: "Kled"
champion_key: "240"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "勇気の護り"
image_path: "raw/assets/champions/Kled.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kled.png"
---

# クレッド

![[raw/assets/champions/Kled.png|128]]

## 基本情報

- **英字ID：** `Kled`
- **キー：** `240`
- **称号：** 狂乱の騎兵
- **データversion：** `16.18.1`

## 紹介

恐れ知らずで粗暴な武人であるヨードルのクレッドは、ノクサスの持つ激情的な無鉄砲さを体現しており、上官には信用されず、貴族には毛嫌いされているが、帝国の兵士たちには愛されている象徴的存在だ。多くの兵士たちが、クレッドは帝国の軍隊が戦ったあらゆる戦争に参加し、あらゆる階級称号を獲得し、そして、戦いにおいて一度たりとも退却したことがないと主張する。細かい部分の信憑性はかなり疑わしいが、クレッドの伝説には一つだけ否定できない事実がある。彼が信頼のおけない愛馬「スカール」に跨って戦場に向かう時、彼は自分のものは...

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** 勇気の護り

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 2 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 410 |
| `hpperlevel` | 84 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 弱虫トカゲ「スカール」：** クレッドが彼の信頼する愛馬、スカールに騎乗している時は、クレッドの代わりにスカールがダメージを受けてくれる。スカールの体力がなくなるとクレッドはスカールから降ろされる。 非騎乗時はクレッドのスキルが変化して敵チャンピオンに与えるダメージが減少する。クレッドは敵と交戦することでスカールの「勇気」を回復できる。「勇気」が最大になると、クレッドは再び騎乗してスカールの体力を獲得する。

- **Q — トラバサミロープ：** ダメージを与えるトラバサミを投げて、敵チャンピオンに引っ掛ける。引っ掛かった状態を少しの間維持すると、対象に追加物理ダメージを与えて自身の方向に引き寄せる。 非騎乗時では、このスキルは「ポケットピストル」に変化する。これは銃を発砲する遠隔攻撃で、反動で自らを後方に飛ばし、「勇気」を回復する。
- **W — 狂暴の宴：** 次の4回の通常攻撃を繰り出す速度が大きく増加する。4回目の通常攻撃はダメージが増加する。
- **E — ジャウスト：** ダッシュして物理ダメージを与え、一時的に移動速度が増加する。スキルを再使用すると、最初に攻撃した対象にダッシュで戻り、初回と同量のダメージを与える。
- **R — チャァァァァァァァジ！！！：** クレッドとスカールが指定した位置に突撃してシールドを獲得し、通り道に移動速度を増加させる効果を残していく。スカールは最初に遭遇した敵チャンピオンにロックオンして体当たりする。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kled` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kled.png)

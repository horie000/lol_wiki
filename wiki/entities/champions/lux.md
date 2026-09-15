---
title: "ラックス"
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
champion_id: "Lux"
champion_key: "99"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Lux.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lux.png"
---

# ラックス

![[raw/assets/champions/Lux.png|128]]

## 基本情報

- **英字ID：** `Lux`
- **キー：** `99`
- **称号：** 光の才女
- **データversion：** `16.18.1`

## 紹介

ラクサーナ・クラウンガードは魔法の才能を恐怖と疑惑の目で見る偏狭な国、デマーシアで生まれた。意思の力で光を自在に操ることができる彼女だったが、力を持つことを見つけられて追放されることを恐れながら育ち、名門一家の権威を守るためにそれを秘密にすることを強いられてきた。しかし、持ち前の楽観主義と負けん気で自らのユニークな能力を受け入れることを決めて、今では祖国のためにその力を密かに行使するようになったのである。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 9 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 99 |
| `mp` | 440 |
| `mpperlevel` | 23.5 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 9 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.669 |

## アビリティ

- **パッシブ — イルミネーション：** 攻撃スキルが命中した対象を数秒間「イルミネーション」でマークする。マークした対象にラックスの攻撃が命中すると、エネルギーが爆発して追加魔法ダメージを与える(追加ダメージの量はラックスのレベルに比例する)。

- **Q — ライトバインド：** 光の玉を発射し、最大2体までの敵にダメージを与えてスネア効果を付与する。
- **W — プリズムバリア：** 指定方向に杖を投げ、自身と杖に触れた味方チャンピオンに光を屈折させたシールドを付与する。杖は最大距離に達するとラックスのもとへ戻り、触れた味方チャンピオンと杖をキャッチしたラックスに再びシールドを付与する。
- **E — シンギュラリティ：** 指定地点に特異な光の玉を放ち、範囲内の敵にスロウ効果を付与する。効果時間内に再度発動すると光の玉が爆発し、範囲内の敵にダメージを与える。
- **R — ファイナルスパーク：** 光のエネルギーを集めてビームを発射し、範囲内の敵にダメージを与える。「イルミネーション」効果を受けている敵に命中すると爆発させて追加魔法ダメージを与え、再度「イルミネーション」を付与する。

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
- **対象試合：** 751試合、全体勝率 50.3%
- **時間帯別勝率：** 〜20分 56.7%（n=127）、20〜25分 46.7%（n=107）、25〜30分 53.6%（n=166）、30〜35分 50.9%（n=165）、35分〜 44.6%（n=186）
- **最高帯：** 〜20分（判定差 12.1ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 12.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Lux` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Lux.png)

---
title: "シン・ジャオ"
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
champion_id: "XinZhao"
champion_key: "5"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/XinZhao.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/XinZhao.png"
---

# シン・ジャオ

![[raw/assets/champions/XinZhao.png|128]]

## 基本情報

- **英字ID：** `XinZhao`
- **キー：** `5`
- **称号：** デマーシアの家令長
- **データversion：** `16.18.1`

## 紹介

シン・ジャオは、現王朝のライトシールド王家に忠誠を誓う毅然とした戦士だ。かつてノクサスの闘技場で戦うことを強いられ無数の戦闘を生き延びてきた彼だったが、デマーシアの軍隊によって解放されたことで、彼はこの勇敢な解放者たちに対して生涯の忠誠を誓った。愛用の三又の槍を手に、彼はどんな不利な状況であってもあらゆる敵に大胆に挑み、新たな故郷となった王国のために戦っている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 106 |
| `mp` | 274 |
| `mpperlevel` | 55 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 4.4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.645 |

## アビリティ

- **パッシブ — 不退転：** 通常攻撃が3回毎に追加ダメージを与えて自身を回復する。

- **Q — 三槍撃：** 通常攻撃が3回分強化され、3回目で敵をノックアップさせる。
- **W — 風成雷鳴：** 前方を槍で薙ぎ払い、次に槍を突いて敵ユニットにスロウを与え、挑戦対象としてマークする。
- **E — 兵貴神速：** 敵に突進して攻撃速度が増加し、範囲内にいるすべての敵にダメージと短時間のスロウ効果を与える。挑戦対象に対しては、このスキルの射程が増加する。
- **R — 三日月槍守：** 自動効果で、直前にダメージを与えた敵が挑戦対象になる。発動すると、周囲にいる敵に対象の現在体力に応じたダメージを与え、挑戦対象以外をノックバックさせる。発生した円の外にいる敵チャンピオンからはダメージを受けなくなる。

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
- **対象試合：** 263試合、全体勝率 47.5%
- **時間帯別勝率：** 〜20分 42.6%（n=47）、20〜25分 45.0%（n=40）、25〜30分 48.1%（n=54）、30〜35分 46.6%（n=58）、35分〜 53.1%（n=64）
- **最高帯：** 35分〜（判定差 10.6ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 10.6%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.XinZhao` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/XinZhao.png)

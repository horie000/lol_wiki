---
title: "セト"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Sett"
champion_key: "875"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "闘魂"
image_path: "raw/assets/champions/Sett.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sett.png"
---

# セト

![[raw/assets/champions/Sett.png|128]]

## 基本情報

- **英字ID：** `Sett`
- **キー：** `875`
- **称号：** ザ・ボス
- **データversion：** `16.18.1`

## 紹介

ノクサスとの戦争の機運が高まる中、セトはアイオニアで勢力を増しつつある裏社会の親玉として名を上げた。ナヴォリの闘技場で戦い始めたときには無名の挑戦者に過ぎなかったセトだが、恐ろしいほどの腕力と底知れぬ打たれ強さで瞬く間にその名を轟かせた。実力で参加者たちの頂点にまで上り詰めたセトは、ついにはかつて自分が戦った闘技場の支配権を握ったのだった。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** 闘魂

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 1 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 670 |
| `hpperlevel` | 114 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 33 |
| `armorperlevel` | 4.7 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.75 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ファイティングスピリット：** 通常攻撃で左右のパンチを交互に繰り出す。右のパンチの方が少し強く、速い。また、セトは負けず嫌いで、減少体力に応じて体力自動回復が増加する。

- **Q — ナックルダウン：** 次の2回の通常攻撃が対象の最大体力に応じた追加ダメージを与える。また、敵チャンピオンに向かう際は移動速度が増加する。
- **W — ヘイメイカー：** 自動効果により、受けたダメージを「闘魂」として蓄える。発動するとすべての「闘魂」を消費してシールドを獲得し、パンチして一定範囲内の中心にいる敵には確定ダメージ、端にいる敵には物理ダメージを与える。
- **E — フェイスブレイカー：** 自身の両側にいるすべての敵を引き寄せ、ダメージを与えてスタンさせる。敵が片側のみにいた場合はスタンの代わりにスロウ効果を与える。
- **R — ショーストッパー：** 敵チャンピオンを担いでジャンプして移動後に地面に叩きつけ、着地時に周囲のすべての敵にダメージとスロウ効果を与える。

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
- **対象試合：** 469試合、全体勝率 51.8%
- **時間帯別勝率：** 〜20分 63.0%（n=73）、20〜25分 53.1%（n=64）、25〜30分 40.4%（n=109）、30〜35分 53.5%（n=114）、35分〜 53.2%（n=109）
- **最高帯：** 〜20分（判定差 9.8ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 9.8%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-875|セトの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（794試合）

- **実測ビルド候補：** 覇王のブラッドメイル + ワーモグ アーマー（該当n=54、70.4% / 非該当48.4%、差+22.0pt）；覇王のブラッドメイル + ワーモグ アーマー + ストライドブレイカー（該当n=52、69.2% / 非該当48.5%、差+20.7pt）
- **ステータス傾向：** ライフスティール（該当n=178、52.2% / 非該当49.2%、差+3.1pt）
- **理論仮説：** トリニティ フォース + ストライドブレイカー（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；実験的ヘクスプレート + ストライドブレイカー（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sett` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sett.png)

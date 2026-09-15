---
title: "ケイン"
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
  - role-assassin
  - data-dragon
champion_id: "Kayn"
champion_key: "141"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Kayn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayn.png"
---

# ケイン

![[raw/assets/champions/Kayn.png|128]]

## 基本情報

- **英字ID：** `Kayn`
- **キー：** `141`
- **称号：** 無情の影
- **データversion：** `16.18.1`

## 紹介

恐るべき影の魔術の卓越した使い手であるシエダ・ケイン。彼は己の真の運命──いつの日か自分が「影の一団」を率い、アイオニアが覇権を握る新時代を拓く、という未来のために戦っている。彼が手にする、自我を持つダーキンの武器「ラースト」はケインの心身を着実に侵しつつあるが、気に留める様子はない。あり得る結末はただ二つ。ケインが強い意志で武器をねじ伏せるか、または邪悪な武器に完全に乗っ取られ、ルーンテラを滅亡の道へと誘う扉を開くかだ。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 6 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 103 |
| `mp` | 410 |
| `mpperlevel` | 50 |
| `movespeed` | 340 |
| `armor` | 38 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.95 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.669 |

## アビリティ

- **パッシブ — 緋眼の大鎌：** ケインは自我を持つダーキンの古代武器ラーストを用いており、両者は常に互いの支配権をかけて争っている。この戦いはダーキンがケインを取り込むか、ケインがラーストを使いこなし影の暗殺者となるまで続く。 ダーキン: 敵チャンピオンにスキルで与えたダメージの一定割合にあたる体力を回復する。 影の暗殺者: 敵チャンピオンと戦闘開始直後の数秒間、追加ダメージを与える。

- **Q — 飛影斬：** ダッシュしてから斬りつける。その両方でダメージを与える。
- **W — 刃影襲：** 直線上にいる敵にダメージとスロウ効果を与える。
- **E — 影抜き：** ケインが地形を無視して歩くことができる。
- **R — 真影侵壊：** 敵の体の中に侵入して、出てくる時に大ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中13位（上位15%）。体力655、物理防御38、攻撃力68、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 300試合、全体勝率 52.7%
- **時間帯別勝率：** 〜20分 54.5%（n=44）、20〜25分 46.5%（n=43）、25〜30分 54.9%（n=71）、30〜35分 58.7%（n=75）、35分〜 46.3%（n=67）
- **最高帯：** 30〜35分（判定差 12.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-141|ケインの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（573試合）

- **実測ビルド候補：** アクシオム アーク + ボルテイク サイクロソード（該当n=61、68.9% / 非該当47.3%、差+21.6pt）；アクシオム アーク + ヒュブリス + ボルテイク サイクロソード（該当n=31、67.7% / 非該当48.5%、差+19.2pt）
- **ステータス傾向：** 体力（該当n=397、50.9% / 非該当46.6%、差+4.3pt）
- **理論仮説：** ガーディアン エンジェル + デス ダンス（n=10（15未満）；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 物理防御・攻撃力）；ショウジンの矛 + ナイト エッジ（n=4（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### TOP（39試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** ブラック クリーバー + ショウジンの矛（n=8（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；ショウジンの矛 + ストライドブレイカー（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kayn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayn.png)

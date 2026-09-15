---
title: "セナ"
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
  - role-support
  - role-marksman
  - data-dragon
champion_id: "Senna"
champion_key: "235"
data_version: "16.18.1"
roles:
  - "Support"
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Senna.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Senna.png"
---

# セナ

![[raw/assets/champions/Senna.png|128]]

## 基本情報

- **英字ID：** `Senna`
- **キー：** `235`
- **称号：** 救済者
- **データversion：** `16.18.1`

## 紹介

幼い頃に呪いを受け、超自然現象である「黒き霧」に追われてきたセナは、「光の番人」として知られる聖なる騎士団に加わり、霧と激しく戦った──しかし、彼女は冷酷な亡霊スレッシュによって殺され、ランタンの中に囚われてしまった。それでも希望を捨てなかったセナは、ランタンの中で霧の力を掌握し、新たな命を得て復活を遂げた。光のみならず闇をも操るようになった彼女は、古の武器で放つ一撃ごとに霧の中で失われた魂を救済しながら、「黒き霧」を滅ぼそうとしている。

## 分類

- **役割タグ：** `Support`、`Marksman`
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
| `hp` | 530 |
| `hpperlevel` | 89 |
| `mp` | 350 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 600 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.6 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 魂の赦し：** セナの周囲でユニットが倒されると、一定時間ごとにその魂が「黒き霧」に囚われる。セナはこの魂を通常攻撃して解放することで、魂を死の世界に閉じ込めていた「霧」を吸収することができる。「霧」によって「レリックキャノン」が強化されて、攻撃力、射程距離、クリティカル率が増加する。 通常攻撃で「レリックキャノン」を発射するまでにかかる時間は長くなるが、追加ダメージを与えるようになり、さらに一時的に対象の移動速度の一部を獲得する。

- **Q — ピアシングダークネス：** 「レリックキャノン」のツインバレルから光と影が一体となったビームを発射して対象を撃ち抜き、味方は回復して敵にはダメージを与える。
- **W — 最期の抱擁：** 前方に「黒き霧」を放つ。霧は当たった敵に絡みつき、少ししてから対象と周囲のすべての敵ユニットにスネア効果を付与する。
- **E — 黒き霧の呪い：** 武器に取り込んだ「霧」を利用して周囲に嵐を引き起こし、闇を受け入れて亡霊に変化する。範囲内に入った味方はカモフラージュ状態になり、「霧」の作用によって亡霊の姿となる。亡霊の姿になると移動速度が増加し、対象指定不可になり、正体が隠される。
- **R — ドーニングシャドウ：** 亡くなった光の番人のレリックストーンに呼びかけ、「レリックキャノン」が聖なる影と光に分かれる。その後、超大射程のビームを発射して命中した味方にはシールドを展開し、ビームの中心にいた敵にはダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「霧」の吸収で攻撃力・射程距離・クリティカル率が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 366試合、全体勝率 48.9%
- **時間帯別勝率：** 〜20分 45.0%（n=60）、20〜25分 54.0%（n=50）、25〜30分 46.5%（n=86）、30〜35分 51.0%（n=96）、35分〜 48.6%（n=74）
- **最高帯：** 20〜25分（判定差 9.0ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-235|セナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（438試合）

- **実測ビルド候補：** インフィニティ エッジ + ブラック クリーバー（該当n=31、64.5% / 非該当47.7%、差+16.9pt）；ブラック クリーバー + ラピッド ファイアキャノン（該当n=115、54.8% / 非該当46.7%、差+8.0pt）
- **ステータス傾向：** クリティカル率（該当n=242、52.5% / 非該当44.4%、差+8.1pt）；攻撃力（該当n=380、49.5% / 非該当44.8%、差+4.6pt）
- **理論仮説：** ルナーン ハリケーン + ラピッド ファイアキャノン（n=3（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）；ファントム ダンサー + ラピッド ファイアキャノン（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

### BOTTOM（345試合）

- **実測ビルド候補：** インフィニティ エッジ + ラピッド ファイアキャノン（該当n=36、66.7% / 非該当50.8%、差+15.9pt）；インフィニティ エッジ + スタティック シヴ（該当n=76、61.8% / 非該当49.8%、差+12.0pt）
- **ステータス傾向：** クリティカル率（該当n=238、55.9% / 非該当44.9%、差+11.0pt）；物理防御（該当n=145、53.8% / 非該当51.5%、差+2.3pt）
- **理論仮説：** スタティック シヴ + クラーケン スレイヤー（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；ファントム ダンサー + ラピッド ファイアキャノン（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Senna` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Senna.png)

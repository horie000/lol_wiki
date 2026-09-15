---
title: "エイトロックス"
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
  - data-dragon
champion_id: "Aatrox"
champion_key: "266"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "ブラッドウェル"
image_path: "raw/assets/champions/Aatrox.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aatrox.png"
---

# エイトロックス

![[raw/assets/champions/Aatrox.png|128]]

## 基本情報

- **英字ID：** `Aatrox`
- **キー：** `266`
- **称号：** ダーキンの暴剣
- **データversion：** `16.18.1`

## 紹介

ヴォイドからシュリーマを守り抜いた誇り高き存在であったエイトロックスとその同胞は、いつしかルーンテラにとってヴォイドを上回る脅威となり、狡猾な定命の者の魔法の前に敗れ去った。数世紀にも及ぶ幽閉を経て、エイトロックスは彼の精髄を封じていた魔の武器を手にした愚か者の肉体を奪い、再び自由の身となることに成功した。奪った肉体をかつての姿へと変え、ルーンテラを闊歩する彼は、長らく望んできた復讐──世界を終焉させる機会をうかがっている。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** ブラッドウェル

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 114 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 38 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 3 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.651 |

## アビリティ

- **パッシブ — 死兆の構え：** 一定時間ごとに、次の通常攻撃が対象の最大体力に応じた追加魔法ダメージを与え、同量の体力を回復する。

- **Q — ダーキンブレード：** 大剣を叩きつけて物理ダメージを与える。剣を3回振ることが可能で、振るごとに効果範囲が変化する。
- **W — 炎獄の鎖：** 地面を叩きつけて、最初に命中した敵にダメージを与える。チャンピオンと大型モンスターは数秒以内に攻撃範囲から出なければ、中央に引き寄せられて再度ダメージを受ける。
- **E — 影進撃：** 自動効果として、敵チャンピオンにダメージを与えると体力が回復する。発動すると、指定方向に向かってダッシュする。
- **R — ワールドエンダー：** 悪魔形態を解放して周囲の敵ミニオンにフィアー効果を与え、攻撃力、回復量、移動速度が増加する。キルまたはアシストを獲得した場合、この効果が延長される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中19位（上位15%）。体力650、物理防御38、攻撃力60、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 347試合、全体勝率 50.7%
- **時間帯別勝率：** 〜20分 53.7%（n=54）、20〜25分 55.8%（n=52）、25〜30分 53.3%（n=75）、30〜35分 43.0%（n=86）、35分〜 51.2%（n=80）
- **最高帯：** 20〜25分（判定差 12.7ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-266|エイトロックスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（902試合）

- **実測ビルド候補：** ショウジンの矛 + セリルダの怨恨（該当n=71、76.1% / 非該当51.0%、差+25.0pt）；ショウジンの矛 + セリルダの怨恨 + ボルテイク サイクロソード（該当n=58、74.1% / 非該当51.5%、差+22.6pt）
- **ステータス傾向：** 魔法防御（該当n=348、54.3% / 非該当52.2%、差+2.1pt）
- **理論仮説：** ケミパンク チェーンソード + サンダード スカイ（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；サンダード スカイ + ストライドブレイカー（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### JUNGLE（59試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** ショウジンの矛 + サンダード スカイ（n=13（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；ブラック クリーバー + サンダード スカイ（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Aatrox` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aatrox.png)

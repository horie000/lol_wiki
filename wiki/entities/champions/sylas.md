---
title: "サイラス"
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
  - role-mage
  - role-assassin
  - data-dragon
champion_id: "Sylas"
champion_key: "517"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Sylas.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sylas.png"
---

# サイラス

![[raw/assets/champions/Sylas.png|128]]

## 基本情報

- **英字ID：** `Sylas`
- **キー：** `517`
- **称号：** 解き放たれし者
- **データversion：** `16.18.1`

## 紹介

デマーシアの貧しい地域に育ったドレグボーンのサイラスは、この大都の闇を象徴する存在となった。少年期の彼には隠れた魔力を発見する才能があり、それゆえに悪名高きメイジ狩りに重用されていた。だがある時、その力をメイジ狩りたちに向けて用いたために投獄されてしまった。やがて脱獄に成功した彼は、今では強硬派の革命家となり、周囲の魔力を盗み取って自分がかつて仕えた王国を破壊しようとしている──そして彼に従う追放されたメイジたちの数は、日を追うごとに増えているのだ。

## 分類

- **役割タグ：** `Mage`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 122 |
| `mp` | 400 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 29 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.55 |
| `attackrange` | 175 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.645 |

## アビリティ

- **パッシブ — ペトリサイトバースト：** スキル使用後、「ペトリサイトバースト」がチャージされる。通常攻撃でチャージを解放し、魔力のこもった鎖を旋回させて当たった敵に追加魔法ダメージを与える。「ペトリサイトバースト」のチャージを保持している間は攻撃速度が増加する。

- **Q — 鎖の鞭：** 指定地点で交わるように2本の鎖を叩きつけ、敵にダメージとスロウ効果を与える。 少ししてから交差地点で魔法エネルギーが爆発し、ダメージを与える。
- **W — 王殺し：** 魔法エネルギーを纏って敵に突進し、ダメージを与える。対象がチャンピオンの場合は自身の体力を回復する。
- **E — 逃亡/拉致：** 指定地点にダッシュする。再発動で鎖を投げつけて命中した敵に向かって自身を引き寄せる。
- **R — 乗っ取り：** 敵のアルティメットスキルを奪い、自由に発動できる。

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
- **対象試合：** 525試合、全体勝率 45.9%
- **時間帯別勝率：** 〜20分 47.0%（n=83）、20〜25分 48.7%（n=78）、25〜30分 48.9%（n=135）、30〜35分 44.3%（n=122）、35分〜 41.1%（n=107）
- **最高帯：** 25〜30分（判定差 7.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-517|サイラスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（829試合）

- **実測ビルド候補：** メジャイ ソウルスティーラー + シャドウフレイム（該当n=47、87.2% / 非該当47.3%、差+39.9pt）；メジャイ ソウルスティーラー + 連呪使いのブーツ + シャドウフレイム（該当n=42、85.7% / 非該当47.6%、差+38.1pt）
- **ステータス傾向：** 体力（該当n=779、50.1% / 非該当42.0%、差+8.1pt）；物理防御（該当n=489、52.4% / 非該当45.6%、差+6.8pt）
- **理論仮説：** コズミック ドライブ + リフトメーカー（n=10（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；コズミック ドライブ + ロッド オブ エイジス（n=9（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

### JUNGLE（442試合）

- **実測ビルド候補：** メジャイ ソウルスティーラー + ゾーニャの砂時計（該当n=30、83.3% / 非該当45.9%、差+37.5pt）；メジャイ ソウルスティーラー + ヘクステック ロケットベルト（該当n=38、81.6% / 非該当45.3%、差+36.3pt）
- **ステータス傾向：** 体力（該当n=396、48.7% / 非該当45.7%、差+3.1pt）；物理防御（該当n=293、48.8% / 非該当47.7%、差+1.2pt）
- **理論仮説：** ヘクステック ロケットベルト + コズミック ドライブ（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；モレロノミコン + リフトメーカー（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sylas` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sylas.png)

---
title: "アリスター"
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
  - role-tank
  - role-support
  - data-dragon
champion_id: "Alistar"
champion_key: "12"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Alistar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Alistar.png"
---

# アリスター

![[raw/assets/champions/Alistar.png|128]]

## 基本情報

- **英字ID：** `Alistar`
- **キー：** `12`
- **称号：** ミノタウロスの戦士
- **データversion：** `16.18.1`

## 紹介

屈強な戦士として恐れられるアリスターは自分の部族を滅ぼしたノクサス帝国に復讐を誓っている。彼は奴隷となり、闘士として戦わされていたものの、不屈の意思の強さで理性を維持し、ただの獣に成り下がってしまうことは免れた。かつての主人たちの鎖から解放された今、彼は虐げられた者や不遇の者たちのために、己の角と蹄と怒りを武器にして戦っている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 9 |
| `magic` | 5 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 685 |
| `hpperlevel` | 120 |
| `mp` | 350 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 40 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.125 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 戦士の咆哮：** 敵チャンピオンをスタンさせるか弾き飛ばした時、または周囲で敵ユニットが倒されると「咆哮」をチャージする。最大までチャージされると自身および近くにいるすべての味方チャンピオンの体力を回復する。

- **Q — 圧砕：** 地面をたたきつけ、周囲にいる敵ユニットにダメージを与えてノックアップする。
- **W — 頭突き：** 対象に「頭突き」を食らわせてダメージを与え、ノックバックさせる。
- **E — 踏破：** 周囲の敵を踏みつけてユニットをすり抜けるようになる。これでチャンピオンにダメージを与えた場合、スタックを1つ獲得。スタックが最大になるとチャンピオンに対する次の通常攻撃に追加魔法ダメージとスタン効果を付与する。
- **R — 不屈の意志：** 荒々しい雄叫びをあげ、自身に付与された行動妨害効果をすべて解除する。効果時間中は自身が受ける物理ダメージと魔法ダメージを軽減する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中17位（上位15%）。体力685、物理防御40、攻撃力62、移動速度335。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 147試合、全体勝率 44.9%
- **時間帯別勝率：** 〜20分 38.7%（n=31）、20〜25分 57.9%（n=19）、25〜30分 46.2%（n=26）、30〜35分 47.4%（n=38）、35分〜 39.4%（n=33）
- **最高帯：** 20〜25分（判定差 18.5ポイント）
- **判定根拠：** 中間帯が最高、端点との差 18.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-12|アリスターの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（378試合）

- **実測ビルド候補：** ソーンメイル + ソラリのロケット（該当n=33、51.5% / 非該当47.5%、差+4.0pt）；ジーク コンバージェンス + ソラリのロケット（該当n=81、49.4% / 非該当47.5%、差+1.9pt）
- **ステータス傾向：** 魔力（該当n=48、52.1% / 非該当47.3%、差+4.8pt）；魔法防御（該当n=341、48.1% / 非該当45.9%、差+2.1pt）
- **理論仮説：** 先人の道標 + デッド マン プレート（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 物理防御・体力・移動速度）；バンドルパイプ + ジーク コンバージェンス + ソラリのロケット（n=6（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Alistar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Alistar.png)

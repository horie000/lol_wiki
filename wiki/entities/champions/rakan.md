---
title: "ラカン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
tags:
  - champion
  - role-support
  - data-dragon
champion_id: "Rakan"
champion_key: "497"
data_version: "16.18.1"
roles:
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Rakan.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rakan.png"
---

# ラカン

![[raw/assets/champions/Rakan.png|128]]

## 基本情報

- **英字ID：** `Rakan`
- **キー：** `497`
- **称号：** 魅惑の翼
- **データversion：** `16.18.1`

## 紹介

気まぐれで魅力的なラカンは、ヴァスタヤの悪名高きトラブルメーカーであり、ロトラン部族史上最高のバトルダンサーだ。アイオニア高地に住む人間たちにとって、彼の名はずっと、無礼講のお祭り、どんちゃん騒ぎ、アナーキーな音楽などと同意義だった。この活力に溢れた旅芸人が反逆者ザヤのパートナーであり、彼女の大義に命を捧げているなどと考える者はまずいない。

## 分類

- **役割タグ：** `Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 99 |
| `mp` | 315 |
| `mpperlevel` | 50 |
| `movespeed` | 335 |
| `armor` | 30 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 300 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8.75 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.635 |

## アビリティ

- **パッシブ — 神秘の翼：** ラカンは定期的にシールドを獲得する。

- **Q — キラリ羽根：** 魔法の羽根を投げて魔法ダメージを与える。敵チャンピオンかエピックモンスターに当たると、ラカンが味方を回復できる。
- **W — 華麗なる登場：** 指定地点にダッシュして、到着時に周囲の敵ユニットをノックアップさせる。
- **E — バトルダンス：** 味方チャンピオンのところまで飛びシールドを付与する。このスキルは少しの間だけコスト無しで再使用できる。
- **R — みんなオレに夢中：** 移動速度が増加して、触れた敵ユニットにチャームと魔法ダメージを与える。

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
- **対象試合：** 175試合、全体勝率 47.4%
- **時間帯別勝率：** 〜20分 46.7%（n=30）、20〜25分 44.0%（n=25）、25〜30分 50.0%（n=40）、30〜35分 43.9%（n=41）、35分〜 51.3%（n=39）
- **最高帯：** 35分〜（判定差 7.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-497|ラカンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（358試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3109|騎士の誓い]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=33、57.6% / 非該当48.9%、差+8.7pt）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3109|騎士の誓い]]（該当n=31、54.8% / 非該当49.2%、差+5.6pt）
- **ステータス傾向：** 魔法防御（該当n=314、50.0% / 非該当47.7%、差+2.3pt）；魔力（該当n=152、50.7% / 非該当49.0%、差+1.6pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-4401|自然の力]]（未観測；共通stats: 体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=10（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-497|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=545）

- **高勝率コンボ候補：** [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率61.1%（22/36）、n=36（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率42.5%（17/40）、n=40（十分性の目安を満たす）。

### JUNGLE（対象n=1）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Rakan` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Rakan.png)

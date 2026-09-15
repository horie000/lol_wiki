---
title: "カリスタ"
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
  - role-marksman
  - data-dragon
champion_id: "Kalista"
champion_key: "429"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Kalista.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kalista.png"
---

# カリスタ

![[raw/assets/champions/Kalista.png|128]]

## 基本情報

- **英字ID：** `Kalista`
- **キー：** `429`
- **称号：** 復讐の槍
- **データversion：** `16.18.1`

## 紹介

報復を誓い、復讐を司る亡霊カリスタは、偽り人や裏切りし者を狩るためシャドウアイルから召喚される。裏切られた者が血にまみれて復讐を乞い叫んでも、カリスタはそのために自らの魂を代償として支払う覚悟がある者の呼びかけにしか応えない。そしてひとたび彼女の憤怒を向けられた者は決して破滅から逃れることはできない。非情なる狩手が交わした契約は常に、彼女の魂が放つ冷たい槍で完了の印を捺されるのだ。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 4 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 114 |
| `mp` | 300 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 5.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 6.3 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4.5 |
| `attackspeed` | 0.694 |

## アビリティ

- **パッシブ — 戦の所作：** 通常攻撃または「貫魂の一投」の準備アクション中に移動指示を出すと、攻撃時にその方向へ跳躍して移動する。

- **Q — 貫魂の一投：** 高速で飛ぶ槍を投げる。命中した敵の体力がゼロになると、槍がその敵を貫通する。
- **W — 執念の霊魂：** カリスタと「魂盟の同志」が同じ対象を攻撃すると追加ダメージを与える。 スキルを発動すると霊魂を飛ばして周辺を偵察させ、霊魂の前方エリアを可視状態にする。
- **E — 引き裂く遺恨：** 通常攻撃するたびに、対象に槍の幻影が残る。発動すると槍の幻影が炸裂し、対象に刺さった槍の本数に比例するダメージを与え、スロウ効果を付与する。
- **R — 宿命の呼び声：** 「魂盟の同志」を強制的に自身の近くに吸い寄せる。カリスタの元に吸い寄せられた「魂盟の同志」は自分で指定した地点に突撃でき、範囲内にいる敵ユニットをわずかにノックバックさせる。

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

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 43試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 62.5%（n=8）、20〜25分 42.9%（n=7）、25〜30分 44.4%（n=9）、30〜35分 50.0%（n=12）、35分〜 28.6%（n=7）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-429|カリスタの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（85試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=37、45.9% / 非該当39.6%、差+6.4pt）；[[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3302|テルミヌス]]（該当n=30、43.3% / 非該当41.8%、差+1.5pt）
- **ステータス傾向：** 魔法防御（該当n=31、51.6% / 非該当37.0%、差+14.6pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3302|テルミヌス]]（n=11（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-429|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=107）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** [[wiki/entities/champions/kaisa|カイ＝サ（Kaisa）]] — 対象側勝率40.0%（6/15）、サンプル不足（n=15、十分性の目安30未満）。

### TOP（対象n=10）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kalista` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kalista.png)

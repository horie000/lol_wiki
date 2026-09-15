---
title: "ドクター・ムンド"
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
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "DrMundo"
champion_key: "36"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "なし"
image_path: "raw/assets/champions/DrMundo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/DrMundo.png"
---

# ドクター・ムンド

![[raw/assets/champions/DrMundo.png|128]]

## 基本情報

- **英字ID：** `DrMundo`
- **キー：** `36`
- **称号：** ゾウンの狂人
- **データversion：** `16.18.1`

## 紹介

完全に正気を失った、おぞましい紫色の悲しき殺人鬼。ゾウン市民の多くが闇の深い夜に外を出歩かないのは、ドクター・ムンドがいるためだ。今では“医者”を名乗っているが、以前はゾウンでも特に評判の悪い、とある医療院の患者だった。そこの職員を一人残らず“治療”したのち、ドクター・ムンドはかつて自身が処置を受けていた無人の病棟に診察室を構え、その身で何度も味わってきた非人道的な医療行為を、見よう見まねで行うようになった。棚に入った大量の薬物と、素人以下の医療知識を手に、ドクター・ムンドは今、注射を打つことで自身を...

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 103 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.5 |
| `spellblock` | 29 |
| `spellblockperlevel` | 2.3 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 気ままな往診：** 最初に受ける移動不能効果を無効化する。その際、代わりに体力を失い、近くに薬品の入った容器を落とす。落とした容器の上を歩いて回収すると体力が回復し、このスキルのクールダウンが短縮される。 また、ドクター・ムンドは極めて高い体力自動回復能力を持っている。

- **Q — 骨切りノコギリ：** 骨切りノコギリを投げ、最初に命中した敵に対象の現在体力に応じたダメージを与えて、スロウ効果を付与する。
- **W — 心臓ビリビリ：** 自身を感電させて、周囲の敵に継続的にダメージを与え、受けたダメージの一部を蓄える。効果時間の最後か再発動時に、周囲の敵に大ダメージを与える。これが敵に命中した場合は、それまでに蓄えていたダメージの一定割合を体力として回復する。
- **E — 野蛮な痛み：** 自動効果 - 自身の最大体力に応じて増加する、増加攻撃力を獲得する。 発動効果 - “往診用”バッグを敵に叩きつけ、自身の減少体力に応じた追加ダメージを与える。対象をキルした場合はその敵を弾き飛ばし、接触した敵にダメージを与える。
- **R — マキシマム投与：** 自身に薬品を注入し、減少体力の一定割合を瞬時に回復する。さらに移動速度が増加し、長い時間をかけて最大体力の一部を自動回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - Eの自動効果で最大体力に応じた増加攻撃力を得る。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 457試合、全体勝率 51.2%
- **時間帯別勝率：** 〜20分 55.3%（n=76）、20〜25分 45.8%（n=72）、25〜30分 43.5%（n=92）、30〜35分 55.7%（n=106）、35分〜 54.1%（n=111）
- **最高帯：** 30〜35分（判定差 12.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-36|ドクター・ムンドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（500試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3083|ワーモグ アーマー]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=82、67.1% / 非該当47.8%、差+19.2pt）；[[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=138、63.8% / 非該当46.1%、差+17.6pt）
- **ステータス傾向：** 魔法防御（該当n=249、58.2% / 非該当43.8%、差+14.4pt）；攻撃力（該当n=150、56.7% / 非該当48.6%、差+8.1pt）
- **理論仮説：** [[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（n=14（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3748|タイタン ハイドラ]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### JUNGLE（300試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=31、64.5% / 非該当45.4%、差+19.2pt）；[[wiki/entities/items/item-3084|心の鋼]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（該当n=36、58.3% / 非該当45.8%、差+12.5pt）
- **ステータス傾向：** 攻撃力（該当n=89、56.2% / 非該当43.6%、差+12.6pt）；物理防御（該当n=237、48.5% / 非該当42.9%、差+5.7pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）；[[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（n=11（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-36|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=638）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/lux|ラックス（Lux）]] — 対象側勝率65.6%（21/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率60.6%（20/33）、n=33（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率50.0%（16/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率50.9%（29/57）、n=57（十分性の目安を満たす）。
  - [[wiki/entities/champions/malphite|マルファイト（Malphite）]] — 対象側勝率53.3%（16/30）、n=30（十分性の目安を満たす）。

### JUNGLE（対象n=400）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率54.8%（17/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率48.4%（15/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率47.1%（16/34）、n=34（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率33.3%（5/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率37.5%（9/24）、サンプル不足（n=24、十分性の目安30未満）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率44.4%（8/18）、サンプル不足（n=18、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象746試合、全体勝率51.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：不死者の握撃／打ちこわし・息継ぎ・超成長；副系天啓：疾駆・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 275/746 | 36.9% | 50.2% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・息継ぎ・超成長；副系天啓：魔法の靴・疾駆；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 87/746 | 11.7% | 55.2% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・息継ぎ・超成長；副系天啓：魔法の靴・ビスケットデリバリー；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 69/746 | 9.2% | 59.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.DrMundo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/DrMundo.png)

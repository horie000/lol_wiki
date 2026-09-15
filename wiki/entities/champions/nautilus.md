---
title: "ノーチラス"
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
  - role-support
  - data-dragon
champion_id: "Nautilus"
champion_key: "111"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Nautilus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nautilus.png"
---

# ノーチラス

![[raw/assets/champions/Nautilus.png|128]]

## 基本情報

- **英字ID：** `Nautilus`
- **キー：** `111`
- **称号：** 深海の巨人
- **データversion：** `16.18.1`

## 紹介

ビルジウォーターに最初の桟橋ができたころからすでに伝説となっていた孤独な男──「ノーチラス」の名で知られる防具に包まれた大男は、ブルーフレイム・アイルの沖の暗い海域をさまよっている。大昔の裏切りに突き動かされている彼は何の前触れもなく攻撃を仕掛け、巨大な錨を振り回しては、不運な者を助け、強欲な者を破滅へと引きずり込む。「ビルジウォーターの供物」を払わなかった者のもとに現れては、彼らを道連れにして波間へと沈むのだという。そうして「何人たりとも深海から逃れることはできない」という鉄の掟を知らしめているのだ。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 6 |
| `magic` | 6 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 646 |
| `hpperlevel` | 100 |
| `mp` | 400 |
| `mpperlevel` | 47 |
| `movespeed` | 325 |
| `armor` | 39 |
| `armorperlevel` | 4.95 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.65 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.706 |

## アビリティ

- **パッシブ — 鉄の錨：** 対象に最初に行う通常攻撃は与える物理ダメージが増加し、短時間スネア効果を与える。

- **Q — 錨投げ：** 前方に錨を投げる。敵に命中すると自身と対象を同時に引き寄せ、魔法ダメージを与える。錨が地形に命中した場合、自身を錨の地点まで引き寄せる。
- **W — 大海の激憤：** 一時的にシールドを獲得する。シールドが持続している間は通常攻撃が対象と周囲の敵に継続ダメージを与える。
- **E — 粉砕水：** 自身の周囲に3回爆発する衝撃波を発生させる。爆発のたびに敵にダメージとスロウ効果を与える。
- **R — 爆雷発射：** 錨を地面にたたきつけ、狙った敵チャンピオンを追尾する爆雷を発射する。爆雷は対象を追尾しながら、通った場所に衝撃波を引き起こし、巻き込んだ敵ユニットに魔法ダメージとノックアップを与える。爆雷が対象に命中すると爆発がおき、対象にノックアップとスタンを付与する。

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
- **対象試合：** 873試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 52.5%（n=158）、20〜25分 44.1%（n=136）、25〜30分 43.3%（n=217）、30〜35分 45.5%（n=176）、35分〜 47.8%（n=186）
- **最高帯：** 〜20分（判定差 9.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-111|ノーチラスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（1,618試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3109|騎士の誓い]] + [[wiki/entities/items/item-3174|装甲強化の進撃]]（該当n=32、75.0% / 非該当46.5%、差+28.5pt）；[[wiki/entities/items/item-3109|騎士の誓い]] + [[wiki/entities/items/item-3174|装甲強化の進撃]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=30、73.3% / 非該当46.6%、差+26.7pt）
- **ステータス傾向：** 移動速度（該当n=1538、47.3% / 非該当43.8%、差+3.5pt）；魔法防御（該当n=1487、47.3% / 非該当44.3%、差+3.1pt）
- **理論仮説：** [[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=4（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-111|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=2,057）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/singed|シンジド（Singed）]] — 対象側勝率67.6%（23/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/senna|セナ（Senna）]] — 対象側勝率66.0%（33/50）、n=50（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率54.4%（112/206）、n=206（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/xerath|ゼラス（Xerath）]] — 対象側勝率31.9%（15/47）、n=47（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率35.5%（60/169）、n=169（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率39.7%（56/141）、n=141（十分性の目安を満たす）。

### JUNGLE（対象n=26）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象2,983試合、全体勝率50.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／シールドバッシュ・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 1,406/2,983 | 47.1% | 49.2% |
| 2 | 主系不滅：アフターショック／シールドバッシュ・心身調整・生気付与；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 328/2,983 | 11.0% | 47.0% |
| 3 | 主系不滅：アフターショック／シールドバッシュ・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5011) | 133/2,983 | 4.5% | 52.6% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nautilus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nautilus.png)

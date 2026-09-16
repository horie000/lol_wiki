---
title: "アリスター"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-16
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

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 中盤寄り
- **対象試合：** 147試合、全体勝率 44.9%
- **時間帯別勝率：** 〜20分 38.7%（n=31）、20〜25分 57.9%（n=19）、25〜30分 46.2%（n=26）、30〜35分 47.4%（n=38）、35分〜 39.4%（n=33）
- **最高帯：** 20〜25分（判定差 18.5ポイント）
- **判定根拠：** 中間帯が最高、端点との差 18.5%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-12|アリスターの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（378試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=33、51.5% / 非該当47.5%、差+4.0pt）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=81、49.4% / 非該当47.5%、差+1.9pt）
- **ステータス傾向：** 魔力（該当n=48、52.1% / 非該当47.3%、差+4.8pt）；魔法防御（該当n=341、48.1% / 非該当45.9%、差+2.1pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 物理防御・体力・移動速度）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=6（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-12|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=575）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率61.2%（30/49）、n=49（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率60.6%（20/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率56.7%（17/30）、n=30（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率37.7%（26/69）、n=69（十分性の目安を満たす）。
  - [[wiki/entities/champions/thresh|スレッシュ（Thresh）]] — 対象側勝率37.8%（14/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率52.5%（31/59）、n=59（十分性の目安を満たす）。

### TOP（対象n=9）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象419試合、全体勝率51.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：宇宙の英知・ヘクステックフラッシュネイター；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 133/419 | 31.7% | 46.6% |
| 2 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系魔道：ニンバスクローク・水走り；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 23/419 | 5.5% | 26.1% |
| 3 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：ヘクステックフラッシュネイター・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 22/419 | 5.3% | 59.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Alistar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Alistar.png)

---
title: "オーロラ"
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
  - role-mage
  - role-assassin
  - data-dragon
champion_id: "Aurora"
champion_key: "893"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Aurora.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aurora.png"
---

# オーロラ

![[raw/assets/champions/Aurora.png|128]]

## 基本情報

- **英字ID：** `Aurora`
- **キー：** `893`
- **称号：** 世界の狭間の魔女
- **データversion：** `16.18.1`

## 紹介

生まれたときから、オーロラは精霊界と物質世界の間を行き来する独自の能力で人生を歩んでいた。精霊界の住民たちに関する知識を手に入れようと、故郷を離れて研究を進めていたとき、彼女は時とともに心が捻じれて自我を失い、はぐれた半神に遭遇した。彼の絶望を目撃し、オーロラはこの暴れる仲間が忘れてしまった自我を取り戻す方法を見つける覚悟を決めた──その旅のなかで、彼女はフレヨルドの辺境の地を訪ねてまわることとなった。

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
| `hp` | 607 |
| `hpperlevel` | 110 |
| `mp` | 475 |
| `mpperlevel` | 30 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.668 |

## アビリティ

- **パッシブ — 精霊の解放：** スキルおよび通常攻撃で敵にダメージを与えると、その敵を祓い、精霊を解放する。解放された精霊はオーロラの背後に付いてまわり、オーロラの体力を回復する。

- **Q — 折れ重なる魔法：** 呪いの塊を放ち、それが触れたすべての敵に呪いをかける。スキルを再発動すると呪いを自身のもとへ呼び戻し、その際に触れた敵にダメージを与える。
- **W — ベールを越えて：** 指定方向に飛び跳ね、着地時に精霊界に入って、少しの間、インビジブル状態になり、移動速度が増加する。
- **E — ウィアーディング：** 二つの領域を融合し、激しくほとばしる精霊魔法を放つ。敵に魔法ダメージとスロウ効果を与え、自身は安全を確保するために後方に飛び跳ねる。
- **R — 世界の狭間：** 指定方向に飛び跳ね、波動を放ち、それが触れたすべての敵にダメージとスロウ効果を与える。その後、敵にスロウ効果を与えるエリアを作り出し、自身はそのエリアの端から別の端にテレポートできるようになる。

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
- **対象試合：** 186試合、全体勝率 51.6%
- **時間帯別勝率：** 〜20分 55.9%（n=34）、20〜25分 52.2%（n=23）、25〜30分 41.3%（n=46）、30〜35分 50.0%（n=44）、35分〜 61.5%（n=39）
- **最高帯：** 35分〜（判定差 20.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-893|オーロラの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（302試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=66、65.2% / 非該当43.2%、差+21.9pt）；[[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=102、60.8% / 非該当41.5%、差+19.3pt）
- **ステータス傾向：** 物理防御（該当n=81、54.3% / 非該当45.7%、差+8.6pt）
- **理論仮説：** [[wiki/entities/items/item-4629|コズミック ドライブ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### TOP（49試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-4629|コズミック ドライブ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-893|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=417）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率53.5%（23/43）、n=43（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率51.1%（23/45）、n=45（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率48.6%（17/35）、n=35（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率47.2%（17/36）、n=36（十分性の目安を満たす）。

### TOP（対象n=78）

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

### MIDDLE（対象472試合、全体勝率48.5%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／血の味わい・グリスリー メメント・至極の賞金首狩り；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 99/472 | 21.0% | 42.4% |
| 2 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・至極の賞金首狩り；副系魔道：マナフローバンド・至高；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 41/472 | 8.7% | 68.3% |
| 3 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・至極の賞金首狩り；副系魔道：追火・マナフローバンド；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 36/472 | 7.6% | 55.6% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Aurora` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aurora.png)

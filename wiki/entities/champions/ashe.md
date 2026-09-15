---
title: "アッシュ"
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
  - role-marksman
  - role-support
  - data-dragon
champion_id: "Ashe"
champion_key: "22"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Ashe.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ashe.png"
---

# アッシュ

![[raw/assets/champions/Ashe.png|128]]

## 基本情報

- **英字ID：** `Ashe`
- **キー：** `22`
- **称号：** 氷の射手
- **データversion：** `16.18.1`

## 紹介

アッシュはアヴァローサンのアイスボーンの戦母であり、北部でもっとも数の多い部隊を率いている。先祖から受け継いだ魔力を手に入れて真なる氷の弓で戦う彼女は、ストイックで知的な理想家だが、リーダーとしての自らの役割には戸惑いがある。部族の人間が彼女は生まれ変わったアヴァローサの伝説の英雄だと信じる中、アッシュは古代から続く部族の土地を取り戻して、もう一度フレヨルドを統一しようと望んでいる。

## 分類

- **役割タグ：** `Marksman`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 3 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 101 |
| `mp` | 280 |
| `mpperlevel` | 35 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 600 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — フロストショット：** 通常攻撃が命中した対象にスロウ効果を付与する。さらにその対象に通常攻撃をすると、ダメージが増加する。 アッシュのクリティカルは追加ダメージを一切与えない代わりに、対象により強力なスロウ効果を付与する。

- **Q — レンジャーフォーカス：** 通常攻撃によって「フォーカス」のスタックがたまるようになり、スタックが最大になるとすべて消費して「レンジャーフォーカス」を使用できる。効果時間中は攻撃速度が増加し、通常攻撃が強力な「疾風の矢」に変化する。
- **W — ボレー：** 矢を扇状に発射し、命中した敵にダメージを与える。同時に、命中した相手に「フロストショット」のレベルに応じたスロウ効果を付与する。
- **E — スカウトホーク：** マップ上の指定した地点へ「ホークスピリット」を放ち、視界を確保することができる。
- **R — クリスタルアロー：** アッシュが一直線に飛翔する氷の矢を放つ。最初に命中した敵チャンピオンにダメージを与え、飛距離に応じたスタン効果を付与する。氷の矢は砕けると同時に周囲の敵ユニットにもダメージを与え、移動速度を低下させる。

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
- **対象試合：** 930試合、全体勝率 48.4%
- **時間帯別勝率：** 〜20分 45.6%（n=149）、20〜25分 52.6%（n=135）、25〜30分 47.7%（n=220）、30〜35分 48.4%（n=221）、35分〜 48.3%（n=205）
- **最高帯：** 20〜25分（判定差 7.0ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-22|アッシュの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,725試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=59、74.6% / 非該当47.8%、差+26.8pt）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=75、73.3% / 非該当47.6%、差+25.8pt）
- **ステータス傾向：** クリティカル率（該当n=1560、50.3% / 非該当33.3%、差+17.0pt）；移動速度（該当n=1634、49.3% / 非該当37.4%、差+12.0pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=7（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-3046|ファントム ダンサー]]（n=6（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）

### UTILITY（60試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-22|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=2,164）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/teemo|ティーモ（Teemo）]] — 対象側勝率68.2%（30/44）、n=44（十分性の目安を満たす）。
  - [[wiki/entities/champions/irelia|イレリア（Irelia）]] — 対象側勝率63.5%（33/52）、n=52（十分性の目安を満たす）。
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率61.8%（55/89）、n=89（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/senna|セナ（Senna）]] — 対象側勝率29.7%（11/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/sivir|シヴィア（Sivir）]] — 対象側勝率42.9%（39/91）、n=91（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率46.1%（95/206）、n=206（十分性の目安を満たす）。

### UTILITY（対象n=72）

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

### BOTTOM（対象2,600試合、全体勝率49.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 迅速・切り崩し；副系天啓：疾駆・ビスケットデリバリー；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 1,275/2,600 | 49.0% | 49.5% |
| 2 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 迅速・切り崩し；副系天啓：ビスケットデリバリー・疾駆；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 371/2,600 | 14.3% | 50.7% |
| 3 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 迅速・切り崩し；副系天啓：キャッシュバック・疾駆；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 205/2,600 | 7.9% | 45.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ashe` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ashe.png)

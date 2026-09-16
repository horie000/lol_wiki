---
title: "ユナラ"
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
  - role-marksman
  - data-dragon
champion_id: "Yunara"
champion_key: "804"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Yunara.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yunara.png"
---

# ユナラ

![[raw/assets/champions/Yunara.png|128]]

## 基本情報

- **英字ID：** `Yunara`
- **キー：** `804`
- **称号：** 揺るがぬ誓い
- **データversion：** `16.18.1`

## 紹介

アイオニアへの揺るぎない忠誠心を胸にユナラは精霊界に身を隠し、均衡の守人に代々受け継がれる遺物「アイオン・エルナ」で修行を重ねた。あらゆるものを犠牲にしてなお、調和を乱すものを排し、争いを絶つという誓いは揺るがず、その信仰もまた決して失われていない。だが、彼女を待ち受ける世界と、再び蘇った古の脅威の影は、ユナラの決意のすべてを試すことになる。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 0 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 110 |
| `mp` | 275 |
| `mpperlevel` | 45 |
| `movespeed` | 325 |
| `armor` | 25 |
| `armorperlevel` | 4.4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 575 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.65 |

## アビリティ

- **パッシブ — 始まりの地への誓い：** クリティカル攻撃が追加魔法ダメージを与える。

- **Q — 精神修養：** 攻撃速度が増加し、通常攻撃時効果で追加ダメージを与え、通常攻撃が周囲の敵に拡散する。
- **W — 裁きの弧/滅びの弧：** 回転する珠を撃ち出し、敵にダメージとスロウ効果を与える。超越状態では、レーザー状に精霊魔法を発射して、敵にダメージとスロウ効果を与える。
- **E — カンメイの歩み/触れ得ぬ影：** 移動速度が増加し、ゴースト化する。超越状態では、代わりに指定方向にダッシュする。
- **R — 自己超越：** 超越状態になり、通常スキルがアップグレードされる。

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

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 496試合、全体勝率 50.4%
- **時間帯別勝率：** 〜20分 52.3%（n=86）、20〜25分 48.6%（n=74）、25〜30分 50.5%（n=107）、30〜35分 54.0%（n=126）、35分〜 45.6%（n=103）
- **最高帯：** 30〜35分（判定差 8.3ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-804|ユナラの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（951試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3085|ルナーン ハリケーン]]（該当n=32、71.9% / 非該当47.0%、差+24.9pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3033|モータル リマインダー]] + [[wiki/entities/items/item-3085|ルナーン ハリケーン]]（該当n=30、70.0% / 非該当47.1%、差+22.9pt）
- **ステータス傾向：** ライフスティール（該当n=149、57.7% / 非該当46.0%、差+11.7pt）；物理防御（該当n=116、56.9% / 非該当46.6%、差+10.3pt）
- **理論仮説：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3085|ルナーン ハリケーン]]（n=6（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）；[[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-3046|ファントム ダンサー]]（n=2（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-804|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=1,250）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/irelia|イレリア（Irelia）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/galio|ガリオ（Galio）]] — 対象側勝率58.8%（30/51）、n=51（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率56.5%（35/62）、n=62（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率37.8%（31/82）、n=82（十分性の目安を満たす）。
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率41.1%（30/73）、n=73（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率41.4%（48/116）、n=116（十分性の目安を満たす）。

### MIDDLE（対象n=1）

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

### BOTTOM（対象1,022試合、全体勝率49.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 迅速・切り崩し；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 197/1,022 | 19.3% | 47.7% |
| 2 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 血脈・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 169/1,022 | 16.5% | 56.8% |
| 3 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 迅速・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 88/1,022 | 8.6% | 53.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yunara` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yunara.png)

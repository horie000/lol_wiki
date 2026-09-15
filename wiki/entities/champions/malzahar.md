---
title: "マルザハール"
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
  - data-dragon
champion_id: "Malzahar"
champion_key: "90"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Malzahar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malzahar.png"
---

# マルザハール

![[raw/assets/champions/Malzahar.png|128]]

## 基本情報

- **英字ID：** `Malzahar`
- **キー：** `90`
- **称号：** ヴォイドの予言者
- **データversion：** `16.18.1`

## 紹介

あらゆる生命の合一にすべてを捧げる熱狂的な予言者マルザハールは、新たに現れたヴォイドこそルーンテラを救済へと導く道なのだと固く信じている。シュリーマの不毛の砂漠の中、彼は心の中に囁いた声に導かれ、古代イカシアにたどり着いた。その廃墟の地で彼は、ヴォイドそのものの核たる闇を覗き込み、新たな力と目的を与えられた。今やマルザハールは己を「羊飼い」と考えており、人々にその福音を広めるための力…あるいは、地の底に棲むヴォイドの怪物たちを解き放つ力を振るうのである。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 9 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 101 |
| `mp` | 375 |
| `mpperlevel` | 28 |
| `movespeed` | 335 |
| `armor` | 18 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 500 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ヴォイドシフト：** 一定時間ダメージか行動妨害を受けていない時、マルザハールは強力なダメージ軽減と行動阻害無効を得る。この効果はダメージを受けた後も短期間継続する。

- **Q — ヴォイドコール：** ヴォイドへ繋がるゲートを2カ所に発生させる。発動から一瞬遅れてゲートからエネルギーが発射され、命中した敵ユニットに魔法ダメージを与える。敵チャンピオンに対しては、さらにサイレンス効果を与える。
- **W — ヴォイドスワーム：** 近くの敵を攻撃する「ヴォイドリング」を召喚する。
- **E — 虚性侵蝕：** 指定した対象の精神を痛みに悶え苦しむ幻覚で蝕み、継続ダメージを与える。対象に他のスペルを使用すると幻覚の効果が更新される。 幻覚に侵蝕されている敵が倒れると近くの敵ユニットに効果が伝染し、マルザハールのマナが回復する。幻覚に蝕まれている敵は、マルザハールが召喚した「ヴォイドリング」に狙われる。
- **R — ネザーグラスプ：** ダメージを与える負のエネルギーに満ちた領域上で敵チャンピオンにヴォイドのエネルギーを注ぎ込み、サプレッション効果を付与する。

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
- **対象試合：** 446試合、全体勝率 53.6%
- **時間帯別勝率：** 〜20分 46.9%（n=64）、20〜25分 52.6%（n=76）、25〜30分 57.7%（n=111）、30〜35分 51.5%（n=99）、35分〜 56.2%（n=96）
- **最高帯：** 25〜30分（判定差 10.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-90|マルザハールの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（827試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=40、70.0% / 非該当51.3%、差+18.7pt）；[[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=207、62.3% / 非該当48.9%、差+13.4pt）
- **ステータス傾向：** 物理防御（該当n=215、54.4% / 非該当51.5%、差+2.9pt）
- **理論仮説：** [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=14（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=5（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### TOP（35試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（n=4（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（n=2（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-90|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=1,105）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/karma|カルマ（Karma）]] — 対象側勝率68.6%（24/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率63.5%（47/74）、n=74（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率61.0%（50/82）、n=82（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率37.1%（13/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率38.1%（24/63）、n=63（十分性の目安を満たす）。
  - [[wiki/entities/champions/mel|メル（Mel）]] — 対象側勝率43.3%（13/30）、n=30（十分性の目安を満たす）。

### BOTTOM（対象n=44）

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

### MIDDLE（対象1,319試合、全体勝率51.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：死神の残り火／マナフローバンド・至高・追火；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 200/1,319 | 15.2% | 53.5% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・至高・強まる嵐；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 176/1,319 | 13.3% | 51.7% |
| 3 | 主系魔道：エアリー召喚／マナフローバンド・至高・追火；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 120/1,319 | 9.1% | 53.3% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Malzahar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Malzahar.png)

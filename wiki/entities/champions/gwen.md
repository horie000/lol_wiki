---
title: "グウェン"
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
  - role-fighter
  - data-dragon
champion_id: "Gwen"
champion_key: "887"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Gwen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gwen.png"
---

# グウェン

![[raw/assets/champions/Gwen.png|128]]

## 基本情報

- **英字ID：** `Gwen`
- **キー：** `887`
- **称号：** 聖なるお針子
- **データversion：** `16.18.1`

## 紹介

魔法によって人間となり、命を与えられた元人形のグウェンは、かつて自分を生み出したまさにその道具を携えている。一歩ごとに作り手の愛の重みを感じながら、あらゆることに感謝を忘れない。グウェンが意のままに操る「聖なる霧」は、古代の防護魔法であり、自身が手にしたハサミ、針、そして縫い糸もその祝福を授かっている。目新しいものに囲まれながらも、グウェンは壊れた世界に生き残っている善意を守るため、大いなる喜びをもって戦い続けようと固く誓っている。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 4 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 115 |
| `mp` | 330 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 39 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 裁断：** 通常攻撃が対象の体力に応じて追加魔法ダメージを与える。この効果でチャンピオンに与えたダメージの一定割合を体力として回復する。

- **Q — チョキチョキッ！：** ハサミで扇状の範囲を最大6回切りつけて魔法ダメージを与える。範囲の中心にいるユニットには確定ダメージを与え、切るたびに固有スキルの効果を適用する。
- **W — 聖なる霧：** 霧を召喚して、霧の外にいる敵から身を守る。霧の中にいる敵からしか対象指定されない。
- **E — スキップスラッシュ：** 短い距離をダッシュして数秒間、攻撃速度と射程が増加し、通常攻撃時効果で魔法ダメージを与える。効果時間中に通常攻撃を命中させた場合、このスキルのクールダウンが一定割合解消される。
- **R — 針仕事：** 針を投げ、命中した敵にスロウ効果と魔法ダメージを与えて、チャンピオンに命中した場合は「裁断」を適用する。 このスキルは最大2回まで再発動可能で、再発動するたびに投げる針の本数とダメージが増加する。

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
- **対象試合：** 299試合、全体勝率 47.8%
- **時間帯別勝率：** 〜20分 46.5%（n=43）、20〜25分 48.9%（n=45）、25〜30分 53.0%（n=66）、30〜35分 48.1%（n=77）、35分〜 42.6%（n=68）
- **最高帯：** 25〜30分（判定差 10.4ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-887|グウェンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（378試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-3115|ナッシャー トゥース]]（該当n=47、68.1% / 非該当44.7%、差+23.4pt）；[[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-3115|ナッシャー トゥース]] + [[wiki/entities/items/item-4633|リフトメーカー]]（該当n=35、65.7% / 非該当45.8%、差+19.9pt）
- **ステータス傾向：** 物理防御（該当n=201、51.2% / 非該当43.5%、差+7.7pt）；攻撃速度（該当n=348、47.7% / 非該当46.7%、差+1.0pt）
- **理論仮説：** [[wiki/entities/items/item-4629|コズミック ドライブ]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=8（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=5（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### JUNGLE（143試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3115|ナッシャー トゥース]] + [[wiki/entities/items/item-4633|リフトメーカー]]（該当n=51、52.9% / 非該当52.2%、差+0.8pt）
- **ステータス傾向：** 物理防御（該当n=57、57.9% / 非該当48.8%、差+9.1pt）
- **理論仮説：** [[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]]（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-4629|コズミック ドライブ]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-887|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=482）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率65.2%（30/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率64.3%（27/42）、n=42（十分性の目安を満たす）。
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率61.1%（22/36）、n=36（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率44.1%（15/34）、n=34（十分性の目安を満たす）。

### JUNGLE（対象n=218）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率76.5%（13/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率61.9%（13/21）、サンプル不足（n=21、十分性の目安30未満）。
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率58.8%（10/17）、サンプル不足（n=17、十分性の目安30未満）。
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

### TOP（対象204試合、全体勝率47.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／冷静沈着・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 53/204 | 26.0% | 41.5% |
| 2 | 主系栄華：征服者／冷静沈着・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 18/204 | 8.8% | 38.9% |
| 3 | 主系栄華：征服者／冷静沈着・レジェンド: 迅速・背水の陣；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 16/204 | 7.8% | 50.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gwen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gwen.png)

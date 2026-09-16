---
title: "チョ＝ガス"
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
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
tags:
  - champion
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Chogath"
champion_key: "31"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Chogath.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Chogath.png"
---

# チョ＝ガス

![[raw/assets/champions/Chogath.png|128]]

## 基本情報

- **英字ID：** `Chogath`
- **キー：** `31`
- **称号：** 未知なる恐怖
- **データversion：** `16.18.1`

## 紹介

チョ＝ガスはルーンテラの眩しい太陽の下に初めて現れた時から、純粋な飢えの衝動に突き動かされていた。チョ＝ガスはすべての生命を吸収しようとするヴォイドの欲望を完璧に具現化した存在であり、その複雑な身体機能は物質を素早く変換して自らの肉体の成長に繋げることが可能であり、筋肉は密度と大きさが増して、昆虫のような外皮は有機的なダイヤモンドのように固くなる。体が大きくなる必要がない時は、余った物質を剃刀のように鋭い槍にして吐き出し、獲物をあとで食べるために串刺しにしておく。

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 7 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 644 |
| `hpperlevel` | 94 |
| `mp` | 270 |
| `mpperlevel` | 60 |
| `movespeed` | 345 |
| `armor` | 38 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 7.2 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.44 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 暴食：** 敵ユニットを倒すたびに体力とマナが回復する。 この回復量はチョ＝ガスのレベルに応じて増加する。

- **Q — ラプチャー：** 指定地点に下から突き出るようにトゲを発生させる。効果範囲内の敵ユニットをノックアップさせてダメージを与え、スロウ効果を付与する。
- **W — スクリーム：** 扇形の範囲内にいる敵に恐ろしい叫声を浴びせ、魔法ダメージと数秒間のサイレンス効果を与える。
- **E — ヴォーパルスパイク：** 通常攻撃時に鋭いトゲを発射し、自身の前方にいる敵ユニットにダメージとスロウ効果を与える。
- **R — 捕食：** 敵ユニットを「捕食」して高い確定ダメージを与える。このスキルで敵ユニットを倒すと自身は巨大化して、最大体力が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中5位（上位15%）。体力644、物理防御38、攻撃力69、移動速度345。
  - 「捕食」で敵を倒すと巨大化し、最大体力が増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 終盤寄り
- **対象試合：** 378試合、全体勝率 52.4%
- **時間帯別勝率：** 〜20分 47.2%（n=53）、20〜25分 48.4%（n=62）、25〜30分 50.0%（n=84）、30〜35分 52.9%（n=87）、35分〜 59.8%（n=92）
- **最高帯：** 35分〜（判定差 12.6ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 12.6%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-31|チョ＝ガスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（438試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=40、72.5% / 非該当51.8%、差+20.7pt）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=43、72.1% / 非該当51.6%、差+20.4pt）
- **ステータス傾向：** 物理防御（該当n=382、56.0% / 非該当37.5%、差+18.5pt）；マナ（該当n=35、57.1% / 非該当53.3%、差+3.8pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

### JUNGLE（106試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 魔法防御（該当n=54、46.3% / 非該当38.5%、差+7.8pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（n=12（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-31|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=531）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率61.5%（24/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率58.5%（24/41）、n=41（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率55.2%（32/58）、n=58（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率29.4%（10/34）、n=34（十分性の目安を満たす）。
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率60.0%（30/50）、n=50（十分性の目安を満たす）。

### MIDDLE（対象n=119）

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

### TOP（対象155試合、全体勝率54.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：ヘイルブレード／追い打ち・グリスリー メメント・至極の賞金首狩り；副系魔道：アクシオム アルカニスト・追い風；シャードUNKNOWN(5008)・UNKNOWN(5010)・UNKNOWN(5001) | 39/155 | 25.2% | 53.8% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・心身調整・超成長；副系天啓：疾駆・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 33/155 | 21.3% | 57.6% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・心身調整・超成長；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 13/155 | 8.4% | 53.8% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 高勝率候補（上位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| CHALLENGER | 5 | 38 | 25勝/13敗 | 65.8% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Chogath` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Chogath.png)

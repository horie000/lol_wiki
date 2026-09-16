---
title: "アンベッサ"
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
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Ambessa"
champion_key: "799"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/Ambessa.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ambessa.png"
---

# アンベッサ

![[raw/assets/champions/Ambessa.png|128]]

## 基本情報

- **英字ID：** `Ambessa`
- **キー：** `799`
- **称号：** 戦乱の母
- **データversion：** `16.18.1`

## 紹介

メダルダの名を知る者なら誰もが、その家長であるアンベッサに敬意と恐れを抱いている。彼女はノクサスの将軍として、戦場における非情な力と恐れ知らずの決意という恐怖の組み合わせを体現する存在だ。家長としての彼女の役割にも大きな違いはなく、メダルダ家の権力を維持するためには抜け目のない狡猾さが必要となり、失敗や慈悲を許容する余地など残されていない。狼の非情ぶりを信奉する彼女は一族の権威を守るためなら手段を厭わない──それが自らの子への愛を犠牲にするとしても。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 0 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 110 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 4.9 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ドレイクハウンドの猛攻：** スキルを発動中に通常攻撃または移動操作をすると、スキル発動後に短い距離をダッシュして、次の通常攻撃の射程距離、ダメージ、攻撃速度が増加し、気を回復する。

- **Q — カニングスイープ/サンダリングスラム：** 両手のドレイクハウンドを自身の前方に向かって半円状に振り回し、刃が当たった敵に追加ダメージを与える。敵に攻撃が命中すると、次に発動するこのスキルが短時間変化し、自身の前方に向かって両手のドレイクハウンドを直線状に叩きつけ、最初に命中した敵に追加ダメージを与える。
- **W — 断交：** シールドを獲得し、少しの間身構えた後地面を叩きつけて周囲の敵にダメージを与える。身構えている間にミニオン以外からのダメージをブロックしていた場合、このスキルの与えるダメージが増加する。
- **E — ラセレイト：** 両手のドレイクハウンドを自身の周囲に振り回し、付近の敵にダメージとスロウ効果を与える。このスキルから「ドレイクハウンドの猛攻」を発動すると、ダッシュ終了後にもう一度攻撃する。
- **R — 公開処刑：** 指定した直線上の最も遠い敵チャンピオンの場所までブリンクし、到着時に敵にサプレッション効果を付与する。その後、敵を地面に叩きつけ、ダメージを与えスタンさせる。

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
- **対象試合：** 370試合、全体勝率 45.1%
- **時間帯別勝率：** 〜20分 40.7%（n=59）、20〜25分 46.3%（n=54）、25〜30分 41.5%（n=82）、30〜35分 48.5%（n=103）、35分〜 47.2%（n=72）
- **最高帯：** 30〜35分（判定差 7.9ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-799|アンベッサの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（563試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2517|終わりなき飢え]] + [[wiki/entities/items/item-6692|赤月の刃]]（該当n=33、66.7% / 非該当46.4%、差+20.3pt）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6333|デス ダンス]]（該当n=102、55.9% / 非該当45.8%、差+10.1pt）
- **ステータス傾向：** 魔法防御（該当n=198、48.5% / 非該当47.1%、差+1.4pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=2（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### JUNGLE（129試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6696|アクシオム アーク]] + [[wiki/entities/items/item-6697|ヒュブリス]]（該当n=33、60.6% / 非該当41.7%、差+18.9pt）；[[wiki/entities/items/item-6333|デス ダンス]] + [[wiki/entities/items/item-6696|アクシオム アーク]]（該当n=41、53.7% / 非該当43.2%、差+10.5pt）
- **ステータス傾向：** 魔法防御（該当n=35、48.6% / 非該当45.7%、差+2.8pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3161|ショウジンの矛]]（n=4（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-799|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=724）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率65.7%（23/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/lux|ラックス（Lux）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率56.4%（31/55）、n=55（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率32.5%（13/40）、n=40（十分性の目安を満たす）。
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率42.4%（14/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率48.4%（15/31）、n=31（十分性の目安を満たす）。

### JUNGLE（対象n=216）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率47.4%（9/19）、サンプル不足（n=19、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率41.2%（7/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率41.2%（7/17）、サンプル不足（n=17、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/briar|ブライアー（Briar）]] — 対象側勝率33.3%（5/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象710試合、全体勝率47.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：不死者の握撃／シールドバッシュ・息継ぎ・超成長；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 212/710 | 29.9% | 43.4% |
| 2 | 主系不滅：不死者の握撃／シールドバッシュ・息継ぎ・超成長；副系覇道：サドンインパクト・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 49/710 | 6.9% | 42.9% |
| 3 | 主系不滅：不死者の握撃／シールドバッシュ・息継ぎ・気迫；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 23/710 | 3.2% | 56.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### ピック数上位5に入った帯

| 観測帯 | 帯内順位 | 試合数 | ピック率 | 勝敗 | 勝率 |
| --- | ---: | ---: | ---: | --- | ---: |
| CHALLENGER | 2 | 197 | 2.0% | 98勝/99敗 | 49.7% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ambessa` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ambessa.png)

# Riot API ランク戦試合結果解析スクリプト仕様書

- 仕様バージョン：1.4（最新レポート連動Lintを追加）
- 作成日：2026-09-15
- 改訂日：2026-09-16
- 対象ゲーム：League of Legends
- 実装：`scripts/riot_ranked_match_analyzer.py`、`scripts/riot_ranked_tier_analyzer.py`
- 関連実装：`scripts/riot_champion_query.py`、`scripts/riot_champion_item_synergy.py`、`scripts/riot_champion_build_wiki_sync.py`、`scripts/riot_champion_matchup_wiki_sync.py`、`scripts/riot_champion_rune_wiki_sync.py`、`scripts/riot_champion_tier_wiki_sync.py`、`scripts/riot_champion_duration_wiki_sync.py`、`scripts/lint.py`
- 関連仕様：[Riotレポート連動Lint仕様書](riot-lint-report-sync-spec.md)
- 関連仕様：[Riot API ランク戦データ収集仕様書](riot-ranked-match-collector-spec.md)

## 1. 目的

取得済みの Match-v5 試合結果を、チャンピオン、ロール、アイテム、ルーン、サモナースペル、チーム構成、試合時間などの単位で集計し、後続の検証や Wiki への分析結果の取り込みを助ける。

このスクリプトは統計量の算出と再現可能なレポート生成を担当する。勝率から因果関係、最適ビルド、チャンピオン間の絶対的な相性を断定しない。分析結果に対する解釈や Wiki ページの作成は別工程とする。

実試合からチャンピオン・アイテムの組み合わせを見直す場合は、最終所持状態を使った条件付きの記述統計を別スクリプトで生成する。これは原典由来の `champion-synergy-*` タグを自動的に置換するものではない。

## 2. 基本方針

- `raw/` 配下の入力ファイルを読み取るだけとし、原典や収集済みデータを変更しない。
- Riot APIへ接続せず、APIキーを要求しない。解析対象はローカルファイルに限定する。
- 同じ試合の重複、欠損、異なるランク帯からの重複観測を明示的に扱う。
- 出力には `puuid`、`summonerId`、`summonerName`、`riotIdGameName`、`riotIdTagline` などの個人識別情報を含めない。
- 入力ファイル、解析条件、データ品質、スクリプトバージョンをマニフェストへ記録し、同じ入力と条件から同じ集計結果を再生成できるようにする。
- すべての率には分母を添え、サンプル数の少ない結果には最小件数によるフィルターを適用する。

## 3. 入力仕様

### 3.1 優先する入力形式

収集器がランク帯ごとに出力する次の JSONL を正規入力とする。

```text
raw/sources/riot-ranked-matches/**/matches.jsonl
```

1行の外側レコードは次のフィールドを持つ。

| フィールド | 必須 | 用途 |
| --- | --- | --- |
| `schema_version` | いいえ | 入力スキーマの検証 |
| `match_id` | 推奨 | 試合の識別子。ない場合は `match.metadata.matchId` を使う |
| `game_start_timestamp` | 推奨 | 時系列の並べ替え。ない場合は `match.info.gameStartTimestamp` または `gameCreation` を使う |
| `observed_tier` | いいえ | 収集時点で観測したランク帯 |
| `observed_divisions` | いいえ | 収集時点で観測したディビジョン |
| `match` | 必須 | Match-v5 のレスポンス。`metadata` と `info` を含む |

入力にディレクトリを指定した場合は、配下の `matches.jsonl` を再帰的に探索する。ファイルを直接指定する入力も許可する。

### 3.2 収集キャッシュの入力

収集途中のデータを解析できるよう、次のキャッシュ形式も受け付ける。

```text
raw/sources/riot-ranked-matches/.cache/matches/<match-id>.json
```

キャッシュレコードは `schema_version`、`cached_at`、`match` を持つ。キャッシュにはランク帯の観測情報がないため、キャッシュだけを入力した場合の `observed_tier` は `UNKNOWN` とする。ランク帯別の比較を行う場合は、完成済みの `matches.jsonl` を優先する。

### 3.3 メタデータの解決

IDから表示名を解決する場合は、外部通信ではなく次のローカル Data Dragon アーカイブを使う。

```text
raw/sources/dragontail-16.18.1.tgz
```

対象メンバーは次のとおり。

- `16.18.1/data/ja_JP/item.json`
- `16.18.1/data/ja_JP/runesReforged.json`
- `16.18.1/data/ja_JP/summoner.json`

表示名を解決できないIDは、推測で補わず `UNKNOWN(<id>)` として品質レポートへ記録する。チャンピオン名は Match-v5 の `championName` を優先し、必要な場合だけローカルデータで補完する。

## 4. 正規化処理

### 4.1 試合単位

1. 試合IDは外側の `match_id`、次に `match.metadata.matchId` の順で解決する。
2. 同じ試合IDを複数の `matches.jsonl` から読み込んだ場合は、分析の基礎試合集合では1件に統合する。
3. 統合後も、試合に紐づく `observed_tiers`、`observed_divisions`、入力ファイル一覧は集合として保持する。
4. 同じ試合IDに異なる Match-v5 本体がある場合は、最初のレコードを黙って優先せず、`conflicting_payload` として品質レポートへ記録する。デフォルトではその試合を統計集計から除外する。
5. `info.queueId` が指定キューと一致しない試合は除外する。

### 4.2 ランク帯の扱い

`observed_tier` は試合実施時の参加者全員のランクではなく、収集時点で試合IDを発見したプレイヤーの所属帯である。したがって、レポートでは「実際の試合時ランク」ではなく「観測ランク帯」と表記する。

同じ試合が複数の観測ランク帯に現れた場合は、次の2つの集計モードを持つ。

| モード | 用途 | 重複の扱い |
| --- | --- | --- |
| `all` | 全体集計 | 試合IDごとに1回だけ数える。ランク帯は `MIXED` とする |
| `observed` | 観測ランク帯別の比較 | 1試合を観測された各ランク帯へ1回ずつ展開する。同一帯内では1回だけ数える |

既定値は `observed` とするが、レポートには必ず `tier_mode` と注意書きを出す。キャッシュ入力のみの場合は `UNKNOWN` の観測帯として扱う。

### 4.3 参加者単位

- 参加者キーは `match_id` と `participantId` の組み合わせとする。
- ロールは `teamPosition`、`individualPosition`、`lane` の順に利用可能な値を採用する。
- `teamId`、`teamPosition`、`championId`、`championName`、`win` が欠ける参加者は、該当する集計から除外し、欠損件数を記録する。
- アイテムは `item0`～`item5` を完成時点の通常スロット、`item6` をトリンケット等の補助スロットとして扱う。ID `0` は未装備として除外する。
- ルーンは `perks.styles` と `perks.statPerks` のIDを抽出する。キーストーン、選択ルーン、ステータスシャードを区別する。
- サモナースペルは `summoner1Id` と `summoner2Id` を抽出する。

### 4.4 完全試合

完全試合は、次の条件を満たす試合とする。

- 参加者が10人いる。
- `participantId` が1～10で重複しない。
- `teamId` が2チームに分かれ、各チームに5人いる。
- 2チームの勝敗が解決できる。
- 試合時間が正の値である。

既定では不完全試合をチャンピオン・アイテム・ルーン等の率の分母から除外する。ただし、品質レポートには不完全試合数を残す。`--include-incomplete` を指定した場合だけ、算出可能な項目に限って含める。

## 5. CLI仕様

実装予定のコマンド名は次のとおり。

```bash
python3 scripts/riot_ranked_match_analyzer.py \
  --input raw/sources/riot-ranked-matches \
  --output reports/riot-ranked-match-analysis \
  --queue-id 420 \
  --tier-mode observed \
  --format markdown,csv,json
```

| オプション | 既定値 | 説明 |
| --- | --- | --- |
| `--input PATH` | 必須 | JSONL、キャッシュファイル、または探索対象ディレクトリ。複数指定可 |
| `--output PATH` | `reports/riot-ranked-match-analysis` | レポート出力先。`raw/` は入力専用とし、既定では `raw/` 配下を拒否 |
| `--queue-id` | `420` | 対象キュー。指定キュー以外は除外 |
| `--tier-mode` | `observed` | `all` または `observed` |
| `--tiers` | 全観測帯 | `IRON,GOLD,DIAMOND` のように観測帯を限定 |
| `--patch` | 全パッチ | `16.18` または `16.18.1` など `gameVersion` の前方一致 |
| `--date-from` / `--date-to` | なし | `gameStartTimestamp` のUTC日付で範囲指定 |
| `--roles` | 全ロール | `TOP,JUNGLE,MIDDLE,BOTTOM,UTILITY` をカンマ区切りで指定 |
| `--champions` | 全チャンピオン | チャンピオンIDまたは表示名をカンマ区切りで指定 |
| `--min-games` | `15` | 集計表に掲載する最小ゲーム数。品質表は除外しない |
| `--include-incomplete` | 無効 | 不完全試合を算出可能な集計へ含める |
| `--include-matchups` | 無効 | 味方ペア・ロール別対面の集計を生成 |
| `--format` | `markdown,csv,json` | 出力形式の組み合わせ |
| `--overwrite` | 無効 | 既存の実行ディレクトリを上書き |
| `--dry-run` | 無効 | 入力件数と解析条件だけを検証し、出力しない |

`--include-pii` のような個人情報出力オプションは設けない。個人単位の分析が必要になった場合は、別仕様として匿名化方法と利用範囲を先に定める。

## 6. 集計項目

### 6.1 試合・品質集計

- 入力ファイル数、入力レコード数、ユニーク試合数
- 重複レコード数、競合本体数、JSON不正件数
- 完全試合数、不完全試合数、参加者欠損数
- キュー別、パッチ別、観測ランク帯別の試合数
- 試合時間の件数、平均、中央値、最小、最大、10・25・75・90パーセンタイル
- 投了、早期降参、試合終了理由の件数

### 6.2 チャンピオン集計

全体および `観測ランク帯 × パッチ × ロール` の組み合わせごとに、次を出力する。

- `champion_id`, `champion_name`
- `games`, `wins`, `losses`, `win_rate`
- `pick_count`, `pick_rate`, `pick_rate_denominator`
- `avg_kda`, `avg_cs_per_min`, `avg_gold_per_min`
- `avg_damage_share`, `avg_vision_score`
- `ban_count`, `ban_match_count`, `ban_rate`（入力に有効なban情報がある場合）

`pick_rate` の定義は、全体では `champion_games / (完全試合数 × 10)` とする。ロールを指定した表では、対象ロールの有効参加者スロット数を分母とする。`win_rate` は `wins / games` とし、割合と同時に分子・分母を出力する。

### 6.3 アイテム集計

`item0`～`item5` に存在するアイテムの所持率を、参加者単位で集計する。

- `item_id`, `item_name`
- `games`, `wins`, `win_rate`
- `holder_count`, `pick_rate`, `pick_rate_denominator`
- `avg_final_slot`
- 観測帯、パッチ、ロール、チャンピオン別の内訳

同じアイテムが複数スロットにある場合は、1参加者につき1所持として数える。`item0`～`item5` は最終状態であり、購入順、完成時刻、実戦上の因果効果を表さない。`item6` は既定では通常アイテム率に含めず、必要な場合に別集計する。

### 6.4 ルーン・サモナースペル集計

ルーンとスペルは参加者単位で次を集計する。

- ID、表示名、種類（キーストーン、選択ルーン、シャード、スペル）
- `games`, `wins`, `win_rate`, `pick_rate`, `pick_rate_denominator`
- 観測帯、パッチ、ロール、チャンピオン別の内訳

ルーンページの系統やスロットが原典から解決できない場合は、IDだけで集計し、未知メタデータとして記録する。

#### 6.4.1 チャンピオン別ルーン選択

チャンピオンと正規化ロールの組み合わせごとに、同じチャンピオン・ロールの参加者を分母としてルーン選択を集計する。通常のルーン集計とは別に、`champion-rune-summary.csv` と `analysis.json` の `results.champion_runes` へ出力する。

- 粒度は `champion_id × role × rune_kind × rune_id × rune_style_id` とする。`role=ALL` はチャンピオン単位の補助集計として併記し、ロール別の選択率の解釈には使わない。
- `champion_games`、`champion_wins`、`champion_losses` はチャンピオン・ロールの全参加者、`games`、`wins`、`losses` は当該ルーンを選択した参加者である。
- `pick_rate = games / champion_games`、`win_rate = wins / games`、`champion_win_rate = champion_wins / champion_games` とし、すべての分子・分母を出力する。
- 同一参加者の同一ルーンは1回だけ数える。キーストーン、通常ルーン、ステータスシャードを `rune_kind` で分け、シャードは3枠を別々に数えるため種類内の選択率を合計して100%とはしない。
- パッチ別の行は、同一チャンピオン・ロール・パッチの分母を一度だけ数えてから、`tier_mode=all` の全パッチ行を合算する。観測帯別行を足し合わせて全体値を作らない。
- `--min-games` はチャンピオン・ロールの母数とルーン選択数の双方に適用する。少数の選択肢は出力から除外するが、品質・解釈上の制約をレポートへ残す。
- 選択時勝率とチャンピオン全体勝率の差は未調整の記述統計であり、ルーンの因果効果、最適性、推奨を示さない。パッチ、ロール、プレイヤー、試合展開、選択バイアスを含む。
- `rune_style_id` は Data Dragon のルーン系統で解決し、ステータスシャードのIDは表示名辞書がない場合 `UNKNOWN(<id>)` とする。

#### 6.4.2 チャンピオン別ルーンセット

チャンピオン・正規化ロールごとに、Match-v5 `perks` の主系、キーストーン、主系3枠、副系、
副系2枠、`statPerks` の offense・flex・defense を一つの完全一致セットとして集計する。
`champion-rune-set-summary.csv` と `analysis.json` の `results.rune_sets` へ出力し、
`scripts/riot_champion_rune_wiki_sync.py` で各チャンピオンの観測数が最も多いロールに上位3件を同期する。

- 完全な主系2系統、主系4選択（先頭をキーストーン）、副系2選択、3シャードを持つ参加者だけをセット集計へ含める。欠落した枠は推測で補完しない。
- セットのキーは系統ID、選択ルーンIDの順序、シャードIDの順序で構成し、同じチャンピオン・ロール・セットをパッチ別に加算する。
- `champion_games` は同じチャンピオン・ロールの完全試合参加者、`games` はその完全セットを選択した参加者である。`pick_rate = games / champion_games`、`win_rate = wins / games` とする。
- `--min-games` はチャンピオン・ロールの母数へ適用する。完全セットのパッチ別行は全パッチ合算で上位を取りこぼさないよう保持し、entity同期では `--role-min-games`（既定15）を満たす観測数最多ロールを1つ選び、セットを選択数降順、同数時は勝率降順で最大3件表示する。
- entity表示にはセットの選択数・選択率・選択時勝率を併記する。Data Dragonでシャード名を解決できない場合は `UNKNOWN(<id>)` としてIDを保持する。
- 選択時勝率は未調整の記述統計であり、ルーンセットの因果効果、最適性、推奨を意味しない。パッチ、プレイヤー、対面、構成、試合時間、選択前状態は調整しない。

### 6.5 参加者パフォーマンス

Match-v5 の最終スコアから、参加者単位の値を集計する。ただし個人識別子は出力しない。

- KDA：`(kills + assists) / max(deaths, 1)`
- CS：`totalMinionsKilled + neutralMinionsKilled`
- CS/分：CS / `timePlayed`（分）
- ゴールド/分：`goldEarned` / `timePlayed`（分）
- チャンピオンへのダメージ/分
- チーム内チャンピオンへのダメージ割合：自身の `totalDamageDealtToChampions` / 同チーム合計
- `visionScore`、`wardsPlaced`、`wardsKilled`
- `firstBloodKill`、`firstBloodAssist`、`firstTowerKill`、`firstTowerAssist`

値がない項目は0に置換せず欠損として扱い、平均の分母から除外する。

### 6.6 ロール別ゴールド獲得率

全体および `観測ランク帯 × パッチ × ロール` の組み合わせごとに、最終スコアからロール単位のゴールド獲得率を集計する。ロールは通常の5ロール（`TOP`、`JUNGLE`、`MIDDLE`、`BOTTOM`、`UTILITY`）とし、解決できない参加者は `UNKNOWN` として品質確認用に残す。

- 参加者ごとのゴールド/分：`goldEarned / (timePlayed / 60)`。各参加者を同じ重みで平均する `avg_gold_per_min`、中央値、P10、P90を出力する。
- 加重ゴールド/分：有効な参加者の `goldEarned` 合計を `timePlayed`（分）の合計で割った `weighted_gold_per_min`。ロール全体の総量ベースの速度として扱う。
- チーム内ゴールド比率：同じ試合・チームの最終 `goldEarned` 合計に対する参加者の比率を算出し、ロール別平均 `avg_team_gold_share` と有効分母を出力する。
- 分母：参加者数、試合数、ゴールド有効参加者数、チーム内比率の有効参加者数を併記する。勝率は勝敗が解決できた参加者だけを分母とする。

この指標は試合終了時点の最終ゴールドを試合時間で正規化した記述統計であり、15分時点のゴールド差、ゴールド獲得の時間的傾き、購入時刻、レーンで実際に得た収入、勝因を示さない。ロール別の差は、チャンピオン、パッチ、試合展開、構成、プレイヤーサンプルなどの交絡を含む。

### 6.7 チーム構成・対面集計

`--include-matchups` 指定時だけ生成する。最小ゲーム数未満の行は通常表から除外する。

- 味方シナジー：同一チーム内のチャンピオンの順序なしペア
- ロール別対面：反対チームで同じ正規化ロールに割り当てられたチャンピオンの有向ペア
- チーム構成：5体のチャンピオン集合と勝敗
- 各行：`games`, `wins`, `win_rate`, `sample_size`, `observed_tiers`, `patches`

対面は `teamPosition` 等の最終スコアから推定した組み合わせであり、レーンで実際に対面したことや、チャンピオン固有のカウンター関係を保証しない。味方ペアや対面の率は、プレイヤー、構成、パッチ、試合選択の交絡を含む記述統計に限定する。

### 6.8 チャンピオン指定クエリ

全体集計とは別に、対象チャンピオンを1体指定して、少数の結果をすぐ確認できる専用スクリプトを用意する。

実装予定のスクリプトは `scripts/riot_champion_query.py` とする。初版では次の2種類を提供する。

#### 味方組み合わせ

対象チャンピオンと同じチームの各チャンピオンを1対1の組み合わせとして集計する。

- `games`：対象チャンピオンと味方チャンピオンが同じ試合にいた件数
- `wins`、`losses`：対象チャンピオンのチームの勝敗
- `target_win_rate`：`wins / games`
- `pick_rate`：対象チャンピオンの出場試合のうち、味方チャンピオンもいた割合
- 対象チャンピオンのロール、味方チャンピオンのロール、観測帯、パッチ

「勝率の高い組み合わせ」は、`min-games` 以上の行を `target_win_rate` 降順、`games` 降順で並べる。これは味方シナジーの観測値であり、組み合わせの因果効果や推奨編成を意味しない。

#### 相手別の低勝率

対象チャンピオンと反対チームのチャンピオンを1対1の対面候補として集計する。

- 既定の `opponent-scope` は `same-role` とし、対象と相手が同じ正規化ロールの行だけを作る。
- `--opponent-scope all-enemy` を指定した場合は、反対チームの全チャンピオンを相手候補にする。
- `target_win_rate` は相手チャンピオン側の勝率ではなく、対象チャンピオンのチームが勝った割合とする。
- 「勝率の低い相手」は、`min-games` 以上の行を `target_win_rate` 昇順、`games` 降順で並べる。
- 同ロールが欠損する参加者は、`same-role` の分母から除外し、除外数を品質欄へ記録する。

相手別の低勝率は、対象チャンピオンにとって不利に見える観測結果を抽出するだけであり、「カウンター」と断定しない。サンプル数、パッチ、観測ランク帯、対象ロールを必ず併記する。

#### 専用CLI

```bash
python3 scripts/riot_champion_query.py \
  --input raw/sources/riot-ranked-matches \
  --champion カタリナ \
  --mode ally-pairs,opponents \
  --opponent-scope same-role \
  --min-games 15 \
  --top 20 \
  --bottom 20
```

| オプション | 既定値 | 説明 |
| --- | --- | --- |
| `--input PATH` | 必須 | 解析スクリプトと同じ入力形式。複数指定可 |
| `--champion VALUE` | 必須 | チャンピオンIDまたは日本語・英語表示名。曖昧な場合は候補を表示して終了 |
| `--mode` | `ally-pairs,opponents` | `ally-pairs`、`opponents` の一方または両方 |
| `--opponent-scope` | `same-role` | `same-role` または `all-enemy` |
| `--role` | 全ロール | 対象チャンピオンのロールを限定 |
| `--tier-mode` | `observed` | `all` または `observed` |
| `--tiers` | 全観測帯 | 観測ランク帯の限定 |
| `--patch` | 全パッチ | `gameVersion` の前方一致 |
| `--date-from` / `--date-to` | なし | 試合開始日の範囲 |
| `--min-games` | `15` | ランキングへ掲載する最小試合数 |
| `--top` | `20` | 味方組み合わせの上位件数 |
| `--bottom` | `20` | 相手別の低勝率件数 |
| `--format` | `markdown,csv,json` | 出力形式 |
| `--output` | `reports/riot-champion-query` | クエリ結果の出力先 |

チャンピオン名が複数のIDに解決される場合は自動選択せず、候補を出して入力エラーにする。対象チャンピオンの試合がない場合も、空のランキングを成功扱いにせず、入力条件と0件の理由をレポートする。

#### 専用クエリの出力

```text
reports/riot-champion-query/
└── run-YYYYMMDDTHHMMSSZ-<champion>/
    ├── query.json
    ├── report.md
    ├── ally-pairs.csv
    ├── opponents.csv
    └── quality.json
```

`ally-pairs.csv` と `opponents.csv` の共通列は次のとおりとする。

```text
scope,tier_mode,observed_tier,patch,target_champion,target_role,
patches,related_champion,related_role,games,wins,losses,target_win_rate,
pick_rate,pick_rate_denominator,min_games_applied
```

複数パッチをまとめた行では `patch` を `ALL` とし、実際に含まれるパッチを `patches` に列挙する。`opponents.csv` には `opponent_scope` と `same_role_match` を追加する。`query.json` には入力条件、対象チャンピオンの解決結果、ランキング順、上位・下位件数、最小ゲーム数、出力ファイルを記録する。

### 6.9 実試合のチャンピオン・アイテム相関

実試合の最終アイテムから、特定チャンピオン・正規化ロールでの所持時と非所持時を比較する。実装は `scripts/riot_champion_item_synergy.py` とする。

- 対象アイテムは通常スロット `item0`～`item5` とし、同じアイテムが複数スロットにあっても1参加者1所持として数える。`item6` は含めない。
- 既定では `Consumable`、`Trinket`、`Vision`、`Stealth`、`GoldPer` のData Dragonタグを持つアイテムを除外する。`--include-utility` で含められる。
- 集計単位は `champion_id × role × item_id` とし、`champion_games`、`item_games`、所持時勝率、非所持時勝率、所持時勝率から非所持時勝率を引いた `win_rate_lift_vs_without` を出力する。
- `item_games` は参加者単位の所持試合数であり、購入率、購入時刻、完成時刻、最初に買ったアイテムを意味しない。
- 既定の `tier-mode` は `all` とし、同じ試合が複数の観測帯に現れても全体値へ1回だけ含める。`observed` を指定した場合は観測帯別の行も生成する。
- `--min-games` の既定値は15とする。CSV/JSONのペア行をこの値で絞り、Markdownの上位表には小標本の極端な差を抑える別の表示閾値を適用できる。
- 複数パッチを合算すると、同じアイテムIDでも効果・名称・採用環境が変化している可能性がある。現行アイテム定義との比較では `--patch` と対応するData Dragonを指定する。

### 6.10 ステータス群・チャンピオン別ビルド分析

個別アイテムの勝率差だけではなく、同じData Dragon `item.json` の `stats` キーを持つアイテム群の採用有無と、完成アイテムの順不同組み合わせをチャンピオン・ロールごとに集計する。実装は `scripts/riot_champion_item_synergy.py` に統合し、同じ入力から再生成できる形で残す。

- ステータス群は `FlatCritChanceMod`（クリティカル率）、`FlatPhysicalDamageMod`（攻撃力）、`PercentAttackSpeedMod`（攻撃速度）など、Data Dragonの `stats` に非ゼロ値があるかで判定する。説明文の発動効果、固有効果、スキルとの相互作用をステータス群へ推測で追加しない。
- ステータス群とビルド中核に用いるアイテムは、指定したData Dragonの `maps["11"]` が `true` のものに限定する。過去データのアイテムIDが現行のArena等の同一IDへ再割り当てされた場合、その現行サモナーズリフト外定義を候補へ混入させないためである。
- 同一参加者が同じステータス群のアイテムを複数持っていても、該当参加者を1回だけ数える。したがって「クリティカル率群」は、クリティカル率を持つアイテムを1つ以上最終所持したかを表し、クリティカル率の合計値や購入順ではない。
- ビルド中核は、通常スロットのうち開始アイテム・素材・utilityを除いた完成アイテムから、順不同の2個・3個組み合わせを作る。最小ゲーム数以上の組み合わせを実測候補として出力する。
- チャンピオン別Markdownは、ロールごとに実測上の個別アイテム、ステータス群、ビルド中核を「推奨候補」として分けて示す。ただし、推奨候補は最終所持状態の観測相関であり、因果効果や購入順を意味しない。
- 十分な実測件数がない組み合わせについては、アイテム同士が共有する `stats` 群を理由に理論仮説候補を別表へ出す。これは機械的な仮説生成であり、ゲーム内で強いことを保証する推奨ではない。
- 既定のステータス群を限定する場合は `--status-groups critical_chance` のように指定し、ビルド中核のサイズは `--build-sizes 2,3` で選択する。

この差は、試合時間、勝敗後まで生存したこと、プレイヤー、対面、構成、パッチ、アイテム選択の逆因果などを調整しない観測値である。実測値の順位を「相性がよい」「弱い」「推奨ビルド」と読み替えない。

#### 専用CLI

```bash
python3 scripts/riot_champion_item_synergy.py \
  --input raw/sources/riot-ranked-matches \
  --output reports/riot-champion-item-synergy \
  --tier-mode all \
  --min-games 15
```

| オプション | 既定値 | 説明 |
| --- | --- | --- |
| `--input PATH` | 必須 | 解析スクリプトと同じJSONL、キャッシュ、ディレクトリ入力 |
| `--output PATH` | `reports/riot-champion-item-synergy` | `raw/` 外の出力先 |
| `--tier-mode` | `all` | 全体の重複除去、または `observed` の観測帯別集計 |
| `--patch` | 全パッチ | `gameVersion` の前方一致。現行アイテム定義と揃える場合に指定 |
| `--roles` / `--champions` | 全件 | ロールまたはチャンピオンの限定 |
| `--status-groups` | 全群 | `critical_chance` などData Dragon `stats` に基づく群の限定 |
| `--build-sizes` | `2,3` | 完成アイテム中核のサイズ。2または3をカンマ区切りで指定 |
| `--min-games` | `15` | CSV/JSONへ掲載するアイテム所持試合数の下限 |
| `--report-min-games` | `30` | Markdown上位表に載せる所持・非所持双方の試合数の下限 |
| `--include-utility` | 無効 | 消耗品、視界、トリンケット等を含める |
| `--format` | `markdown,csv,json` | 出力形式 |
| `--dry-run` | 無効 | 入力・重複・条件だけ検証して出力しない |

#### 専用出力

```text
reports/riot-champion-item-synergy/
└── run-YYYYMMDDTHHMMSSZ/
    ├── manifest.json
    ├── report.md
    ├── quality.json
    ├── analysis.json
    ├── champion-item-synergy.csv
    ├── champion-status-synergy.csv
    ├── champion-build-synergy.csv
    ├── theoretical-build-candidates.csv
    └── champions/
        ├── index.json
        └── champion-<champion_id>.md
```

CSV/JSONには、チャンピオン・ロール・アイテム、ステータス群、ビルド中核の識別子と表示名、該当・非該当の勝敗分子分母、採用率、勝率差、パッチ、観測帯、最小ゲーム数を含める。個人識別情報は含めない。`analysis.json` には `results`（個別アイテム）、`status_group_results`、`build_results`、`theoretical_build_results` を分けて格納する。

`champions/champion-<champion_id>.md` はチャンピオンごとに1ファイルとし、ロール別に「実測からの推奨候補」と「統計が不足する理論仮説」を分離する。理論仮説には未観測か最小ゲーム数未満か、共有するData Dragon `stats` 群を記載する。

### 6.11 チャンピオンentityへの短い分析ブロック同期

チャンピオン情報の入口は `wiki/entities/champions/` とし、詳細な表と全候補は `reports/riot-champion-item-synergy/` に保持する。解析とWiki更新を分離し、選択した実行結果の `analysis.json` を `scripts/riot_champion_build_wiki_sync.py` へ明示的に渡した場合だけentityを更新する。

- 各entityには `<!-- champion-build-analysis:start -->` と `<!-- champion-build-analysis:end -->` で囲んだ生成ブロックを1つ置く。再実行時はこの範囲だけを置換し、原典由来の本文や既存の生成ブロックを変更しない。
- 生成ブロックは既定で、30試合以上ある上位2ロール、各ロールの実測ビルド候補2件、正の差を持つステータス群2件、理論仮説2件までに抑える。
- 実測候補は該当・非該当の双方が `analysis.json` の `report_min_games`（既定30）以上で、勝率差が正のものに限定する。これは表示基準であり統計的有意性ではない。
- 理論仮説は共通するData Dragon `stats` と、生成ブロック外のチャンピオンページにある原典由来の語彙を使って表示順を決める。スキルとの相互作用を実証したものではない。
- ブロックから同一実行の `champions/champion-<champion_id>.md` へ直接リンクし、詳細表、負の差、小標本、候補全体はレポート側で確認できるようにする。
- 生成ブロック内のビルド名・理論仮説に含まれるアイテムは、既存の `wiki/entities/items/item-<item_id>.md` の `title` を表示名としてWikilink化する。アイテム名だけでなく分析結果のアイテムIDでリンク先を確定し、同名のモード別アイテムを取り違えない。
- entityの `sources` には専用の原典要約を追加し、`updated` を解析スナップショットのAsia/Tokyo生成日へ更新する。詳細レポート自体は原典ではなく、収集済み試合データから生成した派生物として扱う。
- 通常の解析実行ではentityを暗黙に変更しない。`--dry-run` で対象・差分・詳細レポート欠落を確認し、`--write` で同期し、`--check` で再現性を検証する。
- アイテムリンク同期は新しい試合レポートを生成しない。既存の `analysis.json` と既存のアイテムentityを入力にして、生成ブロックの表示だけを置換する。対応するアイテムentityがない場合は書き込まずエラーにする。

```bash
python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --dry-run

python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --write

python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --check
```

### 6.12 チャンピオンentityへのコンボ・カウンターピック同期

実測の味方コンボと同ロール対面候補は、`scripts/riot_champion_matchup_wiki_sync.py` でチャンピオンentityへ短く同期する。詳細な候補全体は、選択した同一実行の `reports/riot-champion-matchups/` に残す。

- entityごとに出場数の多い最大2ロールを対象とする。
- 各ロールについて、味方コンボは対象側勝率が高い候補を最大3件、カウンターピックは対象側勝率が低い候補を最大3件掲載する。候補が3件に満たない場合は、最小ゲーム数を満たす実測候補だけを掲載し、判断保留を明記する。
- 小標本の極端値を抑えるため、n≥30の候補が存在する場合はその集合から選び、味方コンボは95% Wilson区間の下限降順、カウンターピックは上限昇順を優先する。n=15〜29はサンプル不足と表示する。
- 勝率は対象チャンピオン側の記述統計であり、コンボの因果効果、確定的なカウンター、推奨編成を意味しない。対面は最終スコアから推定した同ロールであり、実際のレーン対面を保証しない。
- 既存の `analysis.json` を `--analysis` で渡す場合はrawを再集計せず、既存の候補行からentityブロックだけを更新する。`--dry-run` で掲載件数を確認し、`--write` で同期する。通常の `--input` 実行は新しい詳細レポートも生成する。

```bash
python3 scripts/riot_champion_matchup_wiki_sync.py \
  --analysis reports/riot-champion-matchups/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --selection-limit 3 \
  --dry-run

python3 scripts/riot_champion_matchup_wiki_sync.py \
  --analysis reports/riot-champion-matchups/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --selection-limit 3 \
  --write
```

### 6.13 最新レポート連動Lint

`scripts/lint.py` は、各レポート系列の `manifest.json`、宣言済み `outputs`、品質情報、同期に必要な機械可読結果がそろった実行だけを完了済みとみなし、`manifest.json` の `generated_at` が最も新しい実行を選択する。ファイル更新時刻や実行ディレクトリ名は選択基準にしない。

- 試合時間帯別の `champion-duration-winrate.json` は `scripts/riot_champion_duration_wiki_sync.py` で `power-spike-match` ブロックへ同期する。
- ビルド、コンボ・カウンターピック、ルーン、観測ランク帯候補は、それぞれ対応する既存の `*_wiki_sync.py` でentityへ同期する。
- 通常の `python3 scripts/lint.py` は、レポート同期の `--dry-run`、静的生成物の更新、レポート同期の `--write`、静的生成物とレポート同期の `--check` を順に実行する。レポートやrawの再生成・変更は行わない。
- `python3 scripts/lint.py --check-only` は書き込みを行わず、最新レポートから再現されるentity内容を検証する。
- 複数系列の生成日が異なっても、entityの `updated` を古いレポートの日付へ巻き戻さない。候補表示は記述統計であり、推奨や因果効果を自動的に確定しない。

詳細な選択条件、未完了実行の扱い、実行順序は [Riotレポート連動Lint仕様書](riot-lint-report-sync-spec.md) に記載する。

## 7. 出力仕様

1回の実行ごとに、時刻付きのディレクトリを作成する。

```text
reports/riot-ranked-match-analysis/
└── run-YYYYMMDDTHHMMSSZ/
    ├── manifest.json
    ├── report.md
    ├── quality.json
    ├── analysis.json
    ├── champion-summary.csv
    ├── item-summary.csv
    ├── rune-summary.csv
    ├── champion-rune-summary.csv
    ├── champion-rune-set-summary.csv
    ├── summoner-spell-summary.csv
    ├── performance-summary.csv
    ├── role-gold.csv
    ├── duration-summary.csv
    └── matchup-summary.csv       # --include-matchups 時のみ
```

### 7.1 `manifest.json`

次の情報を保存する。

- 解析スクリプト名、仕様バージョン、実行日時
- 入力パス、入力ファイル数、可能ならファイルサイズとSHA-256
- Data Dragonアーカイブのパスとバージョン
- CLI条件（キュー、期間、パッチ、ロール、観測帯、tier mode、最小ゲーム数）
- 入力件数、ユニーク試合数、集計対象数、除外数
- 出力ファイル一覧

入力レコードの内容、APIキー、PUUID、サモナー名はマニフェストに複製しない。

### 7.2 `quality.json`

除外理由ごとの件数と代表的な非個人識別キーを記録する。

- `invalid_json`
- `missing_match_id`
- `missing_info`
- `queue_mismatch`
- `duplicate_match`
- `conflicting_payload`
- `incomplete_participants`
- `unknown_champion`
- `unknown_item`
- `unknown_rune`
- `unknown_summoner_spell`
- `missing_timestamp`

代表例に含めるIDは、必要な場合も `match_id` までとし、参加者IDやプレイヤー名は含めない。

### 7.3 Markdownレポート

`report.md` には次の順で記載する。

1. 解析条件と入力範囲
2. データ品質と除外件数
3. 試合時間の要約
4. ロール別ゴールド獲得率
5. 観測ランク帯・パッチ別の試合数
6. チャンピオンの抽出結果
7. ルーン、サモナースペルの抽出結果
8. 必要な場合の味方ペア・対面結果
9. 解釈上の注意と未解決事項

人間向けMarkdownレポートでは、最終アイテムは勝敗後の所持状態を含み、単純な所持数順が解釈しにくいため、アイテム上位表を掲載しない。アイテムの集計結果は `item-summary.csv` と `analysis.json` に保持する。

チャンピオン・アイテム相関レポートは別出力とし、所持時勝率、非所持時勝率、差、所持試合数を表示する。これはアイテム上位表の代替となる推奨表ではなく、原典由来の相性候補タグを実試合で点検するための探索表である。

ルーンは `rune_kind` とIDを表示する。`perks.statPerks` のステータスシャードは `runesReforged.json` に表示名がないため、`UNKNOWN(<ID>)` となる場合がある。これは試合レコードの欠損とは区別する。

チャンピオン別ルーン選択は、観測数の多いチャンピオン・ロールから代表例をMarkdownへ掲載し、全行を `champion-rune-summary.csv` と `analysis.json` へ保存する。代表例は探索の入口であり、選択率の高いルーンを推奨として扱わない。

チャンピオン別ルーンセットは、主系・キーストーン・主系3枠・副系2枠・3シャードの完全一致を対象に、各チャンピオンの観測数最多ロールから上位3件をMarkdownへ掲載する。詳細な全行は `champion-rune-set-summary.csv` と `analysis.json` に保存し、選択数、選択率、選択時勝率、各ID・表示名を併記する。これは実測された選択傾向の要約であり、最適セットや推奨を意味しない。

チャンピオン、サモナースペル、ルーンのMarkdown表は、全パッチの `overall`・`role=ALL` 行をID単位で合算し、同じ表示名がパッチごとに重複しないようにする。チャンピオン上位では同じチャンピオンを1行にまとめる。

試合時間は全パッチ合算の `patch=ALL` 行と、試合数の多いパッチ別行を分けて示す。中央値は典型的な試合時間、P10〜P90は中央80%の範囲として説明し、パワースパイクや因果効果とは解釈しない。

味方・対面ペアは、味方になると強い組み合わせ（順不同のペアをチーム勝率降順）と、カウンターピック候補（同ロールで対象側勝率昇順）の2表に分離する。いずれも記述統計であり、推奨やカウンター関係の断定ではない。

ランキング表は、原則として `games` 降順、`win_rate` 降順、表示名昇順で安定ソートする。最小ゲーム数で除外した候補は、可能なら品質欄に件数だけ示す。

### 7.4 観測ランク帯別比較（`riot_ranked_tier_analyzer.py`）

ランク帯ごとの特徴を比較する場合は、`ranked-solo-5x5/**/matches.jsonl` を入力し、`observed` 固定で次を出力する。

```bash
python3 scripts/riot_ranked_tier_analyzer.py \
  --input raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5 \
  --output reports/riot-ranked-tier-analysis \
  --queue-id 420 \
  --min-games 15 \
  --format markdown,csv,json
```

`observed_tier` ごとに、試合時間（平均、中央値、P10、P90）、平均総キル、first blood・first tower・投了関連率、最終スコア由来のGPM・DPM・CS/分・視界・KDA、チャンピオン分布、ロール別最終ゴールド比率を集計する。加えて、観測帯別のチャンピオン選択・勝率、キーストーン、順不同かつ重複表示を排除したサモナースペル構成、高低勝率の探索候補を出力する。

出力先は `reports/riot-ranked-tier-analysis/run-YYYYMMDDTHHMMSSZ/` とし、`tier-summary.csv`、`role-summary.csv`、`champion-tier.csv`、`champion-extremes.csv`、`keystone-tier.csv`、`spell-pair-tier.csv`、`analysis.json`、`quality.json`、`report.md` を生成する。`analysis.json` には全観測帯の上位選択の共通部分も保存する。

各帯の試合数をそろえて比較しても、観測帯は試合時点の10人全員のランクを表さず、帯別試合は同じ試合の重複観測を含み得る。したがって、レポートは「観測経路から得た試合の特徴」として記述し、ランク差、技能差、勝率差の因果効果や推奨を断定しない。高低候補の既定 `min-games=15` は探索上の閾値であり、有意性検定や信頼区間を意味しない。

## 8. データ品質と解釈上の限界

- 収集器の `observed_tier` は収集時点のプレイヤー所属帯であり、試合時点の全参加者のランクではない。
- 同じ試合が複数帯に現れるため、観測帯別の表を合算して全体値を求めてはならない。全体値には `tier-mode=all` を使う。
- 収集器はランク帯に所属するプレイヤーの履歴から試合を発見するため、ランク帯の全試合を無作為抽出した標本ではない。
- 同じ試合の重複参加者、プレイヤーサンプル、履歴ページ上限により、試合の出現確率は均一ではない。
- Match-v5 の通常レスポンスだけでは、15分時点のゴールド差、購入時刻、スキル使用順、実際のレーン滞在などを復元できない。
- 最終 `goldEarned / timePlayed` のロール別比較は、試合終了までの時間と勝敗後の状態を含むため、時間ごとのゴールド獲得速度やロール固有の収入源の因果効果を示さない。
- 最終アイテムは生存者バイアスと勝敗後の購入状態を含むため、アイテム所持率からアイテムの勝率向上を直接結論付けない。
- チャンピオン・アイテムの所持時／非所持時比較も、同じチャンピオン・ロール内の未調整比較である。差がプラスでも因果的なシナジーを示さず、差がマイナスでもアイテム自体の弱さを示さない。
- 複数パッチを合算した相関は、現在のData Dragonのアイテム名・タグで過去のアイテムIDを表示するため、アイテム定義の変更をまたいだ厳密な比較には使わない。パッチを限定し、対応する原典を揃える必要がある。
- `gameVersion`、マップ、キュー、取得期間が異なる集計は混ぜず、パッチ・期間をレポートに必ず表示する。
- ゲーム内の欠損値を0とみなさない。項目ごとに有効分母を持つ。
- `min-games` は表示上の安定化であり、統計的有意性の検定や信頼区間を意味しない。

## 9. 非対応範囲（初版）

- Riot APIへの追加取得、再収集、レート制限処理
- 個人別の成績表、プレイヤーランキング、PUUIDの出力
- Timeline APIを使った時系列イベント解析
- 購入順、購入時刻、ビルド完成時刻の推定
- 勝率からの因果推論、最適ビルドやカウンターの自動推薦（専用クエリは観測値の抽出に限る）
- 実試合の所持時／非所持時差からの自動的な相性タグ書き換え、最適ビルド推薦、因果推論
- 実測候補またはステータス群だけから、ゲーム内での最適ビルドを確定すること
- 機械学習モデルの学習・予測
- 解析実行に伴うWikiページの暗黙更新。`scripts/lint.py` は明示的な保守コマンドとして、既存の完了済みレポートから生成ブロックを同期する

## 10. 受け入れ条件

- `matches.jsonl` と `.cache/matches/*.json` を読み取れる。
- 入力を変更せず、`raw/` 配下へ出力しない。
- デフォルトで queue ID `420` 以外を除外できる。
- 同じ `match_id` を同一分析集合で二重計上しない。
- `all` と `observed` のtier modeで、重複観測の扱いが仕様どおり異なる。
- 参加者、チーム、ID、時刻の欠損を検出し、品質レポートへ記録できる。
- チャンピオン、アイテム、ルーン、サモナースペルの表示名をローカルデータから解決できる。
- 勝率、ピック率、バン率、KDA、CS/分、ゴールド/分などの分子・分母を出力できる。
- チャンピオン・ロール別のルーン選択について、同一分母の選択率、選択時勝率、チャンピオン全体勝率、ルーン系統、分子・分母をCSV/JSON/Markdownへ出力できる。
- チャンピオン・ロール別の完全ルーンセットについて、主系・副系・キーストーン・各選択枠・3シャードのID、選択数、選択率、選択時勝率をCSV/JSONへ出力し、観測数最多ロールの上位3件をentityへ同期できる。
- `riot_champion_rune_wiki_sync.py` が `--dry-run`、`--write`、`--check` を提供し、各チャンピオンentityへ完全ルーンセット上位3件を同一実行の解析レポートへの導線付きで同期できる。
- `riot_champion_query.py --champion <name>` で、味方組み合わせの高勝率順と相手別の対象チャンピオン低勝率順を取得できる。
- `riot_champion_matchup_wiki_sync.py --analysis <path> --selection-limit 3 --write` で、既存の候補分析から各チャンピオン・最大2ロールに高勝率コンボ3件と低勝率カウンターピック3件を同期できる。
- 相手別クエリは既定で同ロールに限定し、`all-enemy` へ切り替えられる。
- 味方組み合わせと相手別の表に、最小ゲーム数、対象チャンピオンの勝敗分子・分母、観測帯、パッチを含める。
- 不完全試合を既定で率の分母から除外し、`--include-incomplete` で挙動を変更できる。
- 出力に `puuid`、`summonerId`、`summonerName`、Riot IDを含めない。
- 同じ入力・同じ条件で、時刻と実行ディレクトリ名を除く内容が再現する。
- `--help`、`--dry-run`、Python構文チェックがAPIキーなしで成功する。
- `riot_champion_item_synergy.py` が通常スロットの重複アイテムを参加者単位で1回にまとめ、最小ゲーム数15、所持時・非所持時の勝率と差をCSV/JSON/Markdownへ出力できる。
- チャンピオン・アイテム相関の既定全体集計が同一試合を観測帯の重複で二重計上せず、`--patch` によるパッチ限定と `--include-utility` による補助アイテム包含を検証できる。
- `riot_champion_item_synergy.py` がData Dragon `stats` によるステータス群（クリティカル率を含む）を参加者単位で重複なく集計し、個別アイテムと別CSV/JSONへ出力できる。
- 同スクリプトが完成アイテムの順不同2個・3個中核をチャンピオン・ロールごとに集計し、実測候補と、共通ステータスから導いた実測不足の理論仮説を分離したチャンピオン別Markdownを生成できる。
- ステータス群とビルド中核の候補へ、指定Data Dragonで `maps["11"]` が真ではないアイテムを含めない。
- `riot_champion_build_wiki_sync.py` が `--dry-run`、`--write`、`--check` を提供し、各チャンピオンentityへ短い生成ブロックを1つだけ同期して同一実行の詳細レポートへリンクできる。
- entity同期が既存のアイテムentityをIDで解決し、ビルド名・理論仮説の全アイテム名を対応するアイテムページへのWikilinkとして出力できる。アイテムentityが不足する場合は書き込まない。
- entity同期を再実行しても生成ブロック外の本文を変更せず、専用原典要約を `sources` に重複なく追加できる。
- `riot_ranked_tier_analyzer.py` が `ranked-solo-5x5/**/matches.jsonl` を観測帯別に集計し、各帯の試合時間、最終スコア、ロール、チャンピオン、キーストーン、順不同スペル構成、高低候補、全帯共通性をCSV/JSON/Markdownへ出力できる。
- 観測帯別レポートが、入力件数、ユニーク試合数、帯をまたぐ重複試合数、パッチ数、取得日範囲、観測ランク帯の解釈上の注意を表示できる。
- `riot_champion_tier_wiki_sync.py` が、選択した観測帯分析 `analysis.json` から各帯のピック数上位5件、高勝率候補5件、低勝率候補5件を `champion_key` で対応するentityへ同期できる。同期前後に `--dry-run`、`--write`、`--check` を実行でき、同一分類内のチャンピオン重複を表示しない。
- `riot_champion_duration_wiki_sync.py` が、選択した時間帯別勝率 `champion-duration-winrate.json` から全チャンピオンの試合時間帯別観測ブロックを同期でき、`--dry-run`、`--write`、`--check` を提供する。
- `lint.py` がmanifestの完了条件と `generated_at` に基づき最新レポートを系列ごとに選択し、試合時間帯、ビルド、コンボ・カウンターピック、ルーン、観測ランク帯候補を同期してから静的Lintと再現性チェックを実行できる。`--check-only` では書き込まない。

## 11. 確認済みの仕様

以下を実装の前提とする。

1. 初版の主な出力を、チャンピオン・アイテム・ルーン・スペルの集計までとし、味方ペア・対面はオプション生成とする。
2. `observed` を既定のtier modeとし、観測ランク帯を実際の試合時ランクと解釈しない注意書きをレポートへ入れる。
3. `--min-games 15` を初期値とする。
4. `.cache/matches/*.json` はランク帯情報がない補助入力として許可し、ランク帯別分析には `matches.jsonl` を優先する。
5. 個人識別情報を一切出力しない。
6. 出力先を `reports/riot-ranked-match-analysis/` とする。
7. 粒度の細かいクエリを `scripts/riot_champion_query.py` として分離し、味方組み合わせは全味方、相手は既定で同ロールとする。
8. 「勝率の低い相手」は、相手の勝率ではなく対象チャンピオン側の `target_win_rate` が低い順とする。
9. `--min-games 15`、味方上位20件、相手下位20件を専用クエリの既定値とする。
10. チャンピオン・アイテム相関は `scripts/riot_champion_item_synergy.py` に分離し、通常スロット、既定のutility除外、所持時／非所持時差、パッチ限定、実試合結果の解釈上の限界を記録する。
11. 個別アイテムに加えて、Data Dragon `stats` の同一ステータス群と完成アイテムの順不同中核をチャンピオン別に分析する。実測候補と理論仮説を別表・別節にし、仮説を最適ビルドとして断定しない。
12. チャンピオン情報の入口はentityとし、そこには短い生成ブロックだけを置く。詳細な候補と表は時刻付きの `reports/` に残し、選択した解析結果から明示的に同期する。
13. チャンピオン別ルーン選択は `champion_id × role` の参加者を分母にし、パッチ重複を除いて全パッチを合算する。選択率と勝率は記述統計として扱う。
14. 完全ルーンセットは主系・副系・キーストーン・主系3枠・副系2枠・3シャードの順序付きIDをキーに集計し、観測数最多ロールの上位3件をentityへ掲載する。選択時勝率は記述統計として扱い、推奨と解釈しない。
15. 観測ランク帯の比較は `scripts/riot_ranked_tier_analyzer.py` に分離し、各帯の特徴と全帯共通性を同一実行のレポートへ保存する。`observed_tier` を試合時点の全参加者ランクと解釈せず、帯をまたぐ重複とパッチ・取得期間の差を明示する。
16. 観測帯別のチャンピオン候補は `scripts/riot_champion_tier_wiki_sync.py` で、選択した `analysis.json` の各帯上位5件・高勝率5件・低勝率5件を、候補が登場するchampion entityへ短い生成ブロックとして同期する。最小ゲーム数は分析結果の `filters.min_games`（今回15）を引き継ぎ、候補は推奨ではなく探索的な記述統計として扱う。

この仕様に基づき、`scripts/riot_ranked_match_analyzer.py`、`scripts/riot_ranked_tier_analyzer.py`、`scripts/riot_champion_query.py`、`scripts/riot_champion_item_synergy.py`、`scripts/riot_champion_build_wiki_sync.py`、`scripts/riot_champion_matchup_wiki_sync.py`、`scripts/riot_champion_rune_wiki_sync.py`、`scripts/riot_champion_tier_wiki_sync.py`、`scripts/riot_champion_duration_wiki_sync.py`、`scripts/lint.py` を実装する。

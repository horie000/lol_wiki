# Riot API ランク戦試合結果解析スクリプト仕様書

- 仕様バージョン：0.3（承認済み）
- 作成日：2026-09-15
- 対象ゲーム：League of Legends
- 実装予定：`scripts/riot_ranked_match_analyzer.py`
- 関連仕様：[Riot API ランク戦データ収集仕様書](riot-ranked-match-collector-spec.md)

## 1. 目的

取得済みの Match-v5 試合結果を、チャンピオン、ロール、アイテム、ルーン、サモナースペル、チーム構成、試合時間などの単位で集計し、後続の検証や Wiki への分析結果の取り込みを助ける。

このスクリプトは統計量の算出と再現可能なレポート生成を担当する。勝率から因果関係、最適ビルド、チャンピオン間の絶対的な相性を断定しない。分析結果に対する解釈や Wiki ページの作成は別工程とする。

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

### 6.6 チーム構成・対面集計

`--include-matchups` 指定時だけ生成する。最小ゲーム数未満の行は通常表から除外する。

- 味方シナジー：同一チーム内のチャンピオンの順序なしペア
- ロール別対面：反対チームで同じ正規化ロールに割り当てられたチャンピオンの有向ペア
- チーム構成：5体のチャンピオン集合と勝敗
- 各行：`games`, `wins`, `win_rate`, `sample_size`, `observed_tiers`, `patches`

対面は `teamPosition` 等の最終スコアから推定した組み合わせであり、レーンで実際に対面したことや、チャンピオン固有のカウンター関係を保証しない。味方ペアや対面の率は、プレイヤー、構成、パッチ、試合選択の交絡を含む記述統計に限定する。

### 6.7 チャンピオン指定クエリ

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
related_champion,related_role,games,wins,losses,target_win_rate,
pick_rate,pick_rate_denominator,min_games_applied
```

`opponents.csv` には `opponent_scope` と `same_role_match` を追加する。`query.json` には入力条件、対象チャンピオンの解決結果、ランキング順、上位・下位件数、最小ゲーム数、出力ファイルを記録する。

## 7. 出力仕様

1回の実行ごとに、時刻付きのディレクトリを作成する。

```text
reports/riot-ranked-match-analysis/
└── run-YYYYMMDDTHHMMSSZ/
    ├── manifest.json
    ├── report.md
    ├── quality.json
    ├── champion-summary.csv
    ├── item-summary.csv
    ├── rune-summary.csv
    ├── summoner-spell-summary.csv
    ├── performance-summary.csv
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
4. 観測ランク帯・パッチ別の試合数
5. チャンピオンの抽出結果
6. アイテム、ルーン、スペルの抽出結果
7. 必要な場合の味方ペア・対面結果
8. 解釈上の注意と未解決事項

ランキング表は、原則として `games` 降順、`win_rate` 降順、表示名昇順で安定ソートする。最小ゲーム数で除外した候補は、可能なら品質欄に件数だけ示す。

## 8. データ品質と解釈上の限界

- 収集器の `observed_tier` は収集時点のプレイヤー所属帯であり、試合時点の全参加者のランクではない。
- 同じ試合が複数帯に現れるため、観測帯別の表を合算して全体値を求めてはならない。全体値には `tier-mode=all` を使う。
- 収集器はランク帯に所属するプレイヤーの履歴から試合を発見するため、ランク帯の全試合を無作為抽出した標本ではない。
- 同じ試合の重複参加者、プレイヤーサンプル、履歴ページ上限により、試合の出現確率は均一ではない。
- Match-v5 の通常レスポンスだけでは、15分時点のゴールド差、購入時刻、スキル使用順、実際のレーン滞在などを復元できない。
- 最終アイテムは生存者バイアスと勝敗後の購入状態を含むため、アイテム所持率からアイテムの勝率向上を直接結論付けない。
- `gameVersion`、マップ、キュー、取得期間が異なる集計は混ぜず、パッチ・期間をレポートに必ず表示する。
- ゲーム内の欠損値を0とみなさない。項目ごとに有効分母を持つ。
- `min-games` は表示上の安定化であり、統計的有意性の検定や信頼区間を意味しない。

## 9. 非対応範囲（初版）

- Riot APIへの追加取得、再収集、レート制限処理
- 個人別の成績表、プレイヤーランキング、PUUIDの出力
- Timeline APIを使った時系列イベント解析
- 購入順、購入時刻、ビルド完成時刻の推定
- 勝率からの因果推論、最適ビルドやカウンターの自動推薦（専用クエリは観測値の抽出に限る）
- 機械学習モデルの学習・予測
- Wikiページの自動生成・自動更新

## 10. 受け入れ条件

- `matches.jsonl` と `.cache/matches/*.json` を読み取れる。
- 入力を変更せず、`raw/` 配下へ出力しない。
- デフォルトで queue ID `420` 以外を除外できる。
- 同じ `match_id` を同一分析集合で二重計上しない。
- `all` と `observed` のtier modeで、重複観測の扱いが仕様どおり異なる。
- 参加者、チーム、ID、時刻の欠損を検出し、品質レポートへ記録できる。
- チャンピオン、アイテム、ルーン、サモナースペルの表示名をローカルデータから解決できる。
- 勝率、ピック率、バン率、KDA、CS/分、ゴールド/分などの分子・分母を出力できる。
- `riot_champion_query.py --champion <name>` で、味方組み合わせの高勝率順と相手別の対象チャンピオン低勝率順を取得できる。
- 相手別クエリは既定で同ロールに限定し、`all-enemy` へ切り替えられる。
- 味方組み合わせと相手別の表に、最小ゲーム数、対象チャンピオンの勝敗分子・分母、観測帯、パッチを含める。
- 不完全試合を既定で率の分母から除外し、`--include-incomplete` で挙動を変更できる。
- 出力に `puuid`、`summonerId`、`summonerName`、Riot IDを含めない。
- 同じ入力・同じ条件で、時刻と実行ディレクトリ名を除く内容が再現する。
- `--help`、`--dry-run`、Python構文チェックがAPIキーなしで成功する。

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

この仕様に基づき、`scripts/riot_ranked_match_analyzer.py` と `scripts/riot_champion_query.py` を実装する。

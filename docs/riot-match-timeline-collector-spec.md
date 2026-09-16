# Riot API Match-v5 Timelineデータ取得仕様書

- 仕様バージョン：1.0
- 作成日：2026-09-16
- 改訂日：2026-09-16
- 対象ゲーム：League of Legends
- 実装：`scripts/riot_match_timeline_collector.py`
- 関連仕様：[Riot API ランク戦データ収集仕様書](riot-ranked-match-collector-spec.md)

## 1. 目的

既に取得済みのMatch-v5試合詳細から試合IDを読み取り、Riot APIのTimelineエンドポイントを取得する。Timelineは、フレーム単位の参加者状態とイベントを後続の時間変化分析へ渡すための入力とする。

本スクリプトは試合IDの発見、勝率集計、パワースパイクの推定、購入順の解釈を行わない。試合詳細を取得する既存の`riot_ranked_match_collector.py`と役割を分け、入力済みの試合へTimelineを追加取得する。

## 2. 基本方針

- Riot APIキーは`RIOT_API_KEY`環境変数からのみ読み込み、引数・ログ・マニフェストへ保存しない。
- 入力は既存のMatch-v5 JSONLまたはMatch-v5キャッシュとし、Timeline取得のためにLeague-v4やMatch-v5の試合履歴APIを再度呼び出さない。
- 同じ試合IDは入力ファイルやランク帯をまたいで1件へ統合する。
- 既定ではキューID `420`（Ranked Solo/Duo）のみを対象とする。`--queue-id 0`でキューを限定しない。
- 試合開始時刻の降順で対象を選び、`--limit`でAPI呼び出し数を上限設定する。既定値は100件とし、大量取得を暗黙に開始しない。
- 出力は`reports/`配下に置き、`raw/`へは書き込まない。入力のrawデータは変更しない。
- 取得済みTimelineは出力ルートの`.cache/timelines/`へ保存し、再実行時は同じ試合を再取得しない。`--refresh`で明示的に再取得する。
- APIレスポンスの`puuid`、`summonerId`、`summonerName`、`riotIdGameName`、`riotIdTagline`を再帰的に除去して、分析用出力に個人識別情報を残さない。

## 3. API仕様

| 用途 | HTTPパス | ルート |
| --- | --- | --- |
| 試合Timeline | `/lol/match/v5/matches/{matchId}/timeline` | `americas`、`asia`、`europe`、`sea` |

地域ルートは`--regional-route auto`の場合、`--platform`から既存収集器と同じ規則で解決する。既定の`jp1`は`asia`へ対応する。

Timelineレスポンスは`metadata`と`info.frames`を持つJSONオブジェクトとして検証する。フレームがない、またはJSONオブジェクトでないレスポンスは取得失敗として記録する。

## 4. 入力仕様

### 4.1 Match-v5 JSONL

`--input`には次の形式のファイルまたはディレクトリを指定する。ディレクトリは配下の`matches.jsonl`を再帰的に探索する。

```text
raw/sources/riot-ranked-matches/**/matches.jsonl
```

各行の`match_id`を優先し、ない場合は`match.metadata.matchId`を試合IDとする。`game_start_timestamp`がない場合は`match.info.gameStartTimestamp`、次に`gameCreation`を使う。`queue_id`、パッチ、観測ランク帯、観測ディビジョンはTimelineレコードの周辺メタデータへ引き継ぐ。

### 4.2 Match-v5キャッシュ

`--include-cache`を指定した場合だけ、入力ディレクトリ配下の次のキャッシュも読む。

```text
**/.cache/matches/*.json
```

キャッシュには観測ランク帯がないため、該当するメタデータは空または`UNKNOWN`相当となる。通常はランク帯情報を持つ`matches.jsonl`を優先する。

### 4.3 対象選択

次の条件をすべて満たす試合を選ぶ。

1. 試合IDが解決できる。
2. `--queue-id`が0、または入力の`match.info.queueId`と一致する。
3. `--patch`を指定した場合、`gameVersion`のパッチ接頭辞が一致する。
4. `--date-from`、`--date-to`を指定した場合、UTCの試合開始日が範囲内である。
5. `--match-id`を指定した場合、そのIDに一致する。

同じ試合IDが複数行に登場したときは1件へ統合し、入力ファイル、観測ランク帯、観測ディビジョンを集合として保持する。選択順は`gameStartTimestamp`降順、同時刻は試合ID降順とする。

## 5. CLI仕様

```bash
python3 scripts/riot_match_timeline_collector.py \
  --input raw/sources/riot-ranked-matches \
  --output reports/riot-match-timeline \
  --queue-id 420 \
  --limit 100
```

| オプション | 既定値 | 説明 |
| --- | --- | --- |
| `--input PATH` | `raw/sources/riot-ranked-matches` | Match-v5 JSONL、キャッシュ、または探索対象ディレクトリ |
| `--output PATH` | `reports/riot-match-timeline` | 実行結果とTimelineキャッシュのルート。`raw/`配下は拒否 |
| `--platform` | `jp1` | 地域ルート自動解決に使うプラットフォーム |
| `--regional-route` | `auto` | `americas`、`asia`、`europe`、`sea`、`auto` |
| `--queue-id` | `420` | 対象キュー。`0`は限定なし |
| `--patch` | なし | `16.18`などのパッチ接頭辞 |
| `--date-from` / `--date-to` | なし | UTC試合開始日の範囲（`YYYY-MM-DD`） |
| `--match-id` | なし | 対象試合ID。複数指定可 |
| `--limit` | `100` | 最大取得件数。`0`は全件 |
| `--include-cache` | 無効 | Match-v5キャッシュを入力に含める |
| `--refresh` | 無効 | Timelineキャッシュを無視して再取得 |
| `--run-id` | UTC時刻 | 出力ディレクトリ名を固定する場合に指定 |
| `--overwrite` | 無効 | 同名の実行ディレクトリを上書き |
| `--dry-run` | 無効 | APIへ接続せず入力件数と選択件数を表示 |
| `--rate-limit-count` | `100` | ルートごとのローカルリクエスト数 |
| `--rate-limit-window` | `120` | レート制限の時間窓（秒） |
| `--min-interval` | `0.06` | 同一ルート間の最小間隔（秒） |
| `--timeout` | `30` | HTTPタイムアウト（秒） |
| `--max-retries` | `6` | 429、5xx、通信エラーの再試行回数 |

`--dry-run`はAPIキーなしで実行できる。通常実行では`RIOT_API_KEY`がない場合、APIへ接続せずエラー終了する。

## 6. 出力仕様

実行ごとに`run-YYYYMMDDTHHMMSSZ/`を作成する。

```text
reports/riot-match-timeline/
├── .cache/
│   └── timelines/<match-id>.json
└── run-YYYYMMDDTHHMMSSZ/
    ├── timelines.jsonl
    ├── errors.jsonl
    └── manifest.json
```

### 6.1 `timelines.jsonl`

1行が1試合の個人識別情報を除いたTimelineレコードである。

```json
{
  "schema_version": 1,
  "match_id": "JP1_0000000000",
  "game_start_timestamp": 1760000000000,
  "game_version": "16.18",
  "queue_id": 420,
  "observed_tiers": ["GOLD"],
  "observed_divisions": ["I"],
  "timeline": {
    "metadata": {"dataVersion": "2", "matchId": "JP1_0000000000"},
    "info": {"frameInterval": 60000, "frames": []}
  }
}
```

`timeline.info.frames`以下のイベント、参加者フレーム、時刻情報は保持する。`metadata.participants`の`participantId`は保持するが、PUUIDは除去する。入力のMatch-v5本文やキャッシュを出力へコピーしない。

### 6.2 `errors.jsonl`

取得できなかった試合について、`match_id`、HTTPステータス、一般化した失敗理由を記録する。APIエラー本文やリクエストヘッダーは保存しない。401・403は認証または権限の問題として全体を停止し、404や個別の不正レスポンスは他の試合の取得を継続して失敗行へ記録する。

### 6.3 `manifest.json`

次の情報を記録する。

- スクリプト名、スキーマバージョン、取得日時
- 入力ファイル、プラットフォーム、地域ルート、エンドポイント、キュー
- パッチ・日付・件数のフィルター
- 入力候補数、選択数、キャッシュ利用数、API取得数、失敗数
- 入力品質（JSON不正、試合ID欠損、重複試合ID）
- 出力ファイル、キャッシュ位置、個人識別情報を除去したこと

## 7. キャッシュと再実行

- キャッシュキーは試合IDを安全なファイル名へ変換した値とする。
- キャッシュにもAPI取得済みのサニタイズ済みTimelineだけを保存する。
- 同じ`--output`ルートを使えば、別の実行ディレクトリへ同じキャッシュを再利用できる。
- APIレスポンスを更新したい場合だけ`--refresh`を指定する。
- 出力先の既存実行ディレクトリは、`--overwrite`なしでは上書きしない。

## 8. レート制限と再試行

HTTP通信、429の`Retry-After`、5xx、通信エラー、ルートごとのスライディングウィンドウは既存の`riot_ranked_match_collector.py`の`RiotClient`を再利用する。Timeline取得固有の新しいレート制限値は定義せず、CLIで調整できるようにする。

## 9. データ品質と限界

- Timelineの存在は試合詳細の存在を意味しない。保存期間やAPI側の状態により404となる場合がある。
- 現在のMatch-v5入力は収集時点の観測ランク帯を持つため、Timeline自体が試合時点のランクを保証するものではない。
- `--limit`は取得件数の上限であり、統計的な代表性や無作為抽出を保証しない。
- Timelineはイベントとフレームの記録であり、これだけで購入順、勝因、因果効果、最適ビルドを確定しない。
- `participantId`は同一試合のMatch-v5参加者と対応付けられるが、出力単体では個人を特定できる対応表を保持しない。
- APIキーがない環境では、`--dry-run`による入力検証までを実行可能範囲とする。

## 10. 実行例

### 入力と件数の確認

```bash
python3 scripts/riot_match_timeline_collector.py \
  --input raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5/gold/matches.jsonl \
  --limit 10 --dry-run
```

### 最新10件の取得

```bash
RIOT_API_KEY='RGAPI-...' \
python3 scripts/riot_match_timeline_collector.py \
  --input raw/sources/riot-ranked-matches \
  --output reports/riot-match-timeline \
  --limit 10
```

### 特定パッチ・試合の再取得

```bash
RIOT_API_KEY='RGAPI-...' \
python3 scripts/riot_match_timeline_collector.py \
  --input raw/sources/riot-ranked-matches \
  --patch 16.18 \
  --match-id JP1_0000000000 \
  --refresh
```

## 11. 受け入れ条件

- `--help`、`--dry-run`、Python構文チェックがAPIキーなしで成功する。
- 同一試合IDが入力に複数存在しても、選択・API呼び出し・出力は1件に統合される。
- Timelineエンドポイントを地域ルート付きで呼び出し、429・5xx・通信エラーを既存クライアントの規則で処理する。
- 成功レコードは`info.frames`を持ち、指定順で`timelines.jsonl`へ出力される。
- `timelines.jsonl`、キャッシュ、マニフェスト、エラー出力のいずれにもPUUID、summoner ID、summoner name、Riot IDを含めない。
- APIキー、レスポンスヘッダー、APIエラー本文をログやマニフェストへ保存しない。
- `--dry-run`と通常実行のどちらも`raw/`を変更しない。

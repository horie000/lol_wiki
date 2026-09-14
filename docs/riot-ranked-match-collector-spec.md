# Riot API ランク戦データ収集仕様書

- 仕様バージョン：1.1
- 実装：`scripts/riot_ranked_match_collector.py`
- 作成日：2026-09-15
- 対象ゲーム：League of Legends

## 1. 目的

Riot Games API を利用し、指定地域のランク戦について、ランク帯ごとに直近の試合を1,000件ずつ収集する。収集した試合は後続のチャンピオン、アイテム、ルーン、スペル、勝敗などの統計分析に利用できる形式で保存する。

本仕様でいう「ランク帯」は次の10段階である。

`IRON`、`BRONZE`、`SILVER`、`GOLD`、`PLATINUM`、`EMERALD`、`DIAMOND`、`MASTER`、`GRANDMASTER`、`CHALLENGER`

既定のキューは Ranked Solo/Duo（`RANKED_SOLO_5x5`、queue ID `420`）とする。Ranked Flex（`RANKED_FLEX_SR`、queue ID `440`）もCLIで選択できる。

## 2. 対象範囲と前提

- 既定のプラットフォームは `jp1`、地域ルートは自動的に `asia` とする。
- `--platform` で `na1`、`euw1`、`kr` などのプラットフォームを指定できる。
- `--regional-route` は通常 `auto` とし、Match-v5のルートを明示的に上書きできる。
- 試合の「直近」は Match-v5 の `info.gameStartTimestamp` の降順で判定する。
- 同じ試合IDが同一ランク帯の複数プレイヤーから得られた場合は1件に統合する。
- 同じ試合が複数ランク帯の出力に現れることは許容する。これは、1試合に複数のランク帯のプレイヤーが参加し得るためである。
- ランク帯は収集時点のLeague-v4ランキング情報で観測した所属帯であり、試合実施時点のランクを復元するものではない。

## 3. 利用APIとルーティング

| 用途 | HTTPパス | ルート |
| --- | --- | --- |
| 通常ランク帯の所属者 | `/lol/league/v4/entries/{queue}/{tier}/{division}` | プラットフォーム |
| Master所属者 | `/lol/league/v4/masterleagues/by-queue/{queue}` | プラットフォーム |
| Grandmaster所属者 | `/lol/league/v4/grandmasterleagues/by-queue/{queue}` | プラットフォーム |
| Challenger所属者 | `/lol/league/v4/challengerleagues/by-queue/{queue}` | プラットフォーム |
| `summonerId`からPUUID取得 | `/lol/summoner/v4/summoners/{encryptedSummonerId}` | プラットフォーム |
| PUUID別の試合ID | `/lol/match/v5/matches/by-puuid/{puuid}/ids` | 地域 |
| 試合詳細 | `/lol/match/v5/matches/{matchId}` | 地域 |

通常ランク帯は `I`～`IV` の4ディビジョンを取得し、Master以上は専用リーグエンドポイントを取得する。League-v4のレスポンスに `puuid` がない場合だけ、Summoner-v4で `summonerId` をPUUIDへ変換する。

試合IDの取得には次のクエリを付ける。

```text
queue=420 または 440
type=ranked
start=0, 100, 200, ...
count=100
```

## 4. 収集処理

1. 対象キュー、プラットフォーム、地域ルート、ランク帯を確定する。
2. League-v4からランク帯のエントリを取得する。通常帯は4ディビジョン、高ランク帯は専用エンドポイントを使う。
3. ランク帯ごとにプレイヤーを決定的に均等サンプリングする。既定は100人、`--max-players-per-tier 0` で取得できた全員を対象にする。
4. 各プレイヤーのPUUIDからMatch-v5の試合IDを新しい順に取得する。候補が目標件数の2倍に達するか、指定した履歴ページ上限に達した時点で次へ進む。
5. 試合詳細を取得し、queue ID、試合開始時刻、`info` の存在を検証する。404や不完全なレスポンスは候補から除外する。
6. 試合IDをランク帯内で重複排除し、`gameStartTimestamp` の降順で並べる。
7. 先頭1,000件を `matches.jsonl` に保存し、収集件数・候補件数・欠損件数を `manifest.json` に保存する。
8. 試合詳細は共有キャッシュへ保存し、複数ランク帯で同じ試合を再取得しない。

収集中は標準出力へ全体（ランク帯）と各処理（PUUID解決、試合ID候補取得、試合詳細取得）のシーケンスバーを表示する。各ランク帯の保存完了後、全ランク帯の収集完了時に所要時間を表示する。APIの再試行メッセージとエラーは標準エラー出力へ表示する。

目標件数に満たない場合、既定ではそのランク帯の出力を作らず終了する。`--allow-incomplete` を指定した場合だけ、取得できた件数で `complete: false` の出力を許可する。

## 5. CLI仕様

主要オプションは次のとおり。

| オプション | 既定値 | 説明 |
| --- | --- | --- |
| `--platform` | `jp1` | プラットフォームID |
| `--regional-route` | `auto` | `americas`、`asia`、`europe`、`sea`、`auto` |
| `--queue` | `RANKED_SOLO_5x5` | Ranked Solo または Ranked Flex |
| `--tiers` | 全10帯 | カンマ区切りで対象帯を限定 |
| `--match-count` | `1000` | 帯ごとの要求件数 |
| `--max-players-per-tier` | `100` | 候補プレイヤー数。`0` は全員 |
| `--candidate-multiplier` | `2.0` | 詳細取得候補の目標倍率 |
| `--max-pages-per-player` | `5` | 1ページ100試合の履歴ページ上限 |
| `--output` | `raw/sources/riot-ranked-matches` | `raw/`配下の出力ルート。`raw/`外は拒否 |
| `--overwrite` | 無効 | 既存の帯別ファイルを上書き |
| `--allow-incomplete` | 無効 | 1,000件未満の出力を許可 |
| `--dry-run` | 無効 | APIへ接続せず設定だけ確認 |

### APIキー

APIキーはコマンドライン引数に渡さず、環境変数で指定する。

```bash
export RIOT_API_KEY='RGAPI-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
```

### 進捗表示

進捗は標準出力へ次のような形式で表示する。バーは端末上で更新され、リダイレクト時はキャリッジリターンを含むログとなる。

```text
全体進捗 [########------------------------] 2/10 ( 20.0%)
[GOLD] 試合詳細取得 [################----------------] 500/1000 ( 50.0%)
収集完了: 10ランク帯、所要時間 18分42.3秒
```

## 6. 出力仕様

収集データは必ずリポジトリ内の `raw/` 配下へ保存する。`--output` を変更する場合も、
`raw/` 外のパス（`wiki/`、`docs/`、リポジトリ外など）はスクリプトが拒否する。
既定の出力構成は次のとおり。

```text
raw/sources/riot-ranked-matches/
├── .cache/
│   ├── matches/<match-id>.json
│   └── summoner-puuids.json
└── jp1/
    └── ranked-solo-5x5/
        ├── iron/
        │   ├── matches.jsonl
        │   └── manifest.json
        ├── bronze/
        └── ...
```

### `matches.jsonl`

1行が1試合のJSONオブジェクトである。`match` はMatch-v5のレスポンスを保持し、周辺フィールドで収集時の観測情報を持つ。

```json
{
  "schema_version": 1,
  "match_id": "JP1_0000000000",
  "game_start_timestamp": 1760000000000,
  "observed_tier": "GOLD",
  "observed_divisions": ["I", "II"],
  "match": {
    "metadata": {},
    "info": {}
  }
}
```

`match` 内の参加者情報にはPUUID等の識別子が含まれ得るため、公開用データへ変換する際は別途匿名化する。

### `manifest.json`

次の管理情報を保存する。

- スクリプト名とスキーマバージョン
- 収集日時（UTC）
- プラットフォーム、地域ルート、キュー、queue ID、ランク帯
- 要求件数、収集件数、`complete` フラグ
- League-v4のエントリ数、サンプル数、PUUID解決数
- 候補試合数、有効な詳細数、除外数
- ランク帯の観測上の意味と選択方法

APIキー、レスポンスヘッダー、キーそのものは保存しない。

## 7. レート制限と再試行

- ルートごとにスライディングウィンドウを持つ。
- 既定値は100リクエスト / 120秒、同一ルート間隔0.06秒とする。Riotの個人キーでの利用を想定した保守的な値である。
- HTTP 429では `Retry-After` 秒数を読み、待機して再試行する。
- HTTP 500、502、503、504および通信エラーは指数バックオフ（最大60秒）で最大6回再試行する。
- HTTP 401、403、400などの恒久的エラーは即時終了する。
- 本番キーで許可された制限が異なる場合は、`--rate-limit-count`、`--rate-limit-window`、`--min-interval` を利用者が調整する。

## 8. データ品質と限界

- Riot APIには「ランク帯別の全試合を直接返す」エンドポイントがないため、現在その帯に所属するプレイヤーのMatch-v5履歴を候補源とする。
- 既定の100人サンプルはAPI呼び出し量と網羅性のトレードオフである。より網羅的に収集する場合は `--max-players-per-tier 0` を指定する。
- 100人サンプルで候補が不足する場合は、`--max-pages-per-player` または `--max-players-per-tier` を増やす。
- 現在ランクと試合時点ランクは一致しない可能性がある。
- 試合詳細の欠損、APIの404、プレイヤーの試合履歴上限により、1,000件に到達できない場合がある。
- 同じ試合が複数ランク帯に記録されることは仕様上正常である。
- 本スクリプトは勝率やビルドの推論を行わず、APIレスポンスの収集と時刻順の選択だけを担当する。

## 9. 実行例

### 設定確認

```bash
python3 scripts/riot_ranked_match_collector.py --platform jp1 --dry-run
```

### 全ランク帯を1,000件ずつ収集

```bash
RIOT_API_KEY='RGAPI-...' \
python3 scripts/riot_ranked_match_collector.py \
  --platform jp1 \
  --output raw/sources/riot-ranked-matches \
  --overwrite
```

### 対象をヴィエゴ分析用の上位帯に限定

```bash
RIOT_API_KEY='RGAPI-...' \
python3 scripts/riot_ranked_match_collector.py \
  --platform jp1 \
  --tiers DIAMOND,MASTER,GRANDMASTER,CHALLENGER \
  --overwrite
```

### 帯内プレイヤーを全件対象にする

```bash
RIOT_API_KEY='RGAPI-...' \
python3 scripts/riot_ranked_match_collector.py \
  --platform jp1 \
  --max-players-per-tier 0 \
  --overwrite
```

## 10. 受け入れ条件

- APIキーをソースコード、ログ、出力メタデータへ書き込まない。
- 対象キュー以外の試合を `matches.jsonl` に保存しない。
- 各帯の `complete` が真の場合、`matches.jsonl` は重複しない1,000行である。
- 行の `match_id` が一意で、`game_start_timestamp` の降順に並ぶ。
- 429、5xx、通信エラーを規定どおり処理する。
- 中断後にキャッシュを利用して再実行できる。
- `--dry-run`、`--help`、Python構文チェックがAPIキーなしで成功する。

## 11. 公式仕様

- [Riot Games League of Legends API documentation](https://developer.riotgames.com/docs/lol)
- [Riot Developer Portal API reference](https://developer.riotgames.com/apis)
- [Riot Developer Portal: rate limits and error handling](https://developer.riotgames.com/docs/portal)

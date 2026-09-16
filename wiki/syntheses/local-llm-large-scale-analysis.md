---
title: "大量データ解析向けローカルLLM運用：トークン削減・検索・モデル切り替え"
type: synthesis
status: active
created: 2026-09-16
updated: 2026-09-16
sources:
  - "[[wiki/sources/src-2023-10-09-llmlingua]]"
  - "[[wiki/sources/src-2023-10-10-longllmlingua]]"
  - "[[wiki/sources/src-2024-03-19-llmlingua-2]]"
  - "[[wiki/sources/src-2024-01-31-raptor]]"
  - "[[wiki/sources/src-2024-04-24-graphrag]]"
  - "[[wiki/sources/src-2023-07-06-lost-in-the-middle]]"
  - "[[wiki/sources/src-2023-09-12-pagedattention]]"
  - "[[wiki/sources/src-2023-05-23-qlora]]"
  - "[[wiki/sources/src-2023-05-09-frugalgpt]]"
  - "[[wiki/sources/src-2024-06-26-routellm]]"
  - "[[wiki/sources/src-2024-03-18-routerbench]]"
  - "[[wiki/sources/src-2026-09-16-llama-cpp-readme]]"
tags:
  - local-llm
  - large-scale-analysis
  - token-efficiency
  - model-routing
---

# 大量データ解析向けローカルLLM運用：トークン削減・検索・モデル切り替え

## 問い

本プロジェクトのように、複数パッチの実測データと大量のレポートを扱う場合、ローカルLLMの入力トークン、推論メモリ、応答品質をどう両立し、問い合わせごとにモデルを切り替えるべきか。

## 統合

原典を横断すると、単一の「大きいモデルへ全文投入」ではなく、(1) 入力を減らす、(2) 必要な抽象度だけ検索する、(3) 難しい問い合わせだけ強いモデルへ切り替える、(4) 実行基盤を量子化・キャッシュに合わせる、という分離が再利用しやすい。以下の数値は各原典の評価条件であり、本Wikiの日本語データで再現した値ではない。

| 運用層 | 原典が示す方法・観測 | 本プロジェクトへの適用候補 | 主な注意 |
| --- | --- | --- | --- |
| プロンプト削減 | LLMLinguaは最大20倍、LongLLMLinguaは約4分の1の入力や2〜6倍圧縮、LLMLingua-2は2〜5倍圧縮と圧縮器高速化を報告 | 長いレポートをモデルへ渡す直前に、表の列名・ID・数値を保護する圧縮器を比較 | 圧縮器のコスト、固有名詞・構造の欠落、数値の改変を測る |
| 階層検索 | RAPTORは再帰的な埋め込み・クラスタ・要約木、GraphRAGはエンティティグラフとコミュニティ要約を事前生成 | 個別値は通常検索、全体傾向・テーマ質問は要約木／グラフ要約へ分岐 | インデックス構築・更新のトークン費用と要約誤りを原典へ追跡 |
| 長文の品質管理 | Lost in the Middleは重要情報の位置で性能が変わり、中央で低下する位置バイアスを報告 | 全文連結を既定にせず、検索・再配置・圧縮後の入力を基準にする | モデル、言語、コンテキスト長ごとに再評価する |
| モデル切り替え | FrugalGPTは信頼度付き順次カスケード、RouteLLMは選好データによる強／弱モデルの事前ルーティング、RouterBenchは費用・品質曲線を評価 | 軽量ローカルモデルを既定にし、難易度・信頼度・出典不足時だけ高性能モデルへエスカレーション | ルータ誤判定、追加遅延、モデル更新時の再校正を記録する |
| ローカル推論基盤 | llama.cppは量子化、CPU+GPUハイブリッド、CLI／OpenAI互換サーバを提示。PagedAttention／vLLMはKVキャッシュ共有と多リクエストGPUサービングを改善 | 単一Mac・小規模バッチはllama.cpp、多並列GPU処理はvLLMを比較 | READMEは更新され、PagedAttentionの結果はGPUサーバ中心である |
| タスク適応 | QLoRAは凍結4ビットモデル＋LoRAで学習時メモリを削減 | 用語・出力形式を固定した小型分析モデルのアダプター候補 | 学習時メモリの話であり、入力トークン削減や因果的な正確性を直接保証しない |

## 運用案（統合結果からの推論）

1. **機械的な前処理を先に固定する。** CSV・JSON・レポートを正規化し、パッチ、ロール、分母、出典パス、計算式をLLM入力とは別の構造化フィールドとして保持する。
2. **質問の種類で検索経路を分ける。** 単一チャンピオンや単一集計値は通常の絞り込み、複数レポートの全体傾向はRAPTOR／GraphRAG型の事前要約へ送る。全文を毎回連結しない。
3. **圧縮は品質ゲート付きで行う。** まず圧縮なしを基準にし、LLMLingua系を2倍、4倍、必要ならそれ以上で比較する。ID、数値、表見出し、引用リンクの保持率を自動検査し、失敗時は元入力へ戻す。
4. **モデルルータを後段に置く。** 小型量子化モデルで下書き・単純集計を処理し、信頼度、出典完全性、矛盾検出、入力規模が閾値を超えたときだけ大きいローカルモデルへ切り替える。カスケードを使う場合は、呼び出し回数と遅延を単一ルータと比較する。
5. **同じスナップショットで記録する。** `input_tokens`、`output_tokens`、圧縮率、検索チャンク数、モデルID、フォールバック率、遅延、ピークメモリ、正確性、出典リンク率を実行manifestへ保存する。これは原典にない本プロジェクト固有の評価提案である。

## llm-wikiのドメイン知識を別エージェントへ渡す設計（内部設計案）

大量データを解析するエージェントと、蓄積済みの知識を参照して回答するエージェントを分離する場合、`AGENTS.md` と `wiki/` の責務を混ぜないことが重要である。以下は外部論文の実証結果ではなく、ユーザー指定のリポジトリ規則とLLM Wiki運用から導いた役割設計である。

### 二層に分ける

- **制御層（`AGENTS.md`）**：安定した言語、原典優先、パス所有権、出典・不確実性、編集権限などを短く定義する。ここで既定の編集者を `llm-wiki-editor` と明示する。
- **知識層（`wiki/`）**：チャンピオン、試合データ、LLM運用研究などの変化する事実・分析・相互リンクを `wiki/index.md` から辿れる形で保持する。
- **参照エージェント契約（呼び出し時）**：`role_id: llm-wiki-reader`、`authority: read-only`、`write_scope: []`、禁止操作、出力形式をsystem/developerメッセージへ注入する。テンプレートは [[docs/agent-role-contracts.md|docs/agent-role-contracts.md]] に保存した。

### reader契約の最小形

```yaml
role_id: llm-wiki-reader
identity: "llm-wikiの参照専用エージェント。llm-wiki-editorではない"
authority: read-only
read_scope: [wiki/index.md, wiki/**, 必要時のみraw/sources/**]
write_scope: []
source_order: [wiki/index.md, 関連Wikiページ, 必要時のみraw/sources]
output_contract: "日本語。事実・推論・未解決を分離し、Wikiと原典要約へリンクする"
prohibitions: [ファイル変更, レポート生成, git操作, コミット]
```

最小契約には「あなたは `llm-wiki-reader` であり、`llm-wiki-editor` ではない。回答だけを返し、Vault内のファイルを変更してはならない」という否定形の一文も添える。参照専用という形容詞だけでは、ルート `AGENTS.md` の編集手順を誤って権限と解釈する余地が残る。

### 推奨する参照フロー

1. readerへ契約とVaultの絶対パスだけを渡し、まず `wiki/index.md` を読ませる。
2. 質問に必要なsource／concept／synthesis／entityだけを選ばせ、`reports/` は対応する原典要約を経由して扱わせる。
3. 原典照合が必要な場合だけ `raw/sources/` を読み、回答中の事実・推論・未解決を分ける。
4. 更新候補が出ても、readerは直接編集せず、対象ページ・根拠・差分概要を編集者への提案として返す。
5. 実際の取り込み・統合・索引・ログ更新は、別タスクで明示的に `llm-wiki-editor` を起動して行う。

### 境界上の注意

> [!warning] readerとeditorの混同
> `AGENTS.md` は編集者の運用規則であり、参照エージェントの書き込み権限を意味しない。readerには `write_scope: []`、禁止操作、`llm-wiki-editorではない` の3点を必ず明示する。

- 役割契約をVault内の別 `AGENTS.md` として都度作成すると、AGENTSの階層探索による上書きや適用範囲の誤認が起きる。呼び出し側のsystem/developerメッセージ、またはVault外のタスク契約を使う。
- `AGENTS.md` に大量のドメイン知識を複製すると、更新漏れとコンテキスト消費が増える。知識はWikiへ置き、readerには索引から必要なページだけを与える。
- readerの回答品質は、参照したWikiページ・原典要約へのリンク、数値一致、未解決事項を記録して評価する。これは外部研究のベンチマークではなく、本プロジェクト固有の運用提案である。
- `write_scope: []` は役割の宣言であり、権限の強制ではない。readerはVault外の作業ディレクトリから起動し、Vaultをread-onlyで公開し、編集・シェル書き込み・Gitツールを呼び出し側で無効化する。契約と実行権限を二重化して初めて「参照専用」を運用上の境界にできる。

## 実施内容と評価（内部分析）

### 実施したこと（事実）

- 大量データ解析を対象に、arXiv論文11件とllama.cpp READMEの計12原典を `raw/sources/` に固定し、それぞれの日本語分析レポートを `wiki/sources/` に作成した。
- 各レポートを、プロンプト圧縮、階層・グラフ検索、長文品質管理、モデル切り替え、量子化・サービングの運用層へ整理し、本ページへ統合した。
- 既存Wikiを別エージェントが読む場合の制御層（`AGENTS.md`）、知識層（`wiki/`）、呼び出し時契約（`llm-wiki-reader`）を分離した。最小契約は [[docs/agent-role-contracts.md|エージェント役割契約]] に固定し、ルート指示・概要・ログから辿れるようにした。
- `scripts/lint.py`、WikiページのYAML・リンク・出典構造検査を実行し、既存の生成ページと新規レポートの整合を確認した。

### 分析（この構成から導くこと）

| 観点 | 評価 | 条件・限界 |
| --- | --- | --- |
| 知識の鮮度 | 変化する統計・研究メモを `wiki/` に置き、`AGENTS.md` は安定した境界だけにするため、指示と知識の更新周期を分離できる | readerが毎回 `wiki/index.md` を起点にする運用が必要 |
| コンテキスト効率 | 索引→質問に必要なページ→必要時だけ原典という遅延参照により、全Wiki投入を避けられる | 実際の入力トークン削減量はまだ測定していない |
| 安全性 | identity、`write_scope: []`、禁止操作、read-only実行環境を重ねることで、reader/editor混同への防御を多層化できる | プロンプト契約だけでは書き込み権限を剥奪できない |
| 追跡可能性 | 事実・推論・未解決を分離し、Wikiページと原典要約へリンクするため、回答から根拠へ戻れる | 原典にない推奨を自動的に正当化するものではない |
| 分析パイプライン | 前処理・検索・圧縮・ルーティング・実行基盤を別層で評価でき、失敗時の切り戻し点を作れる | 各原典のベンチマーク値は本プロジェクトの日本語データで再現していない |

### 未検証のため、現時点で結論にしないこと

- readerが実行環境の違いを含めて本当に編集しないか、出典リンク率・数値一致率・拒否率を測定していない。
- `wiki/index.md` 起点の遅延参照が、全ページ投入と比べて何トークン・何秒を削減するか未測定である。
- 圧縮器、要約インデックス、ルータ、量子化ランタイムを組み合わせたときの日本語・表・JSONの忠実性、品質、消費電力は未検証である。

したがって、今回の成果は「運用可能な境界と評価計画を整えた」段階であり、特定モデル・圧縮率・ルータを本番採用したという結論ではない。

## 証拠と解釈

- 圧縮率の数値は、LLMLinguaの最大20倍、LongLLMLinguaの約4倍削減、LLMLingua-2の2〜5倍など、データセット・モデル・測定定義が異なるため横並びの保証ではない。[[wiki/sources/src-2023-10-09-llmlingua|LLMLingua]]、[[wiki/sources/src-2023-10-10-longllmlingua|LongLLMLingua]]、[[wiki/sources/src-2024-03-19-llmlingua-2|LLMLingua-2]]
- RAPTORとGraphRAGは、前処理済みの階層・グラフ要約を検索することで全体質問を扱う設計を示すが、前処理費用を含む総トークン削減量は各原典要旨からは確定しない。[[wiki/sources/src-2024-01-31-raptor|RAPTOR]]、[[wiki/sources/src-2024-04-24-graphrag|GraphRAG]]
- FrugalGPT、RouteLLM、RouterBenchはいずれも費用・品質のトレードオフを扱うが、商用APIや旧世代モデルを含む評価である。ローカルモデルの電力・保守費用へは、そのまま換算できない。[[wiki/sources/src-2023-05-09-frugalgpt|FrugalGPT]]、[[wiki/sources/src-2024-06-26-routellm|RouteLLM]]、[[wiki/sources/src-2024-03-18-routerbench|RouterBench]]
- llama.cppとPagedAttention／vLLMは対象ハードウェアと並列度が異なるため、どちらが常に速いという結論ではなく、単一マシンと多並列サーバの候補として比較する。[[wiki/sources/src-2026-09-16-llama-cpp-readme|llama.cpp README]]、[[wiki/sources/src-2023-09-12-pagedattention|PagedAttention]]

## 矛盾と不確実性

> [!warning] 圧縮と忠実性のトレードオフ
> 高い圧縮率を報告する研究がある一方、長文・構造化データ・日本語で重要な数値や出典が保たれるとは限らない。圧縮率だけで採用せず、原文との差分検査とタスク精度を同一スナップショットで確認する。

> [!warning] カスケードと単一ルータの差
> FrugalGPTの順次カスケードは低品質時に追加モデルを呼ぶため品質を補えるが、呼び出し回数・遅延が増える。RouteLLMは事前に一つのモデルを選ぶため低遅延になり得る一方、選択前に誤りを検出できない。両者を同じ品質指標・費用定義で比較する必要がある。

- GraphRAG／RAPTORの要約は、検索対象を縮める代わりにインデックスの更新遅延と要約誤りを導入する。
- QLoRAのメモリ削減、llama.cppの量子化、PagedAttentionのKV管理は、互いに異なる段階の最適化であり、一つの「トークン削減率」へ合算できない。
- RouterBench自身が、遅延・スループット・新しいモデル・ドメイン固有タスクの不足を限界としている。

## 未解決の問い

- 20,010件の完全試合を含む既存レポートで、圧縮・階層検索・ルーティングを組み合わせたときの品質、入力トークン、総処理時間はどう変わるか。
- 軽量ローカルモデルの信頼度を、出典リンク率・数値一致・矛盾検出で校正できるか。
- 要約木・グラフインデックスをパッチ追加時に差分更新し、古い集計の混入をLintで検出できるか。
- Apple Siliconの単一マシンとGPUサーバで、同じGGUF／量子化レベルを使った費用・電力・スループット比較をどう再現するか。

## 出典

- [[wiki/sources/src-2023-10-09-llmlingua|LLMLingua：LLM推論を高速化するプロンプト圧縮]]
- [[wiki/sources/src-2023-10-10-longllmlingua|LongLLMLingua：長文コンテキスト向けプロンプト圧縮]]
- [[wiki/sources/src-2024-03-19-llmlingua-2|LLMLingua-2：タスク非依存プロンプト圧縮]]
- [[wiki/sources/src-2024-01-31-raptor|RAPTOR：木構造検索のための再帰的抽象処理]]
- [[wiki/sources/src-2024-04-24-graphrag|GraphRAG：ローカルからグローバルへのクエリ指向要約]]
- [[wiki/sources/src-2023-07-06-lost-in-the-middle|Lost in the Middle：長文入力の位置バイアス]]
- [[wiki/sources/src-2023-09-12-pagedattention|PagedAttention：LLMサービングの効率的メモリ管理]]
- [[wiki/sources/src-2023-05-23-qlora|QLoRA：量子化LLMの効率的ファインチューニング]]
- [[wiki/sources/src-2023-05-09-frugalgpt|FrugalGPT：コスト削減と性能向上のLLM利用]]
- [[wiki/sources/src-2024-06-26-routellm|RouteLLM：選好データによるLLMルーティング]]
- [[wiki/sources/src-2024-03-18-routerbench|RouterBench：マルチLLMルーティング評価ベンチマーク]]
- [[wiki/sources/src-2026-09-16-llama-cpp-readme|llama.cpp README：ローカルLLM推論ランタイム]]
- 内部運用規則：[[AGENTS.md|AGENTS.md]]、[[.agents/skills/llm-wiki/SKILL.md|llm-wikiスキル]]、[[docs/agent-role-contracts.md|エージェント役割契約]]

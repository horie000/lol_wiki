---
title: "Lost in the Middle：長文入力の位置バイアス"
type: source
status: active
source_path: raw/sources/lost-in-the-middle-2307.03172.md
source_url: https://arxiv.org/abs/2307.03172
source_date: 2023-07-06
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - long-context
  - evaluation
---

# Lost in the Middle：長文入力の位置バイアス

## 要約

長いコンテキストを受け付けるLLMが、入力内の情報をどの位置でも同じように使えるかを、多文書QAとキー・バリュー検索で検証した研究である。関連情報が入力の中央にあると性能が低下し、先頭・末尾で高くなるU字型の位置依存を報告する。

## 主要な主張

- 長い入力を許容するモデルであっても、関連情報の位置を変えると性能が大きく変わる。
- 入力を長くして情報を増やすことは、利用可能な知識を増やす一方、モデルが推論すべき無関係情報も増やすトレードオフになる。
- 長文をそのまま投入する前に、検索・再配置・圧縮・階層要約を評価すべきだという運用上の警告を与える。

## 根拠と限界

- 原典は制御されたQA・キー値検索の評価であり、実務の集計表や日本語モデルの挙動を直接保証しない。
- 位置バイアスの大きさはモデル、コンテキスト長、プロンプト形式に依存するため、導入先での再測定が必要である。
- 本研究はトークン削減手法そのものではなく、削減・検索を検討する理由を示す基礎評価である。

## 関連ページ

- [[wiki/sources/src-2023-10-10-longllmlingua|LongLLMLingua：長文コンテキスト向けプロンプト圧縮]] — 位置バイアスとノイズを圧縮で扱う。
- [[wiki/sources/src-2024-01-31-raptor|RAPTOR：木構造検索のための再帰的抽象処理]] — 階層レベルから必要情報を検索する。
- [[wiki/sources/src-2024-04-24-graphrag|GraphRAG：ローカルからグローバルへのクエリ指向要約]] — 全体質問向けの中間要約。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 評価設計の注意点。

## 未解決の問い

- 本プロジェクトのレポートをチャンク化したとき、情報位置と回答品質の関係をどの評価指標で記録するか。
- 圧縮後・検索後の入力で位置バイアスがどこまで軽減されるか。

## 出典

- 原典スナップショット：[[raw/sources/lost-in-the-middle-2307.03172.md|lost-in-the-middle-2307.03172.md]]
- 公開ページ：[Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)

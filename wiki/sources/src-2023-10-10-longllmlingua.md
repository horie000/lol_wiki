---
title: "LongLLMLingua：長文コンテキスト向けプロンプト圧縮"
type: source
status: active
source_path: raw/sources/longllmlingua-2310.06839.md
source_url: https://arxiv.org/abs/2310.06839
source_date: 2023-10-10
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - prompt-compression
  - long-context
---

# LongLLMLingua：長文コンテキスト向けプロンプト圧縮

## 要約

長文入力で増える計算費用、無関係な情報による性能低下、重要情報の位置バイアスを同時に扱う、質問依存のプロンプト圧縮手法である。文書の並べ替え、動的圧縮率、圧縮後の部分列復元を組み合わせ、質問に関係する情報の密度を高める。

## 主要な主張

- NaturalQuestionsでは、GPT-3.5-Turboに対して約4分の1のトークンで性能を最大21.4%改善したと報告している。
- LooGLEでは94.0%のコスト削減、約1万トークン入力を2〜6倍に圧縮した条件でエンドツーエンド遅延1.4〜2.6倍を報告している。
- 圧縮率を質問や文書ごとに変えることで、重要情報を一律に削らない設計を採る。

## 根拠と限界

- 数値は原典要旨に記載された長文ベンチマーク結果であり、GPT-3.5-Turbo等の外部モデルを含む評価である。
- 質問依存圧縮は問い合わせごとに異なる入力を生成するため、共通プレフィックスのキャッシュとは相性が悪くなる可能性がある（本プロジェクトでの推論）。
- 圧縮器自体の実行時間、固有名詞・表・コードの欠落リスクを、ローカルモデルと日本語データで検証する必要がある。

## 関連ページ

- [[wiki/sources/src-2023-10-09-llmlingua|LLMLingua：LLM推論を高速化するプロンプト圧縮]] — 基礎となる圧縮器。
- [[wiki/sources/src-2024-03-19-llmlingua-2|LLMLingua-2：タスク非依存プロンプト圧縮]] — 圧縮器を小型化する後続研究。
- [[wiki/sources/src-2023-07-06-lost-in-the-middle|Lost in the Middle：長文入力の位置バイアス]] — 長文をそのまま渡す際の注意点。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — トークン削減策の比較。

## 未解決の問い

- 圧縮を検索・集計パイプラインのどの段階に置くと、キャッシュ再利用と品質を両立できるか。
- 重要な数値やIDを保持する制約を加えた場合の圧縮率と精度はどの程度か。

## 出典

- 原典スナップショット：[[raw/sources/longllmlingua-2310.06839.md|longllmlingua-2310.06839.md]]
- 公開ページ：[LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression](https://arxiv.org/abs/2310.06839)

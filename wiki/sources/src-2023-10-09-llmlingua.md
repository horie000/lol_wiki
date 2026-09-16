---
title: "LLMLingua：LLM推論を高速化するプロンプト圧縮"
type: source
status: active
source_path: raw/sources/llmlingua-2310.05736.md
source_url: https://arxiv.org/abs/2310.05736
source_date: 2023-10-09
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - prompt-compression
  - token-efficiency
---

# LLMLingua：LLM推論を高速化するプロンプト圧縮

## 要約

長いChain-of-Thoughtやin-context learningの入力を、意味を保ちながら段階的に圧縮する手法を提案した論文である。予算制御、トークン単位の反復圧縮、言語モデル間の分布整合を組み合わせ、圧縮後のプロンプトを下流LLMへ渡す。

## 主要な主張

- GSM8K、BBH、ShareGPT、Arxiv-March23の4データセットで、性能を大きく損なわず最大20倍の圧縮を報告している。
- 圧縮率を固定的に決めるのではなく、予算コントローラで意味の整合性を保ちながら粗粒度から細粒度へ圧縮する。
- コードを公開しており、ローカルの小型モデルを圧縮器として検証できる。

## 根拠と限界

- 数値は原典要旨に記載されたベンチマーク結果であり、本プロジェクトの日本語Wiki・Riotデータで再現した結果ではない。
- 圧縮器の推論コスト、ドメイン固有語・表形式データの情報損失、圧縮率と正確性のトレードオフは別途測定が必要である。
- 最大20倍は評価条件の上限値であり、すべてのタスクで同じ品質が得られることを意味しない。

## 関連ページ

- [[wiki/sources/src-2023-10-10-longllmlingua|LongLLMLingua：長文コンテキスト向けプロンプト圧縮]] — 質問依存の圧縮への拡張。
- [[wiki/sources/src-2024-03-19-llmlingua-2|LLMLingua-2：タスク非依存プロンプト圧縮]] — 小型圧縮器と抽出型分類への改良。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 本プロジェクトへの適用候補の比較。

## 未解決の問い

- 日本語のチャンピオン名・アイテム名・ルーン名を含む表やJSONで、どの圧縮率まで数値と識別子を保持できるか。
- 圧縮前後のトークン数、解析精度、再現率を同一の固定データでどう評価するか。

## 出典

- 原典スナップショット：[[raw/sources/llmlingua-2310.05736.md|llmlingua-2310.05736.md]]
- 公開ページ：[LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models](https://arxiv.org/abs/2310.05736)

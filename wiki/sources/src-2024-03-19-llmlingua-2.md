---
title: "LLMLingua-2：タスク非依存プロンプト圧縮"
type: source
status: active
source_path: raw/sources/llmlingua-2-2403.12968.md
source_url: https://arxiv.org/abs/2403.12968
source_date: 2024-03-19
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - prompt-compression
  - token-efficiency
---

# LLMLingua-2：タスク非依存プロンプト圧縮

## 要約

自然言語の冗長性を利用し、LLMから知識を蒸留した小型の抽出型圧縮器を学習する研究である。圧縮をトークン分類として定式化し、双方向コンテキストを扱うTransformer encoderで重要トークンを残す。

## 主要な主張

- MeetingBank、LongBench、ZeroScrolls、GSM8K、BBHの内外データセットで、異なるLLMへの汎化を評価している。
- 既存圧縮法より圧縮器が3〜6倍高速で、2〜5倍の圧縮率ではエンドツーエンド遅延を1.6〜2.9倍改善したと報告している。
- XLM-RoBERTa-largeやmBERTなど比較的小さいモデルを圧縮器に使い、圧縮処理のオーバーヘッドを抑える設計である。

## 根拠と限界

- 原典要旨の速度・圧縮率は著者の評価条件に依存し、CPU・GPU、量子化設定、日本語データで同じ値になる保証はない。
- 抽出型圧縮は要約ではなく元入力の一部を削るため、JSON構造や表の列名を保つ制約が必要になる。
- タスク非依存を掲げるが、Wikiの実測分析に固有の指標・用語は別途検証が必要である。

## 関連ページ

- [[wiki/sources/src-2023-10-09-llmlingua|LLMLingua：LLM推論を高速化するプロンプト圧縮]] — 反復的な基礎圧縮法。
- [[wiki/sources/src-2023-10-10-longllmlingua|LongLLMLingua：長文コンテキスト向けプロンプト圧縮]] — 質問依存圧縮との比較。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — ローカル圧縮器の導入候補。

## 未解決の問い

- 日本語・ゲーム用語・数値表を含む入力で、分類器の再学習なしにどこまで忠実性を保てるか。
- 圧縮器の常駐メモリと推論時間を、llama.cpp等のローカルランタイムで測定できるか。

## 出典

- 原典スナップショット：[[raw/sources/llmlingua-2-2403.12968.md|llmlingua-2-2403.12968.md]]
- 公開ページ：[LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression](https://arxiv.org/abs/2403.12968)

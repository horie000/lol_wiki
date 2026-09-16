---
title: "PagedAttention：LLMサービングの効率的メモリ管理"
type: source
status: active
source_path: raw/sources/pagedattention-vllm-2309.06180.md
source_url: https://arxiv.org/abs/2309.06180
source_date: 2023-09-12
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - serving
  - memory-efficiency
---

# PagedAttention：LLMサービングの効率的メモリ管理

## 要約

生成中に増減するKVキャッシュをOSのページングに似た固定ブロックで管理し、vLLMサービングエンジンへ実装した研究である。リクエスト間のKV共有と細粒度の割当で、メモリ断片化と重複を抑え、バッチ処理の余地を増やす。

## 主要な主張

- PagedAttentionはKVキャッシュを非連続なメモリへ置き、リクエストごとの予約を必要最小限にする。
- vLLMはKVキャッシュの無駄をほぼゼロにし、リクエスト内・リクエスト間の共有を可能にする。
- 原典評価では、同程度の遅延で既存システムよりスループットを2〜4倍改善したと報告している。長い系列・大きいモデル・複雑なデコードほど差が大きい。

## 根拠と限界

- 主な評価対象はGPU上の多リクエストサービングであり、単一ユーザーのCPU推論やllama.cppの挙動を直接示さない。
- ブロックサイズ、スワップ、再計算などの設定には性能・断片化のトレードオフがあり、ハードウェアごとの測定が必要である。
- KVキャッシュ効率は推論メモリとスループットの改善であり、入力トークン数そのものを削減する方法ではない。

## 関連ページ

- [[wiki/sources/src-2026-09-16-llama-cpp-readme|llama.cpp README：ローカルLLM推論ランタイム]] — 単一マシンでの量子化・ハイブリッド実行。
- [[wiki/sources/src-2023-05-23-qlora|QLoRA：量子化LLMの効率的ファインチューニング]] — 学習時メモリ削減。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 推論基盤の比較。

## 未解決の問い

- 本プロジェクトのバッチ解析で、同一プロンプト接頭辞の共有がどの程度発生するか。
- vLLM（GPU）とllama.cpp（CPU・Apple Silicon等）の同一入力におけるスループット・メモリ・品質をどう比較するか。

## 出典

- 原典スナップショット：[[raw/sources/pagedattention-vllm-2309.06180.md|pagedattention-vllm-2309.06180.md]]
- 公開ページ：[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)

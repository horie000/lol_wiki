---
title: "llama.cpp README：ローカルLLM推論ランタイム"
type: source
status: active
source_path: raw/sources/llama-cpp-readme-2026-09-16.md
source_url: https://github.com/ggml-org/llama.cpp/blob/master/README.md
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - inference
  - quantization
---

# llama.cpp README：ローカルLLM推論ランタイム

## 要約

ggml上に構築されたC/C++のLLM・VLM推論ランタイムで、依存を抑えたローカル実行、複数ビット幅の量子化、CPU+GPUハイブリッド実行、CLIとOpenAI互換サーバを提供する公式READMEの取得時点スナップショットである。

## 主要な主張

- 1.5〜8ビットの整数量子化をサポートし、推論の高速化とメモリ使用量削減を狙う。
- Apple Silicon、CUDA、HIP、Metal、Vulkanなど複数バックエンドに対応し、VRAMを超えるモデルをCPU+GPUで部分的に実行できる。
- `llama cli -hf ...`でモデルを実行し、`llama serve -hf ...`でOpenAI互換APIサーバを起動するクイックスタートを示している。

## 根拠と限界

- READMEは公式の実装案内であり、査読論文の比較実験や特定ハードウェアの再現可能なベンチマークではない。
- `master`は更新されるため、取得時点のリビジョンを固定しないとコマンドや対応バックエンドが変わり得る。
- 量子化はメモリと速度を改善し得るが、品質変化・コンテキスト長・電力を本プロジェクトの入力で測定する必要がある。

## 関連ページ

- [[wiki/sources/src-2023-09-12-pagedattention|PagedAttention：LLMサービングの効率的メモリ管理]] — 多リクエストGPUサービングの別基盤。
- [[wiki/sources/src-2023-05-23-qlora|QLoRA：量子化LLMの効率的ファインチューニング]] — 量子化モデルの学習時適応。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 実行基盤候補の比較。

## 未解決の問い

- Apple Silicon上で、圧縮プロンプト・長文RAG・モデル切り替えを組み合わせたときの実効トークン毎秒とメモリ上限は何か。
- 取得するGGUFモデル、量子化幅、コンテキスト長、スレッド数をどの設定ファイルで固定し、レポートへ記録するか。

## 出典

- 原典スナップショット：[[raw/sources/llama-cpp-readme-2026-09-16.md|llama-cpp-readme-2026-09-16.md]]
- 公開ページ：[ggml-org/llama.cpp README](https://github.com/ggml-org/llama.cpp/blob/master/README.md)

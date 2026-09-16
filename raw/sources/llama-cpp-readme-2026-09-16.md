---
title: "llama.cpp README"
source_type: official-project-documentation
source_url: https://github.com/ggml-org/llama.cpp/blob/master/README.md
retrieved: 2026-09-16
revision: master（取得時点）
capture_type: selected-excerpts
---

# llama.cpp README

## Metadata

- Project: ggml-org/llama.cpp
- Document: README.md（取得時点の `master`）
- License and revision detailsは上流リポジトリを参照する。

## Selected excerpts（原文）

> The main goal of `llama.cpp` is to enable LLM (and VLM) inference with minimal setup and state-of-the-art performance on a wide range of hardware - locally and in the cloud.

- Plain C/C++ implementation without any dependencies.
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use.
- CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity.
- Quick-start commands include `llama cli -hf ...` for direct model execution and `llama serve -hf ...` for an OpenAI-compatible API server.
- Apple Silicon、CUDA、HIP、Metal、Vulkanなど複数のバックエンドを表にしている。

## Capture note

- READMEは更新される公式文書であるため、再現時は保存日と上流コミットを確認する。本ファイルは全READMEの複製ではなく、ローカル推論運用に関係する箇所の抜粋である。

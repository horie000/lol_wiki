---
title: "RouteLLM: Learning to Route LLMs with Preference Data"
source_type: research-paper
source_url: https://arxiv.org/abs/2406.18665
source_date: 2024-06-26
retrieved: 2026-09-16
capture_type: abstract-and-metadata
---

# RouteLLM: Learning to Route LLMs with Preference Data

## Metadata

- Authors: Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez, M Waleed Kadous, Ion Stoica
- arXiv: 2406.18665
- Code and preference data: https://github.com/lm-sys/RouteLLM

## Abstract（原文）

Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost. More powerful models, though effective, come with higher expenses, while less capable models are more cost-effective. To address this dilemma, we propose several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality. We develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance. Our evaluation on widely-recognized benchmarks shows that our approach significantly reduces costs-by over 2 times in certain cases-without compromising the quality of responses. Interestingly, our router models also demonstrate significant transfer learning capabilities, maintaining their performance even when the strong and weak models are changed at test time. This highlights the potential of these routers to provide a cost-effective yet high-performance solution for deploying LLMs.

## Capture note

- 本ファイルは原典の書誌情報と公開要旨を保存したスナップショットであり、本文全体の代替ではない。

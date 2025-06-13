<h1>Weaviate <img alt='Weaviate logo' src='https://weaviate.io/img/site/weaviate-logo-light.png' width='148' align='right' /></h1>

[![Go Reference](https://pkg.go.dev/badge/github.com/weaviate/weaviate.svg)](https://pkg.go.dev/github.com/weaviate/weaviate)
[![Build Status](https://github.com/weaviate/weaviate/actions/workflows/.github/workflows/pull_requests.yaml/badge.svg?branch=main)](https://github.com/weaviate/weaviate/actions/workflows/.github/workflows/pull_requests.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/weaviate/weaviate)](https://goreportcard.com/report/github.com/weaviate/weaviate)
[![Coverage Status](https://codecov.io/gh/weaviate/weaviate/branch/main/graph/badge.svg)](https://codecov.io/gh/weaviate/weaviate)
[![Slack](https://img.shields.io/badge/slack--channel-blue?logo=slack)](https://weaviate.io/slack)
[![GitHub Tutorials](https://img.shields.io/badge/Weaviate_Tutorials-green)](https://github.com/weaviate-tutorials/)

## Overview

Weaviate is a cloud-native, **open source vector database** that is robust, fast, and scalable.

To get started quickly, have a look at one of these pages:

- [Quickstart tutorial](https://weaviate.io/developers/weaviate/quickstart) To see Weaviate in action
- [Contributor guide](https://weaviate.io/developers/contributor-guide) To contribute to this project

For more details, read through the summary on this page or see the system [documentation](https://weaviate.io/developers/weaviate/).

---

## Why Weaviate?

Weaviate uses state-of-the-art machine learning (ML) models to turn your data - text, images, and more - into a searchable vector database.

Here are some highlights.

### Speed

Weaviate is fast. The core engine can run a 10-NN nearest neighbor search on millions of objects in milliseconds. See [benchmarks](https://weaviate.io/developers/weaviate/benchmarks).

### Flexibility

Weaviate can **vectorize your data at import time**. Or, if you have already vectorized your data, you can **upload your own vectors** instead.

Modules give you the flexibility to tune Weaviate for your needs. More than two dozen modules connect you to popular services and model hubs such as [OpenAI](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-openai), [Cohere](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-cohere), [VoyageAI](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-voyageai) and [HuggingFace](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-huggingface). Use custom modules to work with your own models or third party services.

### Production-readiness


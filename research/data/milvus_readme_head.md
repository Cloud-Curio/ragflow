<img src="https://github.com/user-attachments/assets/51e33300-7f85-43ff-a05a-3a0317a961f3" alt="milvus banner">

<div class="column" align="middle">
  <a href="https://github.com/milvus-io/milvus/blob/master/LICENSE"><img height="20" src="https://img.shields.io/github/license/milvus-io/milvus" alt="license"/></a>
  <a href="https://milvus.io/docs/install_standalone-docker.md"><img src="https://img.shields.io/docker/pulls/milvusdb/milvus" alt="docker-pull-count"/></a>
  <a href="https://milvus.io/docs/roadmap.md"><img src="https://img.shields.io/badge/2025-roadmap-orange" alt="fully-managed-milvus"/></a>
  <a href="https://cloud.zilliz.com/signup?utm_source=partner&utm_medium=referral&utm_campaign=2024-11-04_web_github-readme_global"><img src="https://img.shields.io/badge/fully_managed-milvus-blue" alt="fully-managed-milvus"/></a>
  <a href="https://milvus.io/docs/tutorials-overview.md"><img src="https://img.shields.io/badge/tutorials-green" alt="tutorials"/></a>
  <a href="https://discord.gg/mKc3R95yE5"><img height="20" src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" alt="discord"/></a>
  <a href="https://x.com/milvusio"><img src="https://img.shields.io/twitter/follow/milvusio" alt="twitter"/></a>
</div>

## What is Milvus?

🐦 [Milvus](https://milvus.io/) is a high-performance vector database built for scale. It powers AI applications by efficiently organizing and searching vast amounts of unstructured data, such as text, images, and multi-modal information.

🧑‍💻 Written in Go and C++, Milvus implements hardware accelaration for CPU/GPU to achieve best-in-class vector search performance. Thanks to its [fully-distributed and K8s-native architecture](https://milvus.io/docs/overview.md#What-Makes-Milvus-so-Scalable), Milvus can scale horizontally, handle tens of thousands of search queries on billions of vectors, and keep data fresh with real-time streaming updates. Milvus also supports [Standalone mode](https://milvus.io/docs/install_standalone-docker.md) for single machine deployment. [Milvus Lite](https://milvus.io/docs/milvus_lite.md) is a lightweight version good for quickstart in python with `pip install`.

Want to use Milvus with zero setup? Try out [Zilliz Cloud ☁️](https://cloud.zilliz.com/signup?utm_source=partner&utm_medium=referral&utm_campaign=2024-11-04_web_github-readme_global) for free. Milvus is available as a fully managed service on Zilliz Cloud, with [Serverless](https://zilliz.com/serverless?utm_source=partner&utm_medium=referral&utm_campaign=2024-11-04_web_github-readme_global), [Dedicated](https://zilliz.com/cloud?utm_source=partner&utm_medium=referral&utm_campaign=2024-11-04_web_github-readme_global) and [BYOC](https://zilliz.com/bring-your-own-cloud?utm_source=partner&utm_medium=referral&utm_campaign=2024-11-04_web_github-readme_global) options available.

For questions about how to use Milvus, join the community on [Discord](https://discord.gg/33mfvwep3J) to get help. For reporting problems, file bugs and feature requests in GitHub [Issues](https://github.com/milvus-io/milvus/issues) or ask in [Discussions](https://github.com/milvus-io/milvus/discussions).

The Milvus open-source project is
under [LF AI & Data Foundation](https://lfaidata.foundation/projects/milvus/), distributed with [Apache 2.0](https://github.com/milvus-io/milvus/blob/master/LICENSE) License, with Zilliz as its major contributor.

## Quickstart

```python
$ pip install -U pymilvus
```
This installs `pymilvus`, the Python SDK for Milvus. Use `MilvusClient` to create a client:
```python
from pymilvus import MilvusClient
```

* `pymilvus` also includes Milvus Lite for quickstart. To create a local vector database, simply instantiate a client with a local file name for persisting data:

  ```python
  client = MilvusClient("milvus_demo.db")
  ```

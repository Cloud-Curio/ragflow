# Faiss

Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. Some of the most useful algorithms are implemented on the GPU. It is developed primarily at Meta's [Fundamental AI Research](https://ai.facebook.com/) group.

## News

See [CHANGELOG.md](CHANGELOG.md) for detailed information about latest features.

## Introduction

Faiss contains several methods for similarity search. It assumes that the instances are represented as vectors and are identified by an integer, and that the vectors can be compared with L2 (Euclidean) distances or dot products. Vectors that are similar to a query vector are those that have the lowest L2 distance or the highest dot product with the query vector. It also supports cosine similarity, since this is a dot product on normalized vectors.

Some of the methods, like those based on binary vectors and compact quantization codes, solely use a compressed representation of the vectors and do not require to keep the original vectors. This generally comes at the cost of a less precise search but these methods can scale to billions of vectors in main memory on a single server. Other methods, like HNSW and NSG add an indexing structure on top of the raw vectors to make searching more efficient.

The GPU implementation can accept input from either CPU or GPU memory. On a server with GPUs, the GPU indexes can be used a drop-in replacement for the CPU indexes (e.g., replace `IndexFlatL2` with `GpuIndexFlatL2`) and copies to/from GPU memory are handled automatically. Results will be faster however if both input and output remain resident on the GPU. Both single and multi-GPU usage is supported.

## Installing

Faiss comes with precompiled libraries for Anaconda in Python, see [faiss-cpu](https://anaconda.org/pytorch/faiss-cpu), [faiss-gpu](https://anaconda.org/pytorch/faiss-gpu) and [faiss-gpu-cuvs](https://anaconda.org/pytorch/faiss-gpu-cuvs). The library is mostly implemented in C++, the only dependency is a [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) implementation. Optional GPU support is provided via CUDA or AMD ROCm, and the Python interface is also optional. The backend GPU implementations of NVIDIA [cuVS](https://github.com/rapidsai/cuvs) can also be enabled optionally. It compiles with cmake. See [INSTALL.md](INSTALL.md) for details.

## How Faiss works

Faiss is built around an index type that stores a set of vectors, and provides a function to search in them with L2 and/or dot product vector comparison. Some index types are simple baselines, such as exact search. Most of the available indexing structures correspond to various trade-offs with respect to

- search time
- search quality
- memory used per index vector
- training time
- adding time
- need for external data for unsupervised training

The optional GPU implementation provides what is likely (as of March 2017) the fastest exact and approximate (compressed-domain) nearest neighbor search implementation for high-dimensional vectors, fastest Lloyd's k-means, and fastest small k-selection algorithm known. [The implementation is detailed here](https://arxiv.org/abs/1702.08734).

## Full documentation of Faiss

The following are entry points for documentation:

- the full documentation can be found on the [wiki page](http://github.com/facebookresearch/faiss/wiki), including a [tutorial](https://github.com/facebookresearch/faiss/wiki/Getting-started), a [FAQ](https://github.com/facebookresearch/faiss/wiki/FAQ) and a [troubleshooting section](https://github.com/facebookresearch/faiss/wiki/Troubleshooting)
- the [doxygen documentation](https://faiss.ai/) gives per-class information extracted from code comments
- to reproduce results from our research papers, [Polysemous codes](https://arxiv.org/abs/1609.01882) and [Billion-scale similarity search with GPUs](https://arxiv.org/abs/1702.08734), refer to the [benchmarks README](benchs/README.md). For [

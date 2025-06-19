RAG Database Data Collection
===========================

This directory contains a small sample dataset of open-source resources related to retrieval-augmented generation (RAG), LLM agents, and vector databases. The data was collected using `curl` commands from public repositories and APIs. Each file contains the first 40 lines (or API response) from its respective source.

Files:
- `data/semantic_scholar_rag.json`: Search results for "retrieval augmented generation" from Semantic Scholar (limit 5).
- `data/qdrant_readme_head.md`: Beginning of the Qdrant vector database README.
- `data/langchain_readme_head.md`: Intro to the LangChain framework.
- `data/llamaindex_readme_head.md`: Intro to the LlamaIndex RAG framework.
- `data/weaviate_readme_head.md`: Intro to the Weaviate vector database.
- `data/transformers_readme_head.md`: Beginning of Hugging Face Transformers README.
- `data/pinecone_readme_head.md`: Example repo README for Pinecone.
- `data/openai_cookbook_readme_head.md`: Intro to the OpenAI Cookbook examples.
- `data/autogen_readme_head.md`: Microsoft AutoGen multi-agent framework intro.
- `data/langgraph_readme_head.md`: LangGraph agent orchestration framework intro.
- `data/chroma_readme_head.md`: Intro to the Chroma vector store.
- `data/milvus_readme_head.md`: Intro to the Milvus vector database.
- `data/unstructured_readme_head.md`: Unstructured document processing toolkit README.
- `data/faiss_readme_head.md`: Intro to Facebook's FAISS similarity search library.

These files can be ingested into a local vector database as a starter knowledge base for building RAG or agentic applications.

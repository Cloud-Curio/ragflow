<p align="center">
  <a href="https://trychroma.com"><img src="https://user-images.githubusercontent.com/891664/227103090-6624bf7d-9524-4e05-9d2c-c28d5d451481.png" alt="Chroma logo"></a>
</p>

<p align="center">
    <b>Chroma - the open-source embedding database</b>. <br />
    The fastest way to build Python or JavaScript LLM apps with memory!
</p>

<p align="center">
  <a href="https://discord.gg/MMeYNTmh3x" target="_blank">
      <img src="https://img.shields.io/discord/1073293645303795742?cacheSeconds=3600" alt="Discord">
  </a> |
  <a href="https://github.com/chroma-core/chroma/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/static/v1?label=license&message=Apache 2.0&color=white" alt="License">
  </a> |
  <a href="https://docs.trychroma.com/" target="_blank">
      Docs
  </a> |
  <a href="https://www.trychroma.com/" target="_blank">
      Homepage
  </a>
</p>


```bash
pip install chromadb # python client
# for javascript, npm install chromadb!
# for client-server mode, chroma run --path /chroma_db_path
```

The core API is only 4 functions (run our [💡 Google Colab](https://colab.research.google.com/drive/1QEzFyqnoFxq7LUGyP1vzR4iLt9PpCDXv?usp=sharing) or [Replit template](https://replit.com/@swyx/BasicChromaStarter?v=1)):

```python
import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

#!/usr/bin/env python3
"""Simple data pipeline to ingest documents from govinfo endpoints."""
import os
import tempfile
import requests
import zipfile
from pathlib import Path

from sentence_transformers import SentenceTransformer
import chromadb

# Setup embedding model and vector DB
EMBED_MODEL = os.environ.get("EMBED_MODEL", "all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection("govinfo")
model = SentenceTransformer(EMBED_MODEL)


def fetch_bulkdata(collection_id: str, congress: str, dest: Path) -> Path:
    """Download a sample bulkdata file."""
    url = f"https://www.govinfo.gov/bulkdata/{collection_id}/{congress}"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    dest.mkdir(parents=True, exist_ok=True)
    fp = dest / f"{collection_id}_{congress}.zip"
    with open(fp, "wb") as f:
        f.write(r.content)
    # Extract if zip
    with zipfile.ZipFile(fp, "r") as z:
        z.extractall(dest)
    return dest


def fetch_api_package(package_id: str, api_key: str, dest: Path) -> Path:
    url = f"https://api.govinfo.gov/packages/{package_id}?api_key={api_key}"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    dest.mkdir(parents=True, exist_ok=True)
    fp = dest / f"{package_id}.json"
    with open(fp, "wb") as f:
        f.write(r.content)
    return fp


def ingest_text(text: str, meta: dict):
    embedding = model.encode(text)
    collection.add(documents=[text], metadatas=[meta], ids=[meta.get("id")])


def main():
    api_key = os.environ.get("GOVINFO_API_KEY", "DEMO_KEY")
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        try:
            bulk_path = fetch_bulkdata("BILLSTATUS", "118", td_path)
            print(f"Downloaded bulk data to {bulk_path}")
        except Exception as e:
            print(f"Bulkdata fetch failed: {e}")
        try:
            pkg = fetch_api_package("BILLS-118hr1", api_key, td_path)
            print(f"Downloaded api package to {pkg}")
        except Exception as e:
            print(f"API fetch failed: {e}")
        for fp in td_path.rglob("*"):
            if fp.suffix in {".xml", ".txt", ".json"}:
                try:
                    text = fp.read_text(encoding="utf-8", errors="ignore")
                    ingest_text(text, {"id": fp.name})
                except Exception as e:
                    print(f"Failed ingest {fp}: {e}")
        print(f"Indexed {collection.count()} documents")


if __name__ == "__main__":
    main()

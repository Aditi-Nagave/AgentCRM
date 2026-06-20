# app/services/rag/index_builder.py
from pathlib import Path

from sentence_transformers import SentenceTransformer

from app.services.rag.vector_store import collection

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

KNOWLEDGE_DIR = Path(
    "app/knowledge"
)


def build_index():

    try:
        ids = collection.get()["ids"]

        if ids:
            collection.delete(
                ids=ids
            )

    except Exception as e:
        print("Cleanup skipped:", e)



    for file in KNOWLEDGE_DIR.glob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        embedding = model.encode(
            text
        ).tolist()

        collection.add(
            ids=[file.stem],
            documents=[text],
            embeddings=[embedding]
        )

    print("Knowledge Index Built")


if __name__ == "__main__":
    build_index()
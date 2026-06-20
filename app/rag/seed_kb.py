# app/rag/index_builder.py
from pathlib import Path

from app.rag.chunker import (
    chunk_text
)

from app.rag.embeddings import (
    generate_embedding
)

from app.rag.vector_store import (
    collection
)

KNOWLEDGE_DIR = Path(
    "app/knowledge"
)


def seed_knowledge_base():

    try:

        ids = collection.get()["ids"]

        if ids:

            collection.delete(
                ids=ids
            )

    except:
        pass

    for file in KNOWLEDGE_DIR.glob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):

            collection.add(

                ids=[
                    f"{file.stem}_{idx}"
                ],

                documents=[
                    chunk
                ],

                metadatas=[
                    {
                        "source":
                        file.stem
                    }
                ],

                embeddings=[
                    generate_embedding(
                        chunk
                    )
                ]
            )

    print("Knowledge Base Seeded")


if __name__ == "__main__":

    seed_knowledge_base()
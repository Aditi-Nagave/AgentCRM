# app/services/rag/retriever.py
from sentence_transformers import SentenceTransformer

from app.services.rag.vector_store import (
    collection
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_knowledge(
        query,
        top_k=3
):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    docs = results["documents"][0]

    return "\n\n".join(docs)
# app/rag/retriever.py
from app.rag.embeddings import (
    generate_embedding
)

from app.rag.vector_store import (
    collection
)


def retrieve_knowledge(
        query,
        top_k=3
):

    embedding = generate_embedding(
        query
    )

    results = collection.query(

        query_embeddings=[
            embedding
        ],

        n_results=top_k
    )

    docs = results["documents"][0]

    return "\n\n".join(docs)


def search_policies(
        query,
        top_k=5
):

    embedding = generate_embedding(
        query
    )

    results = collection.query(

        query_embeddings=[
            embedding
        ],

        n_results=top_k
    )

    output = []

    for i in range(
        len(results["ids"][0])
    ):

        output.append({

            "source":
            results["metadatas"][0][i]["source"],

            "distance":
            round(
                results["distances"][0][i],
                4
            )
        })

    return output
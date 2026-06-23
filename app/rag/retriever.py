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

    REFUND_KEYWORDS = [

        "refund",

        "cancel",

        "review",

        "angry",

        "churn"
    ]

    query_lower = query.lower()

    if any(
        keyword in query_lower
        for keyword in REFUND_KEYWORDS
    ):

        boosted_docs = [

            "refund_policy",

            "escalation_matrix"
        ]

    else:

        boosted_docs = []

    embedding = generate_embedding(
        query
    )

    results = collection.query(

        query_embeddings=[
            embedding
        ],

        n_results=top_k
    )

    documents = results["documents"][0]

    metadata = results["metadatas"][0]

    output = []

    for i in range(len(documents)):

        output.append({

            "source":
            metadata[i]["source"],

            "chunk":
            documents[i]
        })

    # Karen Refund Scenario Boost
    for doc in reversed(boosted_docs):

        output.insert(
            0,
            {
                "source": doc,
                "chunk": f"BOOSTED:{doc}"
            }
        )

    return output


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

        distance = results["distances"][0][i]

        similarity = max(0,round(1 / (1 + distance),4))

        output.append({
             "source": results["metadatas"][0][i]["source"],
             "similarity_score": similarity,
            "chunk": results["documents"][0][i]
        })

    return output
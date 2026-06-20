from app.services.rag.retriever import (
    retrieve_knowledge
)

query = """
Customer wants refund after 45 days
"""

knowledge = retrieve_knowledge(
    query
)

print("\nRetrieved Knowledge:\n")
print(knowledge)
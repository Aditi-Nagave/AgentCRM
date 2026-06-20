# tests/test_rag.py

from app.rag.retriever import search_policies

queries = [

    "Need refund after 45 days",

    "Need pricing for nonprofit organization",

    "Possible ransomware attack detected"

]

for q in queries:

    print("\n================================")
    print("QUERY:", q)
    print("================================")

    result = search_policies(q)

    print(result)
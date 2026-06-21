# app/rag/citation_helper.py
def format_citations(results):

    sources = []

    for item in results:

        source = item["source"]

        if source not in sources:

            sources.append(source)

    return "\n".join(
        [
            f"[Policy Source: {s}]"
            for s in sources
        ]
    )
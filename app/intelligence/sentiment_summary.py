# app/intelligence/sentiment_summary.py
def summarize_reviews(data):

    themes = []

    for source in data:

        if not source:
            continue

        themes.extend(
            source.get(
                "themes",
                []
            )
        )

    return {

        "common_complaints":
        list(set(themes))
    }
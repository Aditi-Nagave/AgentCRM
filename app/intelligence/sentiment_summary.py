# app/intelligence/sentiment_summary.py
def summarize_reviews(data):

    themes = []

    for item in data:

        if isinstance(item, list):

            for source in item:

                themes.extend(
                source.get(
                    "themes",
                    []
                )
            )

        elif item:

            themes.extend(
            item.get(
                "themes",
                []
            )
        )

    return {

        "common_complaints":
        list(set(themes))
    }
# app/intelligence/sentiment_summary.py
def summarize_reviews(data):

    keywords = []

    for item in data:

        if item.get("status") == "success":

            keywords.extend(

                item.get(
                    "content",
                    []
                )
            )

    return {

        "total_sources":
        len(data),

        "content_found":
        len(keywords)
    }

    return {

        "common_complaints":
        list(set(themes))
    }
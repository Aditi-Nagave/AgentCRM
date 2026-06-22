# app/intelligence/trigger_detector.py
TRIGGER_WORDS = [

    "review",
    "trustpilot",
    "g2",
    "twitter",
    "post publicly",
    "public review"
]


def should_fetch_intelligence(
    category,
    urgency,
    sentiment_score,
    subject,
    body
):

    text = (
        subject + " " + body
    ).lower()

    for word in TRIGGER_WORDS:

        if word in text:
            return True

    if sentiment_score < -0.6:
        return True

    if (
        category == "Complaint"
        and urgency in ["High", "Critical"]
    ):
        return True

    return False
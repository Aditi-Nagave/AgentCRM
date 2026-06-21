# app/services/spam_detector.py
from app.services.sender_reputation import (
    sender_reputation
)

SPAM_KEYWORDS = [

    "inheritance",

    "million usd",

    "claim your share",

    "seo",

    "click here",

    "limited offer"
]


def detect_spam(
    sender,
    subject,
    body
):

    text = (

        subject + " " + body

    ).lower()

    for keyword in SPAM_KEYWORDS:

        if keyword in text:

            return True

    if sender_reputation(sender) == "Bad":

        return True

    return False
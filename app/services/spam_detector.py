# app/services/spam_detector.py
SPAM_KEYWORDS = [
    "inheritance",
    "million usd",
    "claim your share",
    "seo",
    "click here",
    "limited offer"
]

def detect_spam(subject, body):

    text = (subject + " " + body).lower()

    for word in SPAM_KEYWORDS:

        if word in text:
            return True

    return False
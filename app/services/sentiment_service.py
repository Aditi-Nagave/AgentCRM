# app/services/sentiment_service.py
from textblob import TextBlob

def analyze_sentiment(text):

    score = TextBlob(text).sentiment.polarity

    if score > 0.2:
        label = "Positive"

    elif score < -0.2:
        label = "Negative"

    else:
        label = "Neutral"

    return {
        "label": label,
        "score": score
    }
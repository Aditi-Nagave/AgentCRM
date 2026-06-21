# app/services/sentiment_trend_service.py
from app.models.email import Email


def get_sender_trend(
    db,
    sender,
    days=30
):

    emails = (

        db.query(Email)

        .filter(
            Email.sender == sender
        )

        .order_by(
            Email.timestamp
        )

        .all()
    )

    return [

        {

            "date": e.timestamp,

            "score": e.sentiment_score

        }

        for e in emails
    ]


def has_negative_trend(
    db,
    sender
):

    emails = (

        db.query(Email)

        .filter(
            Email.sender == sender
        )

        .order_by(
            Email.timestamp.desc()
        )

        .limit(3)

        .all()
    )

    if len(emails) < 3:

        return False

    return all(

        e.sentiment_score < 0

        for e in emails
    )
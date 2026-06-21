# app/services/validation_service.py
import html
import re

MAX_BODY_LENGTH = 10000


def validate_email_payload(subject, body):

    if not subject or not subject.strip():
        raise ValueError(
            "Subject cannot be empty"
        )

    if not body or not body.strip():
        raise ValueError(
            "Body cannot be empty"
        )

    cleaned = html.unescape(body)

    cleaned = re.sub(
        r"<[^>]+>",
        "",
        cleaned
    )

    if not cleaned.strip():
        raise ValueError(
            "Body contains only HTML entities"
        )

    return True


def truncate_body(body):

    if len(body) > MAX_BODY_LENGTH:

        return body[:MAX_BODY_LENGTH]

    return body
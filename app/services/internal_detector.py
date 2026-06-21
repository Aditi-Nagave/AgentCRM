# app/services/internal_detector.py
INTERNAL_DOMAINS = [
    "@internal.com",
    "@mycompany.com"
]


def is_internal_email(
    email
):

    email = email.lower()

    return any(
        domain in email
        for domain
        in INTERNAL_DOMAINS
    )
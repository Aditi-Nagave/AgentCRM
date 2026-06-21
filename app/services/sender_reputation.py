# app/services/sender_reputation.py
BAD_DOMAINS = [

    "spam-domain.com",

    "fake-offers.net"
]


def sender_reputation(email):

    domain = email.split("@")[-1]

    if domain in BAD_DOMAINS:

        return "Bad"

    return "Good"
# app/services/entity_extractor.py
import re


def extract_entities(text):

    money = re.findall(
        r"\$[\d,]+",
        text
    )

    ticket_ids = re.findall(
        r"TICKET-\d+",
        text,
        re.IGNORECASE
    )

    order_ids = re.findall(
        r"ORD-\d+",
        text,
        re.IGNORECASE
    )

    deadlines = re.findall(
        r"\d{1,2}/\d{1,2}/\d{4}",
        text
    )

    return {

        "order_ids": order_ids,

        "ticket_ids": ticket_ids,

        "monetary_amounts": money,

        "deadlines": deadlines,

        "products_mentioned": []
    }
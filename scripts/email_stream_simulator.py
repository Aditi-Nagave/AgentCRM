# scripts/email_stream_simulator.py
import json
import requests
import time

with open(
    "data/email-data-advanced.json",
    "r"
) as file:

    emails = json.load(file)

for email in emails:

    requests.post(
        "http://localhost:8000/api/ingest",
        json=email
    )

    print(email["message_id"])

    time.sleep(1)
# scripts/email_stream_simulator.py
import json
import time
import requests

URL = "http://localhost:8000/api/ingest"

with open(
    "data/email-data-advanced.json",
    "r",
    encoding="utf-8"
) as f:

    emails = json.load(f)

for email in emails:

    try:

        response = requests.post(
            URL,
            json=email
        )

        print(
            response.json()
        )

    except Exception as e:

        print(e)

    time.sleep(1)
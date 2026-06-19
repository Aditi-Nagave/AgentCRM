import requests
import time

BASE_URL = "http://localhost:8000"

emails = [

{
    "message_id":"t1",
    "sender":"alice@company.com",
    "subject":"Need nonprofit pricing",
    "body":"We are evaluating your product and need nonprofit pricing details.",
    "timestamp":"2026-06-20T10:00:00",
    "thread_id":"pricing_thread_1"
},

{
    "message_id":"t2",
    "sender":"alice@company.com",
    "subject":"Proceeding with purchase",
    "body":"Our management approved the purchase.",
    "timestamp":"2026-06-20T10:05:00",
    "thread_id":"pricing_thread_1"
},

{
    "message_id":"t3",
    "sender":"alice@company.com",
    "subject":"Need 200 more seats",
    "body":"We need to add 200 more users to our subscription.",
    "timestamp":"2026-06-20T10:10:00",
    "thread_id":"pricing_thread_1"
}

]

for email in emails:

    response = requests.post(
        f"{BASE_URL}/api/ingest",
        json=email
    )

    print(response.json())

    time.sleep(2)

print("\nFetching Thread...\n")

thread = requests.get(
    f"{BASE_URL}/threads/alice@company.com"
)

for mail in thread.json():

    print(
        mail["subject"],
        "->",
        mail["customer_stage"]
    )
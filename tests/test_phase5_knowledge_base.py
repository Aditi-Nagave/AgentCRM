import requests
import time

BASE_URL = "http://localhost:8000"

emails = [

    {
        "message_id": "kb_001",
        "sender": "customer@test.com",
        "subject": "Refund Request",
        "body": "I purchased the software 45 days ago and would like a refund.",
        "timestamp": "2026-06-20T10:00:00",
        "thread_id": "refund_thread"
    },

    {
        "message_id": "kb_002",
        "sender": "ngo@test.com",
        "subject": "Need Pricing Information",
        "body": "We are a nonprofit organization and need pricing details.",
        "timestamp": "2026-06-20T10:05:00",
        "thread_id": "pricing_thread"
    },

    {
        "message_id": "kb_003",
        "sender": "security@test.com",
        "subject": "Possible Data Breach",
        "body": "We suspect customer data has been exposed. Please investigate.",
        "timestamp": "2026-06-20T10:10:00",
        "thread_id": "security_thread"
    }
]

print("\nLoading test emails...\n")

for email in emails:

    response = requests.post(
        f"{BASE_URL}/api/ingest",
        json=email
    )

    print(response.json())

    time.sleep(2)

print("\nFetching results...\n")

for sender in [
    "customer@test.com",
    "ngo@test.com",
    "security@test.com"
]:

    response = requests.get(
        f"{BASE_URL}/threads/{sender}"
    )

    data = response.json()

    print("\n==============================")
    print(sender)
    print("==============================")

    for email in data:

        print(
            f"""
Subject: {email['subject']}
Category: {email.get('category')}
Stage: {email.get('customer_stage')}
Urgency: {email.get('urgency')}
Action: {email.get('recommended_action')}
Knowledge Used: {email.get('knowledge_used')}
Confidence: {email.get('confidence')}
"""
        )
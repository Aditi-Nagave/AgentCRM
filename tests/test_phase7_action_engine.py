import requests

BASE_URL = "http://127.0.0.1:8000"

emails = [

    {
        "message_id": "phase7_refund_001",
        "sender": "customer@test.com",
        "subject": "Need refund after 45 days",
        "body": "I purchased the product 45 days ago and would like a refund.",
        "timestamp": "2026-01-10T10:00:00",
        "thread_id": "refund_thread"
    },

    {
        "message_id": "phase7_pricing_001",
        "sender": "ngo@test.com",
        "subject": "Need pricing for nonprofit organization",
        "body": "We are a nonprofit organization and need pricing details.",
        "timestamp": "2026-01-10T10:05:00",
        "thread_id": "pricing_thread"
    },

    {
        "message_id": "phase7_security_001",
        "sender": "security@test.com",
        "subject": "Possible ransomware attack detected",
        "body": "Our systems may be affected by ransomware.",
        "timestamp": "2026-01-10T10:10:00",
        "thread_id": "security_thread"
    }
]

print("\nLoading Emails...\n")

for email in emails:

    response = requests.post(
        f"{BASE_URL}/api/ingest",
        json=email
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

print("\nFetching Results...\n")

for sender in [

    "customer@test.com",
    "ngo@test.com",
    "security@test.com"

]:

    response = requests.get(
        f"{BASE_URL}/threads/{sender}"
    )

    data = response.json()

    latest = data[-1]

    print("\n================================")
    print(sender)
    print("================================")

    print(f"""
Subject:
{latest['subject']}

Category:
{latest['category']}

Customer Stage:
{latest['customer_stage']}

Action:
{latest['recommended_action']}

Draft Reply:
{latest['draft_reply']}

Knowledge Used:
{latest['knowledge_used']}
""")
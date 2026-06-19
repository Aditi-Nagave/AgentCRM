import requests

BASE_URL = "http://localhost:8000"

emails = [

{
    "message_id":"spam_001",
    "sender":"spam@test.com",
    "subject":"Claim Your Share",
    "body":"You inherited 10 million USD. Click here now.",
    "timestamp":"2026-06-20T10:00:00",
    "thread_id":"spam_thread"
},

{
    "message_id":"security_001",
    "sender":"security@test.com",
    "subject":"Data Breach Alert",
    "body":"A ransomware attack has exposed customer data.",
    "timestamp":"2026-06-20T10:01:00",
    "thread_id":"security_thread"
},

{
    "message_id":"urgent_001",
    "sender":"ops@test.com",
    "subject":"Production Down",
    "body":"Urgent. Production down. SLA breach imminent.",
    "timestamp":"2026-06-20T10:02:00",
    "thread_id":"ops_thread"
}

]

for email in emails:

    response = requests.post(
        f"{BASE_URL}/api/ingest",
        json=email
    )

    print(response.json())

print("\nCheck:")
print("GET /threads/spam@test.com")
print("GET /threads/security@test.com")
print("GET /threads/ops@test.com")
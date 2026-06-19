import requests

BASE_URL = "http://localhost:8000"

payload = {
    "message_id": "phase1_001",
    "sender": "john@test.com",
    "subject": "Login Issue",
    "body": "I cannot login to my account.",
    "timestamp": "2026-06-20T10:00:00",
    "thread_id": "thread_1"
}

response = requests.post(
    f"{BASE_URL}/api/ingest",
    json=payload
)

print(response.json())
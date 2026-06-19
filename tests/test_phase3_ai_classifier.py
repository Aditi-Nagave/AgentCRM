import requests

BASE_URL = "http://localhost:8000"

payload = {

    "message_id":"ai_001",

    "sender":"customer@test.com",

    "subject":"Very disappointed",

    "body":"I requested a refund three times. Nobody replied and I will post a negative review.",

    "timestamp":"2026-06-20T10:00:00",

    "thread_id":"ai_thread"
}

response = requests.post(
    f"{BASE_URL}/api/ingest",
    json=payload
)

print(response.json())

thread = requests.get(
    f"{BASE_URL}/threads/customer@test.com"
)

print("\nStored Email:")
print(thread.json())
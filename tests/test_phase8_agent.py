import requests

response = requests.post(

    "http://127.0.0.1:8000/agent/dry-run/1"
)

print(response.json())
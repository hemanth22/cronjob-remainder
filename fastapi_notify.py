import requests
import json
import os


FASTAPI_WEBHOOK = os.environ.get('FASTAPI_WEBHOOK')

payload = json.dumps({
  "source": "circleci",
  "message": "Remainder to book a cab"
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", FASTAPI_WEBHOOK, headers=headers, data=payload)

print(response.text)

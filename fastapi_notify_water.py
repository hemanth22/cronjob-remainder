import requests
import json
import os


FASTAPI_WEBHOOK_SERVERLESS = os.environ.get('FASTAPI_WEBHOOK_SERVERLESS')

payload = json.dumps({
  "source": "circleci",
  "message": "Drink plenty of water"
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", FASTAPI_WEBHOOK_SERVERLESS, headers=headers, data=payload)

print(response.text)

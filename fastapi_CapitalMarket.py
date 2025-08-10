import requests
import json
import os
import logging

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

FASTAPI_WEBHOOK_SERVERLESS = os.environ.get('FASTAPI_WEBHOOK_SERVERLESS')

payload = json.dumps({
  "source": "circleci",
  "message": "Check capitalmarkets.com for the latest stock market news",
})
headers = {
  'Content-Type': 'application/json',
}

logger.debug(f"Payload: {payload}")
logger.debug(f"Headers: {headers}")

response = requests.request("POST", FASTAPI_WEBHOOK_SERVERLESS, headers=headers, data=payload)

logger.debug(f"Response: {response.text}")
print(response.text)

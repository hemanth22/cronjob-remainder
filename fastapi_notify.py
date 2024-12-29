import requests
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

FASTAPI_WEBHOOK = os.environ.get('FASTAPI_WEBHOOK')

payload = json.dumps({
    'source': 'github',
    'message': 'Reminder to book a cab'
})
headers = {
    'Content-Type': 'application/json',
}

logger.debug('Payload prepared: %s', payload)

try:
    logger.info('Sending POST request to webhook')
    response = requests.post(FASTAPI_WEBHOOK, headers=headers, data=payload)
    response.raise_for_status()  # Check for HTTP errors
    logger.info('Response status code: %s', response.status_code)
    logger.debug('Response content: %s', response.text)
except requests.exceptions.RequestException as e:
    logger.error('Request failed: %s', e)
    if e.response is not None:
        logger.warning('Response content: %s', e.response.text)

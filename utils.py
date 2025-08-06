
import requests

TOKEN_URL = "https://vaspp-ai-usecases-acvc7v2w.authentication.eu10.hana.ondemand.com/oauth/token"
CLIENT_ID = "sb-fe1fe06b-ddc6-4ed4-8bad-cadb547cbd2b!b576571|aicore!b540"
CLIENT_SECRET = "7d0fe768-f0e1-4448-be1d-671c0117949d$jrD9aNO0JjS6KCLctU6zhLOUkd2calM6AQ4wRRwq3u0="
GENAI_ENDPOINT = "https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com"

def get_token():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

def call_sap_genai(prompt):
    token = get_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 100
    }
    response = requests.post(f"{GENAI_ENDPOINT}/v2/chat/completions", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

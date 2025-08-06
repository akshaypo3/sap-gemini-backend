import requests

def get_access_token(client_id, client_secret, auth_url):
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(
        f"{auth_url}/oauth/token",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    if response.status_code != 200:
        raise Exception("Failed to get access token: " + response.text)

    return response.json()["access_token"]

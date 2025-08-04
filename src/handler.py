import argparse
import os
import requests

def call_gemini(prompt):
    endpoint = os.environ.get("LLM_ENDPOINT")
    token = os.environ.get("LLM_AUTH_TOKEN")

    if not endpoint or not token:
        raise ValueError("Missing LLM_ENDPOINT or LLM_AUTH_TOKEN environment variables.")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "temperature": 0.7
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        print("response=" + response.json().get("text", ""))
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()
    call_gemini(args.prompt)

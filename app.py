from flask import Flask, request, jsonify
import os
import requests
from utils import get_access_token

app = Flask(__name__)

# === SAP AI Core service credentials ===
SAP_GENAI_URL = "https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com"
SAP_AUTH_URL = "https://vaspp-ai-usecases-acvc7v2w.authentication.eu10.hana.ondemand.com"
SAP_CLIENT_ID = "sb-fe1fe06b-ddc6-4ed4-8bad-cadb547cbd2b!b576571|aicore!b540"
SAP_CLIENT_SECRET = "7d0fe768-f0e1-4448-be1d-671c0117949d$jrD9aNO0JjS6KCLctU6zhLOUkd2calM6AQ4wRRwq3u0="

@app.route("/", methods=["POST"])
def ask_genai():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        # === Get OAuth2 access token ===
        access_token = get_access_token(SAP_CLIENT_ID, SAP_CLIENT_SECRET, SAP_AUTH_URL)

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        # === Send request to GenAI ===
        response = requests.post(
            f"{SAP_GENAI_URL}/llm/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            return jsonify({"error": response.text}), response.status_code

        return jsonify(response.json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

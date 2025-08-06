import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# These are secrets injected in AI Core or during local testing set as env
AI_API_URL = os.getenv("AI_API_URL", "https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

@app.route("/ask", methods=["POST"])
def ask_genai():
    user_input = request.json.get("prompt", "")

    if not user_input:
        return jsonify({"error": "Missing prompt"}), 400

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    body = {
        "messages": [{"role": "user", "content": user_input}],
        "model": "gemini-1.5-flash",  # Update if needed
        "temperature": 0.7
    }

    response = requests.post(
        f"{AI_API_URL}/v1/chat/completions",
        json=body,
        headers=headers
    )

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": response.text}), response.status_code
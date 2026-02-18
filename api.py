from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():
    return "CODM API is running"

@app.route("/check_login", methods=["POST"])
def check_login():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return jsonify({"status": "error", "reason": "invalid_api_key"}), 401

    data = request.get_json(force=True)
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "reason": "missing_fields"}), 400

    # LEGAL PLACEHOLDER LOGIC
    if len(password) >= 6:
        return jsonify({
            "status": "clean",
            "username": username
        })
    else:
        return jsonify({
            "status": "invalid",
            "username": username
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

#!/usr/bin/python3
from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory user storage
users = {}

# Root Endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Status Endpoint
@app.route("/status")
def status():
    return "OK"

# Return All Usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Get Specific User
@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])

# Add New User (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Remove username from stored object
    user_data = data.copy()
    user_data.pop("username")

    users[username] = user_data

    return jsonify(data), 201

# Run Server
if __name__ == "__main__":
    app.run()
#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""

from flask import Flask, jsonify, request
app = Flask(__name__)

# define a dictionary to store user data
users = {}

# defines a route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# defines a route for the /data endpoint that returns OK
@app.route("/status")
def status():
    return "OK"

# defines a route for the /data endpoint that returns a JSON response with username data
@app.route('/data')
def usernames():
    return jsonify(list(users.keys()))

# defines a route for the /data/<username> endpoint that returns user information in JSON
@app.route('/users/<username>')
def user_info(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
# defines a route for the /data/<username> endpoint that allows adding new user data via POST request
@app.route('/data/<username>', methods=['POST'])
def add_user(username):
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()

    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']

    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201

if __name__ == '__main__':
    app.run()
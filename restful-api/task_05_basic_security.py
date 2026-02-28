#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'super_secret_key_omg'

# Accepted users with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role":"user"
    },
    "admin": {
        "username": "admin",
        "password": generate_password_hash("admin123"),
        "role":"admin"
    }
}

# Basic Authentication verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username).get('password'), password):
        return users.get(username)
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({'message': 'Basic Auth: Access Granted'})


# JWT Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400
    
    if username in users and check_password_hash(users.get(username).get('password'), password):
        access_token = create_access_token(identity=username, additional_claims={"role": users.get(username).get('role')})
        return jsonify({'access_token': access_token}), 200
    else:        
        return jsonify({'error': 'Unauthorized response'}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({'message': 'JWT Auth: Access Granted'})

# Admin only endpoint
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get('role') != 'admin':
        return jsonify({'error': 'Admin access required'}), 403
    return jsonify({'message': 'Admin Access: Granted'})

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Blueprint, request, jsonify
from auth.login import login_user
from auth.register import register_user
from auth.session import create_session
from database import init_app

auth_bp = Blueprint('auth', __name__)
mongo = init_app(None)  # Initialize the database

# Register route for login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get user data from the request
    session = {
        "emp_id": data.get("emp_id"),
        "password": data.get("password")
    }
    return jsonify({"message": login_user(session, mongo)}), 200

# Register route for registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Get user data from the request
    session = {
        "emp_id": data.get("emp_id"),
        "password": data.get("password"),
        "role": data.get("role", "user")  # Default role is 'user'
    }
    return jsonify({"message": register_user(session, mongo)}), 201

from flask import Blueprint, request, jsonify
from app.models import User  # Import the User model
from app.utils.hashers import hash_password  # Helper for hashing passwords
from app import db  # Database instance
from flask_jwt_extended import create_access_token  # JWT for authentication
auth_bp = Blueprint('auth', __name__)  # Create a blueprint for authentication routes

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    # Validate inputs
    if not email and not phone:
        return jsonify({"error": "Either email or phone is required"}), 400
    if not password:
        return jsonify({"error": "Password is required"}), 400

    # Check if the email or phone is already registered
    if email and User.query.filter_by(email=email).first():
        return jsonify({"error": "Email is already registered"}), 409
    if phone and User.query.filter_by(phone=phone).first():
        return jsonify({"error": "Phone number is already registered"}), 409

    # Create a new user
    hashed_password = hash_password(password)
    new_user = User(email=email, phone=phone, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email_or_phone = data.get('email_or_phone')
    password = data.get('password')

    # Validate inputs
    if not email_or_phone or not password:
        return jsonify({"error": "Email/Phone and password are required"}), 400

    # Check if user exists
    user = User.query.filter((User.email == email_or_phone) | (User.phone == email_or_phone)).first()
    if not user or not verify_password(password, user.password):
        return jsonify({"error": "Invalid email/phone or password"}), 401

    # Generate access token
    access_token = create_access_token(identity=user.id)

    return jsonify({"message": "Login successful", "access_token": access_token}), 200

from flask import Blueprint, jsonify, request
from app.models import User  # Import the User model
from app import db  # Import the database instance

user_bp = Blueprint('user', __name__, url_prefix='/user')  # Blueprint for user-related routes

# Route to get user details by ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "email": user.email,
        "phone": user.phone,
        "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }), 200


# Route to update user information
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    # Update user details
    if email:
        user.email = email
    if phone:
        user.phone = phone
    if password:
        from app.utils.hashers import hash_password  # Ensure hash_password is imported
        user.password_hash = hash_password(password)

    db.session.commit()

    return jsonify({"message": "User updated successfully"}), 200


# Route to delete a user
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200


# Route to list all users
@user_bp.route('/list', methods=['GET'])
def list_users():
    users = User.query.all()
    user_list = [
        {
            "id": user.id,
            "email": user.email,
            "phone": user.phone,
            "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        for user in users
    ]

    return jsonify(user_list), 200

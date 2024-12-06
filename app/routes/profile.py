from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from app.extensions import db

profile_bp = Blueprint('profile', __name__)  # Blueprint for profile routes

@profile_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """
    Get the current user's profile information.
    """
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Return user details
    return jsonify({
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "preferences": user.preferences
    }), 200


@profile_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """
    Update the current user's profile information.
    """
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Get data from the request
    data = request.json
    name = data.get('name', user.name)
    phone = data.get('phone', user.phone)
    preferences = data.get('preferences', user.preferences)

    # Validate inputs (e.g., phone)
    if phone and not phone.isnumeric():
        return jsonify({"error": "Phone number must be numeric"}), 400

    # Update user details
    user.name = name
    user.phone = phone
    user.preferences = preferences

    # Commit changes to the database
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update profile"}), 500

    return jsonify({"message": "Profile updated successfully"}), 200

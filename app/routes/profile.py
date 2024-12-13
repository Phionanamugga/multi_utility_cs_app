
#from flask_jwt_extended import jwt_required, get_jwt_identity
#from app.extensions import db

from flask import Blueprint, request, jsonify
from app.models import User  # Assuming a User model exists in app.models
from app import db  # Assuming the database instance is initialized in app.__init__.py


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

from flask import Blueprint, request, jsonify
from app.models import User  # Assuming a User model exists in app.models
from app import db  # Assuming the database instance is initialized in app.__init__.py

# Create a blueprint for profile-related routes
profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

# Route to fetch a user profile
@profile_bp.route('/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    """
    Retrieve the profile of a user by ID.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Serialize user data for response
    return jsonify({
        "id": user.id,
        "email": user.email,
        "phone": user.phone,
        "created_at": user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    }), 200

# Route to update a user profile
@profile_bp.route('/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    """
    Update a user's profile.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    email = data.get('email')
    phone = data.get('phone')

    # Update fields if provided
    if email:
        user.email = email
    if phone:
        user.phone = phone

    db.session.commit()
    return jsonify({"message": "Profile updated successfully"}), 200

# Route to delete a user profile
@profile_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_profile(user_id):
    """
    Delete a user's profile.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Profile deleted successfully"}), 200

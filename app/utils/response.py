from flask import jsonify

def success_response(data, message="Request successful", status_code=200):
    """Generate a success response."""
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code

def error_response(error_message, status_code=400):
    """Generate an error response."""
    return jsonify({
        "status": "error",
        "message": error_message
    }), status_code

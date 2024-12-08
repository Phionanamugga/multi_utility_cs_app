import re

def validate_email(email):
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format."""
    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, phone) is not None

def validate_required_fields(data, required_fields):
    """Check if all required fields are present and non-empty."""
    missing_fields = [field for field in required_fields if not data.get(field)]
    return missing_fields

def validate_location(location):
    """Validate location string."""
    return bool(location.strip()) and len(location) > 2

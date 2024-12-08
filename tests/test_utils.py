from utils.validation import validate_email, validate_phone

def test_validate_email():
    """Test email validation."""
    assert validate_email("valid@example.com")
    assert not validate_email("invalid-email")

def test_validate_phone():
    """Test phone validation."""
    assert validate_phone("+1234567890")
    assert not validate_phone("12345")

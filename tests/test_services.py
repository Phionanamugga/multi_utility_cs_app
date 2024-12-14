import pytest
from app.services import UserService  # Replace with your actual service module
from app.models import User
from app import db

@pytest.fixture
def test_user():
    """Fixture to create a test user."""
    user = User(username="testuser", password="password123")
    db.session.add(user)
    db.session.commit()
    yield user
    db.session.delete(user)
    db.session.commit()

def test_create_user(app, test_user):
    """Test the creation of a user."""
    user_data = {"username": "newuser", "password": "newpassword"}
    created_user = UserService.create_user(user_data)

    assert created_user.username == "newuser"
    assert created_user.check_password("newpassword")  # Assuming you have a method for password hashing
    db.session.delete(created_user)
    db.session.commit()

def test_get_user_by_id(app, test_user):
    """Test fetching a user by ID."""
    fetched_user = UserService.get_user_by_id(test_user.id)
    assert fetched_user is not None
    assert fetched_user.id == test_user.id
    assert fetched_user.username == test_user.username

def test_user_authentication(app, test_user):
    """Test user authentication."""
    is_authenticated = UserService.authenticate_user("testuser", "password123")
    assert is_authenticated is True

    is_authenticated = UserService.authenticate_user("testuser", "wrongpassword")
    assert is_authenticated is False

def test_update_user(app, test_user):
    """Test updating user information."""
    updated_user = UserService.update_user(test_user.id, {"username": "updateduser"})
    assert updated_user.username == "updateduser"

def test_delete_user(app, test_user):
    """Test deleting a user."""
    UserService.delete_user(test_user.id)
    deleted_user = UserService.get_user_by_id(test_user.id)
    assert deleted_user is None

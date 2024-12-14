import pytest
from app.models import User
from app import db


@pytest.fixture
def new_user():
    """Fixture to create a new user instance."""
    user = User(username="testuser", password="password123")
    return user


def test_user_creation(new_user):
    """Test the creation of a User object."""
    assert new_user.username == "testuser"
    assert new_user.password != "password123"  # Assuming password is hashed


def test_password_hashing(new_user):
    """Test that passwords are hashed correctly."""
    new_user.set_password("mypassword")
    assert new_user.password != "mypassword"  # Password should be hashed
    assert new_user.check_password("mypassword") is True
    assert new_user.check_password("wrongpassword") is False


def test_add_user_to_database(app, new_user):
    """Test adding a user to the database."""
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

        user_in_db = User.query.filter_by(username="testuser").first()
        assert user_in_db is not None
        assert user_in_db.username == "testuser"


def test_delete_user_from_database(app, new_user):
    """Test deleting a user from the database."""
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

        db.session.delete(new_user)
        db.session.commit()

        user_in_db = User.query.filter_by(username="testuser").first()
        assert user_in_db is None


def test_update_user_details(app, new_user):
    """Test updating user details."""
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

        # Update user details
        new_user.username = "updateduser"
        db.session.commit()

        updated_user = User.query.filter_by(username="updateduser").first()
        assert updated_user is not None
        assert updated_user.username == "updateduser"

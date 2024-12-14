import pytest
from app import create_app, db


@pytest.fixture
def test_app():
    """Fixture to create a Flask test app."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # In-memory DB for testing
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(test_app):
    """Fixture to provide a test client."""
    return test_app.test_client()



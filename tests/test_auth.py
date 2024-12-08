def test_signup(client):
    """Test user signup."""
    response = client.post('/auth/signup', json={
        "email": "test@example.com",
        "password": "password123",
        "phone": "+1234567890"
    })
    assert response.status_code == 201
    assert response.json["status"] == "success"
    assert "User registered successfully" in response.json["message"]

def test_login(client):
    """Test user login."""
    client.post('/auth/signup', json={
        "email": "test@example.com",
        "password": "password123",
        "phone": "+1234567890"
    })
    response = client.post('/auth/login', json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json["status"] == "success"
    assert "token" in response.json["data"]

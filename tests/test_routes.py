def test_report_power_outage(client):
    """Test reporting a power outage."""
    response = client.post('/utility/power_outage', json={
        "location": "123 Main Street",
        "account_id": "ACC12345"
    })
    assert response.status_code == 201
    assert response.json["status"] == "success"
    assert "ticket_id" in response.json["data"]

def test_report_water_issue(client):
    """Test reporting a water supply issue."""
    response = client.post('/utility/water_issue', json={
        "location": "456 Water Lane",
        "issue_type": "No supply"
    })
    assert response.status_code == 201
    assert response.json["status"] == "success"
    assert "ticket_id" in response.json["data"]

def test_report_missed_ferry_trip(client):
    """Test reporting a missed ferry trip."""
    response = client.post('/utility/missed_ferry_trip', json={
        "user_id": 1
    })
    assert response.status_code == 201
    assert response.json["status"] == "success"
    assert "ticket_id" in response.json["data"]

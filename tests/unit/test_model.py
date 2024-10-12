import pytest
from iebank_api.models import Account


def test_create_account(testing_client):  # Add 'testing_client' as a parameter
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post(
        "/accounts", json={"name": "John Doe", "currency": "€", "country": "Ireland"}
    )
    assert response.status_code == 200
    assert response.json["name"] == "John Doe"
    assert response.json["currency"] == "€"
    assert response.json["country"] == "Ireland"

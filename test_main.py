from fastapi.testclient import TestClient
from main import app
import pandas as pd
import os

client = TestClient(app)

# Test valid state
def test_mean_price_valid_state():
    response = client.get("/mean_price?state=Vic")
    assert response.status_code == 200
    assert response.json()["state"] == "Vic"
    assert response.json()["mean_price"] == 52.23

# Test invalid state (not in Enum)
def test_mean_price_invalid_state():
    response = client.get("/mean_price?state=WA")
    assert response.status_code == 422
    assert "Invalid state value" in response.json()["error"]


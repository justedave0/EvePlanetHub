import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to EvePlanetHub API"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_api_v1_health():
    response = client.get("/api/v1/health/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
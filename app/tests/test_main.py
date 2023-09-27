from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import api

client = TestClient(api)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}

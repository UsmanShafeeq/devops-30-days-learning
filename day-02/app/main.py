from app.main import app
from fastapi import FastAPI

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

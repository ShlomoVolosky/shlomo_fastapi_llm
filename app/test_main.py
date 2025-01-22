# app/test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_text():
    response = client.post(
        "/generate",
        json={"prompt": "Hello, I'm GPT-2", "max_length": 10, "num_return_sequences": 1},
    )
    assert response.status_code == 200
    assert "results" in response.json()


def test_encode_text():
    response = client.post("/encode", json={"text": "Hello, world"})
    assert response.status_code == 200
    assert "token_ids" in response.json()


def test_decode_text():
    response = client.post("/decode", json={"token_ids": [50256]})
    assert response.status_code == 200
    assert "text" in response.json()

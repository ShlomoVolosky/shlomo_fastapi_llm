import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test data
generate_payload = {
    "prompt": "Hello, world",
    "max_length": 10,
    "num_return_sequences": 1
}

encode_payload = {
    "text": "Hello, world"
}

decode_payload = {
    "token_ids": [50256, 198, 198]
}


@pytest.mark.asyncio
async def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the GPT-Powered REST API with FastAPI."
    }


@pytest.mark.asyncio
async def test_favicon():
    """Test the favicon endpoint."""
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.json() == {"detail": "No favicon available."}


@pytest.mark.asyncio
async def test_generate_text():
    """Test the generate endpoint."""
    response = client.post("/generate", json=generate_payload)
    assert response.status_code == 200
    assert "results" in response.json()
    assert isinstance(response.json()["results"], list)
    assert len(response.json()["results"]) == 1


@pytest.mark.asyncio
async def test_generate_text_invalid():
    """Test the generate endpoint with invalid input."""
    response = client.post("/generate", json={"prompt": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Prompt cannot be empty."


@pytest.mark.asyncio
async def test_encode_text():
    """Test the encode endpoint."""
    response = client.post("/encode", json=encode_payload)
    assert response.status_code == 200
    assert "token_ids" in response.json()
    assert isinstance(response.json()["token_ids"], list)


@pytest.mark.asyncio
async def test_encode_text_invalid():
    """Test the encode endpoint with invalid input."""
    response = client.post("/encode", json={"text": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Text cannot be empty."


@pytest.mark.asyncio
async def test_decode_text():
    """Test the decode endpoint."""
    response = client.post("/decode", json=decode_payload)
    assert response.status_code == 200
    assert "text" in response.json()
    assert isinstance(response.json()["text"], str)


@pytest.mark.asyncio
async def test_decode_text_invalid():
    """Test the decode endpoint with invalid input."""
    response = client.post("/decode", json={"token_ids": []})
    assert response.status_code == 400
    assert response.json()["detail"] == "Token IDs cannot be empty."

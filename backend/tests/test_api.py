from unittest.mock import AsyncMock, patch, MagicMock
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
HEADERS = {"Authorization": "Bearer demo-token-12345"}

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_chat_sin_token_rechazado():
    res = client.post("/api/chat", json={"message": "Hola"})
    assert res.status_code in (401, 403)

def test_chat_con_token_y_llm_mockeado():
    respuesta_falsa = {"messages": [MagicMock(content="Respuesta mockeada")]}
    with patch("main.agente") as mock_agente:
        mock_agente.ainvoke = AsyncMock(return_value=respuesta_falsa)
        res = client.post(
            "/api/chat",
            json={"message": "Hola", "session_id": "test"},
            headers=HEADERS,
        )
    assert res.status_code == 200
    assert "response" in res.json()
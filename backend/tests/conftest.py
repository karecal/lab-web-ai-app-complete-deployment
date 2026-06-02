import os
import sys
import pytest

# Añadir el directorio backend al path para que pytest encuentre main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")
    monkeypatch.setenv("DEMO_TOKEN", "demo-token-12345")
"""Requirement tests: verify Vercel root entrypoint and routes."""

import pytest
from fastapi.testclient import TestClient

from index import app

client = TestClient(app)


def test_vercel_entrypoint_exposes_app() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_vercel_healthz_gemini_route_exists(monkeypatch: pytest.MonkeyPatch) -> None:
    async def mock_gemini_health() -> None:
        return None

    monkeypatch.setattr("app.routes.gemini_health_check", mock_gemini_health)
    response = client.get("/healthz/gemini")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_vercel_api_turn_and_speak_routes_exist() -> None:
    # POST endpoints return 422 for empty request bodies, proving the routes exist
    turn_response = client.post("/api/turn", json={})
    assert turn_response.status_code == 422

    speak_response = client.post("/api/speak", json={})
    assert speak_response.status_code == 422


def test_vercel_serves_frontend_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "HerVoice" in response.text


def test_vercel_serves_static_assets() -> None:
    response = client.get("/styles.css")
    assert response.status_code == 200
    assert "--green-dark" in response.text

    response = client.get("/app.js")
    assert response.status_code == 200
    assert "languageData" in response.text

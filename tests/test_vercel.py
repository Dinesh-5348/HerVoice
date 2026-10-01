"""Requirement tests: verify Vercel entrypoint exposes FastAPI app."""

from fastapi.testclient import TestClient

from api.index import app

client = TestClient(app)


def test_vercel_entrypoint_exposes_app() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


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

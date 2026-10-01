"""Requirement tests: request controls reject oversized and excessive API turns."""

from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

from app.security import SecurityMiddleware


def create_test_app(
    *, requests_per_minute: int = 10, max_request_bytes: int = 1024
) -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        SecurityMiddleware,
        requests_per_minute=requests_per_minute,
        max_request_bytes=max_request_bytes,
    )

    @application.post("/api/turn")
    async def echo_body(request: Request) -> dict[str, object]:
        return {"payload": await request.json()}

    @application.post("/api/speak")
    async def echo_speech_body(request: Request) -> dict[str, object]:
        return {"payload": await request.json()}

    return application


def test_security_headers_are_added_to_api_responses() -> None:
    client = TestClient(create_test_app())
    response = client.post("/api/turn", json={"text": "answer"})

    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["Cache-Control"] == "no-store"


def test_per_ip_rate_limit_returns_429() -> None:
    client = TestClient(create_test_app(requests_per_minute=1))
    assert client.post("/api/turn", json={"text": "first"}).status_code == 200

    response = client.post("/api/turn", json={"text": "second"})

    assert response.status_code == 429
    assert response.headers["Retry-After"] == "60"


def test_speech_endpoint_shares_per_ip_rate_limit() -> None:
    client = TestClient(create_test_app(requests_per_minute=1))
    assert client.post("/api/turn", json={"text": "first"}).status_code == 200

    response = client.post("/api/speak", json={"text": "hello"})

    assert response.status_code == 429


def test_declared_request_size_limit_returns_413() -> None:
    client = TestClient(create_test_app(max_request_bytes=16))

    response = client.post("/api/turn", json={"text": "x" * 50})

    assert response.status_code == 413
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_streamed_request_size_limit_returns_413() -> None:
    client = TestClient(create_test_app(max_request_bytes=16))

    response = client.post(
        "/api/turn",
        content=(part for part in [b"{" + b"x" * 10, b"y" * 10, b"}"]),
        headers={"Content-Type": "application/json", "Transfer-Encoding": "chunked"},
    )

    assert response.status_code == 413

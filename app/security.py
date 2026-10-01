"""Requirement: protect stateless requests with bounded size and per-IP limits."""

import hashlib
import hmac
import secrets
import time
from collections import defaultdict, deque
from collections.abc import Awaitable, Callable

from starlette.datastructures import MutableHeaders
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Message, Receive, Scope, Send

MAX_REQUEST_BYTES = 12 * 1024 * 1024
RATE_LIMIT_WINDOW_SECONDS = 60
RATE_LIMITED_PATHS = {"/api/turn", "/api/speak"}


class SecurityMiddleware:
    """Enforce API body limits, a short-lived IP limit, and browser security headers."""

    def __init__(
        self,
        app: ASGIApp,
        requests_per_minute: int = 30,
        max_request_bytes: int = MAX_REQUEST_BYTES,
    ) -> None:
        self.app = app
        self.requests_per_minute = max(1, requests_per_minute)
        self.max_request_bytes = max_request_bytes
        self._requests: dict[bytes, deque[float]] = defaultdict(deque)
        self._ip_hash_key = secrets.token_bytes(32)
        self._last_cleanup = time.monotonic()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        secured_send = self._send_with_headers(path, send)
        if path in RATE_LIMITED_PATHS and scope.get("method") == "POST":
            client = scope.get("client")
            client_ip = client[0] if client else "unknown"
            if self._is_rate_limited(client_ip):
                await self._error_response(
                    scope,
                    receive,
                    secured_send,
                    429,
                    "rate limit exceeded",
                    {"Retry-After": "60"},
                )
                return

            content_length = self._content_length(scope)
            if content_length is None:
                await self._error_response(
                    scope, receive, secured_send, 400, "invalid content length"
                )
                return
            if content_length > self.max_request_bytes:
                await self._error_response(
                    scope, receive, secured_send, 413, "request too large"
                )
                return

            body = await self._read_bounded_body(scope, receive, secured_send)
            if body is None:
                return
            body_sent = False

            async def replay_body() -> Message:
                nonlocal body_sent
                if body_sent:
                    return {"type": "http.request", "body": b"", "more_body": False}
                body_sent = True
                return {"type": "http.request", "body": body, "more_body": False}

            await self.app(scope, replay_body, secured_send)
            return

        await self.app(scope, receive, secured_send)

    def _is_rate_limited(self, client_ip: str) -> bool:
        now = time.monotonic()
        if now - self._last_cleanup >= RATE_LIMIT_WINDOW_SECONDS:
            self._cleanup(now)
        ip_key = hmac.new(
            self._ip_hash_key, client_ip.encode("utf-8"), hashlib.sha256
        ).digest()
        bucket = self._requests[ip_key]
        while bucket and now - bucket[0] >= RATE_LIMIT_WINDOW_SECONDS:
            bucket.popleft()
        if len(bucket) >= self.requests_per_minute:
            return True
        bucket.append(now)
        return False

    def _cleanup(self, now: float) -> None:
        for ip_key, bucket in list(self._requests.items()):
            while bucket and now - bucket[0] >= RATE_LIMIT_WINDOW_SECONDS:
                bucket.popleft()
            if not bucket:
                del self._requests[ip_key]
        self._last_cleanup = now

    @staticmethod
    def _content_length(scope: Scope) -> int | None:
        for key, value in scope.get("headers", []):
            if key.lower() == b"content-length":
                try:
                    return int(value)
                except ValueError:
                    return None
        return 0

    async def _read_bounded_body(
        self, scope: Scope, receive: Receive, send: Send
    ) -> bytes | None:
        chunks: list[bytes] = []
        total_bytes = 0
        while True:
            message = await receive()
            if message["type"] == "http.disconnect":
                return None
            if message["type"] != "http.request":
                continue
            chunk = message.get("body", b"")
            total_bytes += len(chunk)
            if total_bytes > self.max_request_bytes:
                await self._error_response(
                    scope, receive, send, 413, "request too large"
                )
                return None
            chunks.append(chunk)
            if not message.get("more_body", False):
                return b"".join(chunks)

    @staticmethod
    def _send_with_headers(
        path: str, send: Send
    ) -> Callable[[Message], Awaitable[None]]:
        async def send_secured(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.setdefault(
                    "Content-Security-Policy",
                    "default-src 'self'; script-src 'self'; style-src 'self'; "
                    "img-src 'self' data:; media-src blob:; connect-src 'self'; "
                    "object-src 'none'; frame-ancestors 'none'; base-uri 'self'; "
                    "form-action 'self'",
                )
                headers.setdefault("X-Content-Type-Options", "nosniff")
                headers.setdefault("X-Frame-Options", "DENY")
                headers.setdefault("Referrer-Policy", "no-referrer")
                headers.setdefault("Permissions-Policy", "microphone=(self)")
                if path in RATE_LIMITED_PATHS:
                    headers.setdefault("Cache-Control", "no-store")
            await send(message)

        return send_secured

    @staticmethod
    async def _error_response(
        scope: Scope,
        receive: Receive,
        send: Send,
        status_code: int,
        detail: str,
        headers: dict[str, str] | None = None,
    ) -> None:
        response = JSONResponse(
            {"detail": detail}, status_code=status_code, headers=headers
        )
        await response(scope, receive, send)

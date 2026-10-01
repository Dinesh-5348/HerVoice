"""Requirement: provide the FastAPI application and health endpoint."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import get_rate_limit
from app.routes import router
from app.security import SecurityMiddleware

app = FastAPI()
app.add_middleware(SecurityMiddleware, requests_per_minute=get_rate_limit())


@app.get("/healthz", include_in_schema=False)
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(router)

static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

"""Requirement: provide the FastAPI application and health endpoint."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router

app = FastAPI()


@app.get("/healthz", include_in_schema=False)
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(router)

static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
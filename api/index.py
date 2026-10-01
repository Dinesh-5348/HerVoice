"""Requirement: entrypoint exposing the FastAPI app for Vercel Serverless Functions."""

from app.main import app

__all__ = ["app"]

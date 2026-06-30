"""TASS REST API application (TASS-040).

Requires: pip install -e '.[api]'
Run: tass api  OR  uvicorn api.app:app --host 0.0.0.0 --port 8000
OpenAPI: http://localhost:8000/openapi.json
"""

from __future__ import annotations

try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
except ImportError:
    FastAPI = None  # type: ignore[misc, assignment]
    CORSMiddleware = None  # type: ignore[misc, assignment]

if FastAPI is not None:
    from config.app_settings import get_settings

    from api.routers import analyze, backtest, health, market, picks, ranking, stock

    _settings = get_settings()
    _cors_origins = [
        origin.strip()
        for origin in _settings.cors_origins.split(",")
        if origin.strip()
    ]

    app = FastAPI(
        title="TASS API",
        description="Technical Analysis Scoring System REST API (TASS-040)",
        version="1.0.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)
    app.include_router(analyze.router)
    app.include_router(picks.router)
    app.include_router(ranking.router)
    app.include_router(stock.router)
    app.include_router(backtest.router)
    app.include_router(market.router)

else:
    app = None  # type: ignore[assignment]

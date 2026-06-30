"""SQLAlchemy engine and session factory with graceful fallback."""

from __future__ import annotations

import threading
from contextlib import contextmanager
from typing import Generator

from engine.core.logging import get_logger

logger = get_logger(__name__)

_lock = threading.Lock()
_engine = None
_SessionLocal = None
_db_available: bool | None = None  # None = not yet checked


def _build_engine():
    """Create SQLAlchemy engine from settings; return None if not configured."""
    try:
        import sqlalchemy as sa
        from sqlalchemy.orm import sessionmaker

        from config.app_settings import get_settings

        settings = get_settings()
        url = settings.database_url.strip()

        if not url or url.startswith("postgresql://user:password@localhost"):
            return None, None

        engine = sa.create_engine(
            url,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
            connect_args={"connect_timeout": 5},
        )
        factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
        return engine, factory
    except Exception as exc:
        logger.warning("DB engine init failed: {}", exc)
        return None, None


def _ensure_initialized() -> tuple:
    global _engine, _SessionLocal, _db_available
    with _lock:
        if _db_available is not None:
            return _engine, _SessionLocal
        _engine, _SessionLocal = _build_engine()
        _db_available = _engine is not None
        if _db_available:
            logger.info("PostgreSQL connected")
        else:
            logger.info("PostgreSQL not configured — using file-based fallback")
        return _engine, _SessionLocal


def is_db_available() -> bool:
    """Return True if PostgreSQL is configured and reachable."""
    _ensure_initialized()
    return bool(_db_available)


@contextmanager
def get_session() -> Generator:
    """Context manager for a DB session.

    Yields ``None`` if DB is not available so callers can check and skip.
    """
    engine, factory = _ensure_initialized()
    if factory is None:
        yield None
        return

    try:
        import sqlalchemy as sa
    except ImportError:
        yield None
        return

    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

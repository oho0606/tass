"""TASS structured logging setup (TASS-030 §12)."""

from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger


def setup_logging(
    *,
    log_level: str = "INFO",
    log_dir: Path | None = None,
    rotation: str = "10 MB",
    retention: str = "30 days",
) -> None:
    """Configure Loguru for console and optional file output.

    Args:
        log_level: Minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_dir: Directory for log files; skips file sink when None.
        rotation: Log file rotation policy.
        retention: Log file retention policy.

    Example:
        >>> setup_logging(log_level="DEBUG", log_dir=Path("logs"))
    """
    logger.remove()
    logger.add(
        sys.stderr,
        level=log_level.upper(),
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan> | "
            "<level>{message}</level>"
        ),
    )
    if log_dir is not None:
        log_dir.mkdir(parents=True, exist_ok=True)
        logger.add(
            log_dir / "tass_{time:YYYY-MM-DD}.log",
            level=log_level.upper(),
            rotation=rotation,
            retention=retention,
            encoding="utf-8",
        )


def get_logger(name: str):
    """Return a bound logger for a module or layer.

    Args:
        name: Logger namespace (typically ``__name__``).

    Returns:
        Bound Loguru logger instance.
    """
    return logger.bind(module=name)

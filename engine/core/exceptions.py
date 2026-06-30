"""TASS custom exception hierarchy (TASS-030 §11)."""

from __future__ import annotations


class TassError(Exception):
    """Base exception for all TASS errors."""

    def __init__(self, message: str, *, context: dict[str, object] | None = None) -> None:
        """Initialize with message and optional diagnostic context.

        Args:
            message: Human-readable error description.
            context: Optional key-value diagnostics for logging.
        """
        super().__init__(message)
        self.message = message
        self.context = context or {}


class RuleException(TassError):
    """Raised when atomic or composite rule evaluation fails."""


class EngineException(TassError):
    """Raised when a domain or scoring engine fails."""


class DataException(TassError):
    """Raised when data loading, validation, or adapter operations fail."""


class BacktestException(TassError):
    """Raised when backtest execution or validation fails."""


class RecommendationException(TassError):
    """Raised when recommendation pipeline fails."""

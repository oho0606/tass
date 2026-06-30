"""Backward-compatible re-exports. Use engine.rules.tr instead."""

from engine.rules.tr.atomic import (
    evaluate_higher_high,
    evaluate_higher_low,
    evaluate_lower_high,
    evaluate_lower_low,
)
from engine.rules.tr.composite import (
    evaluate_trend_continuation,
    evaluate_trend_failure,
    evaluate_trend_quality,
    evaluate_trend_structure,
)

__all__ = [
    "evaluate_higher_high",
    "evaluate_higher_low",
    "evaluate_lower_high",
    "evaluate_lower_low",
    "evaluate_trend_structure",
    "evaluate_trend_quality",
    "evaluate_trend_continuation",
    "evaluate_trend_failure",
]

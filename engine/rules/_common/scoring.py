"""Shared scoring for catalog-driven atomic rules."""

from __future__ import annotations

from engine.core.types import RuleVerdict

PASS_SCORE = 10.0


def score_from_verdict(verdict: RuleVerdict) -> float:
    """Map rule verdict to score."""
    if verdict == "PASS":
        return PASS_SCORE
    if verdict == "PARTIAL":
        return PASS_SCORE / 2.0
    return 0.0


def confidence_risk_for_pass(passed: bool) -> tuple[float, float]:
    """Return confidence/risk deltas."""
    if passed:
        return 1.0, -0.5
    return 0.0, 0.5

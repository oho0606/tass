"""Shared scoring for MA atomic rules."""

from __future__ import annotations

from engine.core.types import RuleVerdict

MA_PASS_SCORE = 10.0
MA_FAIL_SCORE = 0.0


def score_from_verdict(verdict: RuleVerdict) -> float:
    """Map MA rule verdict to score."""
    if verdict == "PASS":
        return MA_PASS_SCORE
    return MA_FAIL_SCORE


def confidence_risk_for_pass(passed: bool) -> tuple[float, float]:
    """Return confidence/risk deltas for binary MA rules."""
    if passed:
        return 1.0, -0.5
    return 0.0, 0.5

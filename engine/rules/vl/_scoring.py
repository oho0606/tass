"""Shared scoring for VL atomic rules."""

from __future__ import annotations

from engine.core.types import RuleVerdict

VL_PASS_SCORE = 10.0
VL_FAIL_SCORE = 0.0


def score_from_verdict(verdict: RuleVerdict) -> float:
    """Map VL rule verdict to score."""
    if verdict == "PASS":
        return VL_PASS_SCORE
    return VL_FAIL_SCORE


def confidence_risk_for_pass(passed: bool) -> tuple[float, float]:
    """Return confidence/risk deltas for binary VL rules."""
    if passed:
        return 1.0, -0.5
    return 0.0, 0.5

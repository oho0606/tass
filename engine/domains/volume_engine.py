"""Volume Domain Engine (TASS-017 subset)."""

from __future__ import annotations

import pandas as pd

from engine.core.adopted_rules import filter_adopted_weights, load_adopted_mvp_rule_ids
from engine.core.types import RuleResult, RuleVerdict, VolumeEngineResult
from engine.rules.vl.registry import VL_ENGINE_RULES, VL_ENGINE_WEIGHTS, get_vl_evaluator

VL_BUDGET = 150.0
RULE_MAX_SCORE = 10.0


def _weighted_vl_score(
    results: dict[str, RuleResult],
    weights: dict[str, float] | None = None,
) -> float:
    """Aggregate weighted VL rule scores into domain budget."""
    if not results:
        return 0.0
    active_weights = weights or VL_ENGINE_WEIGHTS
    active_weights = {key: active_weights[key] for key in results if key in active_weights}
    weighted = sum(results[key].score * active_weights[key] for key in results)
    max_weighted = sum(RULE_MAX_SCORE * active_weights[key] for key in results)
    if max_weighted <= 0:
        return 0.0
    return min(VL_BUDGET, (weighted / max_weighted) * VL_BUDGET)


def _grade_from_score(score: float) -> str:
    if score >= 135:
        return "S"
    if score >= 120:
        return "A"
    if score >= 100:
        return "B"
    if score >= 80:
        return "C"
    return "D"


def _state_from_results(results: dict[str, RuleResult]) -> str:
    bullish_keys = ("VL0001", "VL0004", "VL0021", "VL0041", "VL0027", "VL0059")
    bullish = sum(1 for key in bullish_keys if key in results and results[key].verdict == "PASS")
    if bullish >= 4:
        return "Strong Volume Confirmation"
    if bullish >= 2:
        return "Moderate Volume Support"
    return "Weak Volume Support"


def evaluate_volume_engine(df: pd.DataFrame) -> VolumeEngineResult:
    """Evaluate MVP volume rule subset and return domain score.

    Args:
        df: OHLCV DataFrame with volume indicators computed.

    Returns:
        ``VolumeEngineResult`` with score out of 150.
    """
    adopted = load_adopted_mvp_rule_ids()
    scoring_rules = tuple(rule_id for rule_id in VL_ENGINE_RULES if rule_id in adopted)
    atomic_results = {rule_id: get_vl_evaluator(rule_id)(df) for rule_id in scoring_rules}
    vl_weights = filter_adopted_weights(VL_ENGINE_WEIGHTS, adopted)
    vl_score = round(
        _weighted_vl_score({k: atomic_results[k] for k in vl_weights}, vl_weights),
        1,
    )
    grade = _grade_from_score(vl_score)
    state = _state_from_results(atomic_results)

    reasons: list[str] = []
    for result in atomic_results.values():
        if result.verdict in ("PASS", "PARTIAL"):
            reasons.extend(result.reasons)

    return VolumeEngineResult(
        vl_score=vl_score,
        vl_grade=grade,
        vl_state=state,
        atomic_results=atomic_results,
        reasons=list(dict.fromkeys(reasons))[:6],
    )

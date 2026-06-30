"""Moving Average Domain Engine (TASS-015 subset)."""

from __future__ import annotations

import pandas as pd

from engine.core.adopted_rules import filter_adopted_weights, load_adopted_mvp_rule_ids
from engine.core.types import MovingAverageEngineResult, RuleResult, RuleVerdict
from engine.rules.ma.registry import MA_ENGINE_RULES, MA_ENGINE_WEIGHTS, get_ma_evaluator

MA_BUDGET = 150.0
RULE_MAX_SCORE = 10.0


def _weighted_ma_score(
    results: dict[str, RuleResult],
    weights: dict[str, float] | None = None,
) -> float:
    """Aggregate weighted MA rule scores into domain budget."""
    if not results:
        return 0.0
    active_weights = weights or MA_ENGINE_WEIGHTS
    active_weights = {key: active_weights[key] for key in results if key in active_weights}
    weighted = sum(results[key].score * active_weights[key] for key in results)
    max_weighted = sum(RULE_MAX_SCORE * active_weights[key] for key in results)
    if max_weighted <= 0:
        return 0.0
    return min(MA_BUDGET, (weighted / max_weighted) * MA_BUDGET)


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


def _state_from_results(results: dict[str, RuleResult], adopted: frozenset[str]) -> str:
    bullish_keys = tuple(key for key in ("MA0002", "MA0003", "MA0012", "MA0021", "MA0029") if key in adopted)
    bullish = sum(1 for key in bullish_keys if key in results and results[key].verdict == "PASS")
    bearish = "MA0007" in adopted and results.get("MA0007") and results["MA0007"].verdict == "PASS"
    if bullish >= 4:
        return "Bullish MA Structure"
    if bearish:
        return "Bearish MA Structure"
    return "Mixed MA Structure"


def evaluate_moving_average_engine(df: pd.DataFrame) -> MovingAverageEngineResult:
    """Evaluate MVP moving-average rule subset and return domain score.

    Args:
        df: OHLCV DataFrame with MA/EMA indicators computed.

    Returns:
        ``MovingAverageEngineResult`` with score out of 150.
    """
    adopted = load_adopted_mvp_rule_ids()
    scoring_rules = tuple(rule_id for rule_id in MA_ENGINE_RULES if rule_id in adopted)
    atomic_results = {rule_id: get_ma_evaluator(rule_id)(df) for rule_id in scoring_rules}
    ma_weights = filter_adopted_weights(MA_ENGINE_WEIGHTS, adopted)
    ma_score = round(_weighted_ma_score({k: atomic_results[k] for k in ma_weights}, ma_weights), 1)
    grade = _grade_from_score(ma_score)
    state = _state_from_results(atomic_results, adopted)

    reasons: list[str] = []
    for result in atomic_results.values():
        if result.verdict in ("PASS", "PARTIAL"):
            reasons.extend(result.reasons)

    return MovingAverageEngineResult(
        ma_score=ma_score,
        ma_grade=grade,
        ma_state=state,
        atomic_results=atomic_results,
        reasons=list(dict.fromkeys(reasons))[:6],
    )

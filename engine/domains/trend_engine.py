from __future__ import annotations

import pandas as pd

from engine.core.adopted_rules import filter_adopted_weights, load_adopted_mvp_rule_ids
from engine.core.types import RuleResult, RuleVerdict, TrendEngineResult, TrendGrade, TrendState
from engine.rules.composite import evaluate_ctr_rules
from engine.rules.tr.atomic import (
    evaluate_higher_low,
    evaluate_lower_high,
    evaluate_lower_low,
)
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high

ATOMIC_WEIGHTS = {
    "TR0001": 1.20,
    "TR0002": 1.20,
    "TR0003": 1.00,
    "TR0004": 1.10,
}

COMPOSITE_WEIGHTS = {
    "CTR001": 1.50,
    "CTR002": 1.20,
    "CTR003": 1.30,
    "CTR004": 1.10,
    "CTR005": 1.20,
    "CTR006": 1.00,
    "CTR007": 1.00,
    "CTR008": 1.10,
    "CTR009": 1.10,
    "CTR010": 1.50,
}

ATOMIC_MAX = 80.0
COMPOSITE_MAX = 120.0
ATOMIC_RULE_MAX = 20.0
COMPOSITE_RULE_MAX = 12.0

VERDICT_SCORE: dict[RuleVerdict, float] = {
    "PASS": 12.0,
    "PARTIAL": 6.0,
    "FAIL": 0.0,
    "UNKNOWN": 0.0,
}


def _weighted_score(
    results: dict[str, float], weights: dict[str, float], rule_max: float, budget: float
) -> float:
    if not results:
        return 0.0
    weighted = sum(results[k] * weights[k] for k in results)
    max_weighted = sum(rule_max * weights[k] for k in results)
    return min(budget, (weighted / max_weighted) * budget) if max_weighted > 0 else 0.0


def _composite_score(result: RuleResult) -> float:
    return VERDICT_SCORE.get(result.verdict, 0.0)


def _grade_from_score(score: float) -> TrendGrade:
    if score >= 180:
        return TrendGrade.S
    if score >= 160:
        return TrendGrade.A
    if score >= 140:
        return TrendGrade.B
    if score >= 120:
        return TrendGrade.C
    return TrendGrade.D


def _state_from_direction(metadata: dict) -> TrendState:
    direction = metadata.get("direction", "Mixed")
    mapping = {
        "Up": TrendState.STRONG_UP,
        "Weak Up": TrendState.UP,
        "Down": TrendState.DOWN,
        "Weak Down": TrendState.WEAK_DOWN,
        "Mixed": TrendState.SIDEWAYS,
    }
    return mapping.get(str(direction), TrendState.SIDEWAYS)


def evaluate_trend_engine(df: pd.DataFrame) -> TrendEngineResult:
    atomic_results = {
        "TR0001": evaluate_higher_high(df),
        "TR0002": evaluate_higher_low(df),
        "TR0003": evaluate_lower_high(df),
        "TR0004": evaluate_lower_low(df),
    }

    composite_results = evaluate_ctr_rules(atomic_results)

    adopted = load_adopted_mvp_rule_ids()
    atomic_weights = filter_adopted_weights(ATOMIC_WEIGHTS, adopted)
    composite_weights = filter_adopted_weights(COMPOSITE_WEIGHTS, adopted)

    atomic_scores = {k: v.score for k, v in atomic_results.items() if k in atomic_weights}
    composite_scores = {
        k: _composite_score(v) for k, v in composite_results.items() if k in composite_weights
    }

    atomic_total = _weighted_score(atomic_scores, atomic_weights, ATOMIC_RULE_MAX, ATOMIC_MAX)
    composite_total = _weighted_score(
        composite_scores, composite_weights, COMPOSITE_RULE_MAX, COMPOSITE_MAX
    )
    trend_score = round(atomic_total + composite_total, 1)

    grade = _grade_from_score(trend_score)
    state = _state_from_direction(composite_results["CTR001"].metadata)

    conf_deltas = [r.confidence_delta for r in atomic_results.values()]
    risk_deltas = [r.risk_delta for r in atomic_results.values()]
    for result in composite_results.values():
        if result.rule_id not in adopted:
            continue
        if result.verdict == "PASS":
            conf_deltas.append(2.0)
            risk_deltas.append(-1.0)
        elif result.verdict == "PARTIAL":
            conf_deltas.append(0.5)
        elif result.verdict == "FAIL":
            risk_deltas.append(1.0)

    trend_confidence = max(0.0, min(100.0, 50.0 + sum(conf_deltas)))
    trend_risk = max(0.0, min(100.0, 30.0 + sum(risk_deltas)))

    reasons: list[str] = []
    for r in composite_results.values():
        reasons.extend(r.reasons)
    if grade in (TrendGrade.S, TrendGrade.A):
        reasons.insert(0, "강한 상승추세")

    return TrendEngineResult(
        trend_score=trend_score,
        trend_grade=grade,
        trend_state=state,
        trend_confidence=round(trend_confidence, 1),
        trend_risk=round(trend_risk, 1),
        atomic_results=atomic_results,
        composite_results=composite_results,
        reasons=list(dict.fromkeys(reasons))[:8],
    )

"""Generic catalog-driven domain engine evaluator."""

from __future__ import annotations

import pandas as pd

from engine.core.types import DomainEngineResult, RuleResult
from engine.domains._config import RULE_MAX_SCORE, DomainEngineConfig, domain_budget
from engine.rules.catalog_registry import get_evaluator
from engine.rules.composite.registry import COMPOSITE_EVALUATORS
from engine.scoring.domain_budgets import ENGINE_WEIGHTS

COMPOSITE_RULE_MAX = 12.0
COMPOSITE_BUDGET_RATIO = 0.35


def _grade_from_ratio(ratio: float) -> str:
    if ratio >= 0.9:
        return "S"
    if ratio >= 0.8:
        return "A"
    if ratio >= 0.67:
        return "B"
    if ratio >= 0.53:
        return "C"
    return "D"


def _state_from_results(engine_key: str, results: dict[str, RuleResult]) -> str:
    display_name, _ = ENGINE_WEIGHTS[engine_key]
    passed = sum(1 for result in results.values() if result.verdict == "PASS")
    total = len(results) or 1
    ratio = passed / total
    if ratio >= 0.6:
        return f"Strong {display_name}"
    if ratio >= 0.35:
        return f"Moderate {display_name}"
    return f"Weak {display_name}"


def _weighted_atomic_score(
    results: dict[str, RuleResult],
    weights: dict[str, float],
    budget: float,
) -> float:
    if not results:
        return 0.0
    weighted = sum(results[key].score * weights[key] for key in results)
    max_weighted = sum(RULE_MAX_SCORE * weights[key] for key in results)
    if max_weighted <= 0:
        return 0.0
    return min(budget, (weighted / max_weighted) * budget)


def _composite_score(results: dict[str, RuleResult], budget: float) -> float:
    if not results:
        return 0.0
    verdict_scores = {"PASS": 12.0, "PARTIAL": 6.0, "FAIL": 0.0, "UNKNOWN": 0.0}
    raw = sum(verdict_scores.get(result.verdict, 0.0) for result in results.values())
    max_raw = COMPOSITE_RULE_MAX * len(results)
    composite_budget = budget * COMPOSITE_BUDGET_RATIO
    if max_raw <= 0:
        return 0.0
    return min(composite_budget, (raw / max_raw) * composite_budget)


def evaluate_generic_domain_engine(
    config: DomainEngineConfig,
    df: pd.DataFrame,
) -> DomainEngineResult:
    """Evaluate one catalog-driven domain engine."""
    budget = domain_budget(config.engine_key)
    atomic_results = {
        rule_id: get_evaluator(rule_id)(df) for rule_id in config.atomic_rules
    }
    composite_results: dict[str, RuleResult] = {}
    if config.composite_rules:
        composite_results = {
            rule_id: COMPOSITE_EVALUATORS[rule_id](atomic_results)
            for rule_id in config.composite_rules
        }

    atomic_budget = budget * (1.0 - COMPOSITE_BUDGET_RATIO if config.composite_rules else 1.0)
    atomic_score = _weighted_atomic_score(atomic_results, config.atomic_weights, atomic_budget)
    composite_score = _composite_score(composite_results, budget)
    score = round(atomic_score + composite_score, 1)
    ratio = score / budget if budget > 0 else 0.0

    reasons: list[str] = []
    for result in atomic_results.values():
        if result.verdict in ("PASS", "PARTIAL"):
            reasons.extend(result.reasons)
    for result in composite_results.values():
        if result.verdict in ("PASS", "PARTIAL"):
            reasons.extend(result.reasons)

    return DomainEngineResult(
        engine_key=config.engine_key,
        score=score,
        max_score=budget,
        grade=_grade_from_ratio(ratio),
        state=_state_from_results(config.engine_key, atomic_results),
        atomic_results=atomic_results,
        composite_results=composite_results,
        reasons=list(dict.fromkeys(reasons))[:6],
    )

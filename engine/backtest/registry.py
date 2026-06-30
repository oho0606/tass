"""Rule evaluator registry for backtest runs."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma.ma0002_price_above_sma20 import evaluate_ma0002
from engine.rules.tr.atomic import evaluate_higher_low, evaluate_lower_high, evaluate_lower_low
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

LOCAL_RULE_EVALUATORS: dict[str, RuleEvaluator] = {
    "TR0001": evaluate_higher_high,
    "TR0002": evaluate_higher_low,
    "TR0003": evaluate_lower_high,
    "TR0004": evaluate_lower_low,
    "MA0002": evaluate_ma0002,
}

_CTR_ATOMIC_DEPS = ("TR0001", "TR0002", "TR0003", "TR0004")


def _ctr_dataframe_evaluator(rule_id: str) -> RuleEvaluator:
    """Wrap composite CTR evaluators for walk-forward backtest (DataFrame in)."""
    from engine.rules.composite.registry import COMPOSITE_EVALUATORS
    from engine.rules.tr.registry import TR_EVALUATORS

    composite_fn = COMPOSITE_EVALUATORS[rule_id]

    def evaluator(df: pd.DataFrame) -> RuleResult:
        atomic = {aid: TR_EVALUATORS[aid](df) for aid in _CTR_ATOMIC_DEPS}
        return composite_fn(atomic)

    return evaluator


# Backward-compatible alias
RULE_EVALUATORS = LOCAL_RULE_EVALUATORS


def get_rule_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator callable for a canonical rule ID."""
    if rule_id in LOCAL_RULE_EVALUATORS:
        return LOCAL_RULE_EVALUATORS[rule_id]

    if rule_id.startswith("CTR"):
        from engine.rules.composite.registry import COMPOSITE_EVALUATORS

        if rule_id in COMPOSITE_EVALUATORS:
            return _ctr_dataframe_evaluator(rule_id)

    from engine.rules.catalog_registry import get_evaluator

    return get_evaluator(rule_id)


def list_backtestable_rules() -> list[str]:
    """Return sorted rule IDs available for backtest."""
    from engine.rules.catalog_registry import all_rule_ids

    return sorted(set(LOCAL_RULE_EVALUATORS) | set(all_rule_ids()))

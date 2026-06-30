"""PB0024 — Price Touching EMA60 During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0024PriceTouchingEMA60DuringPullbackRule(SpecRule):
    rule_id = "PB0024"
    rule_name = "Price Touching EMA60 During Pullback"


def evaluate_pb0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0024."""
    return run_spec_rule(PB0024PriceTouchingEMA60DuringPullbackRule, df)

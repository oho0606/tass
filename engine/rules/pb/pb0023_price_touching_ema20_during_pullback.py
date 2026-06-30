"""PB0023 — Price Touching EMA20 During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0023PriceTouchingEMA20DuringPullbackRule(SpecRule):
    rule_id = "PB0023"
    rule_name = "Price Touching EMA20 During Pullback"


def evaluate_pb0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0023."""
    return run_spec_rule(PB0023PriceTouchingEMA20DuringPullbackRule, df)

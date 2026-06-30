"""PB0021 — Price Touching SMA20 During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0021PriceTouchingSMA20DuringPullbackRule(SpecRule):
    rule_id = "PB0021"
    rule_name = "Price Touching SMA20 During Pullback"


def evaluate_pb0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0021."""
    return run_spec_rule(PB0021PriceTouchingSMA20DuringPullbackRule, df)

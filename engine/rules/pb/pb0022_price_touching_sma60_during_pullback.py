"""PB0022 — Price Touching SMA60 During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0022PriceTouchingSMA60DuringPullbackRule(SpecRule):
    rule_id = "PB0022"
    rule_name = "Price Touching SMA60 During Pullback"


def evaluate_pb0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0022."""
    return run_spec_rule(PB0022PriceTouchingSMA60DuringPullbackRule, df)

"""PB0025 — Price Closing Above SMA20 During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0025PriceClosingAboveSMA20DuringPullbackRule(SpecRule):
    rule_id = "PB0025"
    rule_name = "Price Closing Above SMA20 During Pullback"


def evaluate_pb0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0025."""
    return run_spec_rule(PB0025PriceClosingAboveSMA20DuringPullbackRule, df)

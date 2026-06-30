"""PB0026 — Price Closing Below SMA20 During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0026PriceClosingBelowSMA20DuringPullbackRule(SpecRule):
    rule_id = "PB0026"
    rule_name = "Price Closing Below SMA20 During Pullback"


def evaluate_pb0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0026."""
    return run_spec_rule(PB0026PriceClosingBelowSMA20DuringPullbackRule, df)

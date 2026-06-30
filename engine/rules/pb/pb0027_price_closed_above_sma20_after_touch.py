"""PB0027 — Price Closed Above SMA20 After Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0027PriceClosedAboveSMA20AfterTouchRule(SpecRule):
    rule_id = "PB0027"
    rule_name = "Price Closed Above SMA20 After Touch"


def evaluate_pb0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0027."""
    return run_spec_rule(PB0027PriceClosedAboveSMA20AfterTouchRule, df)

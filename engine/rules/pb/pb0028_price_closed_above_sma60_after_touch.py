"""PB0028 — Price Closed Above SMA60 After Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0028PriceClosedAboveSMA60AfterTouchRule(SpecRule):
    rule_id = "PB0028"
    rule_name = "Price Closed Above SMA60 After Touch"


def evaluate_pb0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0028."""
    return run_spec_rule(PB0028PriceClosedAboveSMA60AfterTouchRule, df)

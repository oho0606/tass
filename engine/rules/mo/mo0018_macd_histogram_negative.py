"""MO0018 — MACD Histogram Negative. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0018MACDHistogramNegativeRule(SpecRule):
    rule_id = "MO0018"
    rule_name = "MACD Histogram Negative"


def evaluate_mo0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0018."""
    return run_spec_rule(MO0018MACDHistogramNegativeRule, df)

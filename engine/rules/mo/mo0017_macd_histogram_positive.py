"""MO0017 — MACD Histogram Positive. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0017MACDHistogramPositiveRule(SpecRule):
    rule_id = "MO0017"
    rule_name = "MACD Histogram Positive"


def evaluate_mo0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0017."""
    return run_spec_rule(MO0017MACDHistogramPositiveRule, df)

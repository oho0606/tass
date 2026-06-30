"""MO0020 — MACD Histogram Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0020MACDHistogramFallingRule(SpecRule):
    rule_id = "MO0020"
    rule_name = "MACD Histogram Falling"


def evaluate_mo0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0020."""
    return run_spec_rule(MO0020MACDHistogramFallingRule, df)

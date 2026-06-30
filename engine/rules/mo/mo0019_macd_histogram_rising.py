"""MO0019 — MACD Histogram Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0019MACDHistogramRisingRule(SpecRule):
    rule_id = "MO0019"
    rule_name = "MACD Histogram Rising"


def evaluate_mo0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0019."""
    return run_spec_rule(MO0019MACDHistogramRisingRule, df)

"""MR0044 — Historical Volatility At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0044HistoricalVolatilityAtNPeriodLowRule(SpecRule):
    rule_id = "MR0044"
    rule_name = "Historical Volatility At N-Period Low"


def evaluate_mr0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0044."""
    return run_spec_rule(MR0044HistoricalVolatilityAtNPeriodLowRule, df)

"""MR0034 — Historical Volatility At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0034HistoricalVolatilityAtNPeriodHighRule(SpecRule):
    rule_id = "MR0034"
    rule_name = "Historical Volatility At N-Period High"


def evaluate_mr0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0034."""
    return run_spec_rule(MR0034HistoricalVolatilityAtNPeriodHighRule, df)

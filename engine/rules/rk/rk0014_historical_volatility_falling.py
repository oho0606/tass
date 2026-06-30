"""RK0014 — Historical Volatility Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0014HistoricalVolatilityFallingRule(SpecRule):
    rule_id = "RK0014"
    rule_name = "Historical Volatility Falling"


def evaluate_rk0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0014."""
    return run_spec_rule(RK0014HistoricalVolatilityFallingRule, df)

"""RK0013 — Historical Volatility Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0013HistoricalVolatilityRisingRule(SpecRule):
    rule_id = "RK0013"
    rule_name = "Historical Volatility Rising"


def evaluate_rk0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0013."""
    return run_spec_rule(RK0013HistoricalVolatilityRisingRule, df)

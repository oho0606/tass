"""CF0040 — Historical Volatility Rising Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0040HistoricalVolatilityRisingConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0040"
    rule_name = "Historical Volatility Rising Confirms Bearish Trend"


def evaluate_cf0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0040."""
    return run_spec_rule(CF0040HistoricalVolatilityRisingConfirmsBearishTrendRule, df)

"""CF0039 — Historical Volatility Rising Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0039HistoricalVolatilityRisingConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0039"
    rule_name = "Historical Volatility Rising Confirms Bullish Trend"


def evaluate_cf0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0039."""
    return run_spec_rule(CF0039HistoricalVolatilityRisingConfirmsBullishTrendRule, df)

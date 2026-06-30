"""VO0021 — Historical Volatility Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0021HistoricalVolatilityRisingRule(SpecRule):
    rule_id = "VO0021"
    rule_name = "Historical Volatility Rising"


def evaluate_vo0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0021."""
    return run_spec_rule(VO0021HistoricalVolatilityRisingRule, df)

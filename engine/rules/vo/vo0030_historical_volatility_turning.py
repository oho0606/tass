"""VO0030 — Historical Volatility Turning. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0030HistoricalVolatilityTurningRule(SpecRule):
    rule_id = "VO0030"
    rule_name = "Historical Volatility Turning"


def evaluate_vo0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0030."""
    return run_spec_rule(VO0030HistoricalVolatilityTurningRule, df)

"""VO0022 — Historical Volatility Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0022HistoricalVolatilityFallingRule(SpecRule):
    rule_id = "VO0022"
    rule_name = "Historical Volatility Falling"


def evaluate_vo0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0022."""
    return run_spec_rule(VO0022HistoricalVolatilityFallingRule, df)

"""VO0052 — Historical Volatility Stable. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0052HistoricalVolatilityStableRule(SpecRule):
    rule_id = "VO0052"
    rule_name = "Historical Volatility Stable"


def evaluate_vo0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0052."""
    return run_spec_rule(VO0052HistoricalVolatilityStableRule, df)

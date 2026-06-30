"""VO0029 — Historical Volatility Flat. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0029HistoricalVolatilityFlatRule(SpecRule):
    rule_id = "VO0029"
    rule_name = "Historical Volatility Flat"


def evaluate_vo0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0029."""
    return run_spec_rule(VO0029HistoricalVolatilityFlatRule, df)

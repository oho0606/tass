"""VO0028 — Historical Volatility At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0028HistoricalVolatilityAtNPeriodLowRule(SpecRule):
    rule_id = "VO0028"
    rule_name = "Historical Volatility At N-Period Low"


def evaluate_vo0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0028."""
    return run_spec_rule(VO0028HistoricalVolatilityAtNPeriodLowRule, df)

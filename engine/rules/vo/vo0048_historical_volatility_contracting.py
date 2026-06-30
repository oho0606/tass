"""VO0048 — Historical Volatility Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0048HistoricalVolatilityContractingRule(SpecRule):
    rule_id = "VO0048"
    rule_name = "Historical Volatility Contracting"


def evaluate_vo0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0048."""
    return run_spec_rule(VO0048HistoricalVolatilityContractingRule, df)

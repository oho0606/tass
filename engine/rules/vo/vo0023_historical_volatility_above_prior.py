"""VO0023 — Historical Volatility Above Prior. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0023HistoricalVolatilityAbovePriorRule(SpecRule):
    rule_id = "VO0023"
    rule_name = "Historical Volatility Above Prior"


def evaluate_vo0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0023."""
    return run_spec_rule(VO0023HistoricalVolatilityAbovePriorRule, df)

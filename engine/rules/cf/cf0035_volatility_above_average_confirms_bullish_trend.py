"""CF0035 — Volatility Above Average Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0035VolatilityAboveAverageConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0035"
    rule_name = "Volatility Above Average Confirms Bullish Trend"


def evaluate_cf0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0035."""
    return run_spec_rule(CF0035VolatilityAboveAverageConfirmsBullishTrendRule, df)

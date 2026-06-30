"""CF0036 — Volatility Above Average Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0036VolatilityAboveAverageConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0036"
    rule_name = "Volatility Above Average Confirms Bearish Trend"


def evaluate_cf0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0036."""
    return run_spec_rule(CF0036VolatilityAboveAverageConfirmsBearishTrendRule, df)

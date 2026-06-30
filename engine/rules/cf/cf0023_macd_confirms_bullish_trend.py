"""CF0023 — MACD Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0023MACDConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0023"
    rule_name = "MACD Confirms Bullish Trend"


def evaluate_cf0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0023."""
    return run_spec_rule(CF0023MACDConfirmsBullishTrendRule, df)

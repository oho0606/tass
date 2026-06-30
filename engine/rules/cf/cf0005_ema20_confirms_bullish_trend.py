"""CF0005 — EMA20 Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0005EMA20ConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0005"
    rule_name = "EMA20 Confirms Bullish Trend"


def evaluate_cf0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0005."""
    return run_spec_rule(CF0005EMA20ConfirmsBullishTrendRule, df)

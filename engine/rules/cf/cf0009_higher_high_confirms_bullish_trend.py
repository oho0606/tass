"""CF0009 — Higher High Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0009HigherHighConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0009"
    rule_name = "Higher High Confirms Bullish Trend"


def evaluate_cf0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0009."""
    return run_spec_rule(CF0009HigherHighConfirmsBullishTrendRule, df)

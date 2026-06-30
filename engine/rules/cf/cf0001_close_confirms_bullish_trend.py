"""CF0001 — Close Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0001CloseConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0001"
    rule_name = "Close Confirms Bullish Trend"


def evaluate_cf0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0001."""
    return run_spec_rule(CF0001CloseConfirmsBullishTrendRule, df)

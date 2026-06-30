"""CF0027 — CCI Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0027CCIConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0027"
    rule_name = "CCI Confirms Bullish Trend"


def evaluate_cf0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0027."""
    return run_spec_rule(CF0027CCIConfirmsBullishTrendRule, df)

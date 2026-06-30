"""CF0022 — RSI Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0022RSIConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0022"
    rule_name = "RSI Confirms Bearish Trend"


def evaluate_cf0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0022."""
    return run_spec_rule(CF0022RSIConfirmsBearishTrendRule, df)

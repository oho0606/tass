"""CF0024 — MACD Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0024MACDConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0024"
    rule_name = "MACD Confirms Bearish Trend"


def evaluate_cf0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0024."""
    return run_spec_rule(CF0024MACDConfirmsBearishTrendRule, df)

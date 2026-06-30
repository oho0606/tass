"""CF0006 — EMA20 Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0006EMA20ConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0006"
    rule_name = "EMA20 Confirms Bearish Trend"


def evaluate_cf0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0006."""
    return run_spec_rule(CF0006EMA20ConfirmsBearishTrendRule, df)

"""CF0004 — SMA20 Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0004SMA20ConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0004"
    rule_name = "SMA20 Confirms Bearish Trend"


def evaluate_cf0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0004."""
    return run_spec_rule(CF0004SMA20ConfirmsBearishTrendRule, df)

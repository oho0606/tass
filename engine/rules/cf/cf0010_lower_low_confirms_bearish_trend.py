"""CF0010 — Lower Low Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0010LowerLowConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0010"
    rule_name = "Lower Low Confirms Bearish Trend"


def evaluate_cf0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0010."""
    return run_spec_rule(CF0010LowerLowConfirmsBearishTrendRule, df)

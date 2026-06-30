"""CF0030 — Rate Of Change Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0030RateOfChangeConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0030"
    rule_name = "Rate Of Change Confirms Bearish Trend"


def evaluate_cf0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0030."""
    return run_spec_rule(CF0030RateOfChangeConfirmsBearishTrendRule, df)

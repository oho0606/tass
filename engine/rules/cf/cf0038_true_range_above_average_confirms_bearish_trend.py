"""CF0038 — True Range Above Average Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0038TrueRangeAboveAverageConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0038"
    rule_name = "True Range Above Average Confirms Bearish Trend"


def evaluate_cf0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0038."""
    return run_spec_rule(CF0038TrueRangeAboveAverageConfirmsBearishTrendRule, df)

"""CF0007 — SMA Alignment Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0007SMAAlignmentConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0007"
    rule_name = "SMA Alignment Confirms Bullish Trend"


def evaluate_cf0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0007."""
    return run_spec_rule(CF0007SMAAlignmentConfirmsBullishTrendRule, df)

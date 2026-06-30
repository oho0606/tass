"""CF0008 — SMA Alignment Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0008SMAAlignmentConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0008"
    rule_name = "SMA Alignment Confirms Bearish Trend"


def evaluate_cf0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0008."""
    return run_spec_rule(CF0008SMAAlignmentConfirmsBearishTrendRule, df)

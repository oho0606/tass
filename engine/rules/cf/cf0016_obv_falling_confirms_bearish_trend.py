"""CF0016 — OBV Falling Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0016OBVFallingConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0016"
    rule_name = "OBV Falling Confirms Bearish Trend"


def evaluate_cf0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0016."""
    return run_spec_rule(CF0016OBVFallingConfirmsBearishTrendRule, df)

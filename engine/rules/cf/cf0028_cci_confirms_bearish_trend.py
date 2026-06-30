"""CF0028 — CCI Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0028CCIConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0028"
    rule_name = "CCI Confirms Bearish Trend"


def evaluate_cf0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0028."""
    return run_spec_rule(CF0028CCIConfirmsBearishTrendRule, df)

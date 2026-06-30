"""CF0032 — ATR Rising Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0032ATRRisingConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0032"
    rule_name = "ATR Rising Confirms Bearish Trend"


def evaluate_cf0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0032."""
    return run_spec_rule(CF0032ATRRisingConfirmsBearishTrendRule, df)

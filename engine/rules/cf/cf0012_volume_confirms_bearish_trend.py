"""CF0012 — Volume Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0012VolumeConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0012"
    rule_name = "Volume Confirms Bearish Trend"


def evaluate_cf0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0012."""
    return run_spec_rule(CF0012VolumeConfirmsBearishTrendRule, df)

"""CF0017 — Volume Above Average Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0017VolumeAboveAverageConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0017"
    rule_name = "Volume Above Average Confirms Bullish Trend"


def evaluate_cf0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0017."""
    return run_spec_rule(CF0017VolumeAboveAverageConfirmsBullishTrendRule, df)

"""CF0015 — OBV Rising Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0015OBVRisingConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0015"
    rule_name = "OBV Rising Confirms Bullish Trend"


def evaluate_cf0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0015."""
    return run_spec_rule(CF0015OBVRisingConfirmsBullishTrendRule, df)

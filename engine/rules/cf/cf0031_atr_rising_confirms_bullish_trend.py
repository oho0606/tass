"""CF0031 — ATR Rising Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0031ATRRisingConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0031"
    rule_name = "ATR Rising Confirms Bullish Trend"


def evaluate_cf0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0031."""
    return run_spec_rule(CF0031ATRRisingConfirmsBullishTrendRule, df)

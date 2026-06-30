"""VO0032 — Price Below Lower Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0032PriceBelowLowerBollingerBandRule(SpecRule):
    rule_id = "VO0032"
    rule_name = "Price Below Lower Bollinger Band"


def evaluate_vo0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0032."""
    return run_spec_rule(VO0032PriceBelowLowerBollingerBandRule, df)

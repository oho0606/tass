"""BO0036 — Price Below Lower Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0036PriceBelowLowerBollingerBandRule(SpecRule):
    rule_id = "BO0036"
    rule_name = "Price Below Lower Bollinger Band"


def evaluate_bo0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0036."""
    return run_spec_rule(BO0036PriceBelowLowerBollingerBandRule, df)

"""VO0031 — Price Above Upper Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0031PriceAboveUpperBollingerBandRule(SpecRule):
    rule_id = "VO0031"
    rule_name = "Price Above Upper Bollinger Band"


def evaluate_vo0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0031."""
    return run_spec_rule(VO0031PriceAboveUpperBollingerBandRule, df)

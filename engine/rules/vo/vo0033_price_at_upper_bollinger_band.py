"""VO0033 — Price At Upper Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0033PriceAtUpperBollingerBandRule(SpecRule):
    rule_id = "VO0033"
    rule_name = "Price At Upper Bollinger Band"


def evaluate_vo0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0033."""
    return run_spec_rule(VO0033PriceAtUpperBollingerBandRule, df)

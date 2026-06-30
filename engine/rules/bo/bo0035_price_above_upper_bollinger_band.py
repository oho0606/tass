"""BO0035 — Price Above Upper Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0035PriceAboveUpperBollingerBandRule(SpecRule):
    rule_id = "BO0035"
    rule_name = "Price Above Upper Bollinger Band"


def evaluate_bo0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0035."""
    return run_spec_rule(BO0035PriceAboveUpperBollingerBandRule, df)

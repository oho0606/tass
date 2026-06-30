"""VO0035 — Price At Middle Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0035PriceAtMiddleBollingerBandRule(SpecRule):
    rule_id = "VO0035"
    rule_name = "Price At Middle Bollinger Band"


def evaluate_vo0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0035."""
    return run_spec_rule(VO0035PriceAtMiddleBollingerBandRule, df)

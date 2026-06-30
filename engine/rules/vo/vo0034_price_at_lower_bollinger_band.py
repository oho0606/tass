"""VO0034 — Price At Lower Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0034PriceAtLowerBollingerBandRule(SpecRule):
    rule_id = "VO0034"
    rule_name = "Price At Lower Bollinger Band"


def evaluate_vo0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0034."""
    return run_spec_rule(VO0034PriceAtLowerBollingerBandRule, df)

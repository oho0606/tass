"""SR0015 — Price Touching Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0015PriceTouchingHorizontalResistanceRule(SpecRule):
    rule_id = "SR0015"
    rule_name = "Price Touching Horizontal Resistance"


def evaluate_sr0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0015."""
    return run_spec_rule(SR0015PriceTouchingHorizontalResistanceRule, df)

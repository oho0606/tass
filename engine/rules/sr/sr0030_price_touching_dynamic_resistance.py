"""SR0030 — Price Touching Dynamic Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0030PriceTouchingDynamicResistanceRule(SpecRule):
    rule_id = "SR0030"
    rule_name = "Price Touching Dynamic Resistance"


def evaluate_sr0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0030."""
    return run_spec_rule(SR0030PriceTouchingDynamicResistanceRule, df)

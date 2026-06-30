"""SR0011 — Price Above Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0011PriceAboveHorizontalResistanceRule(SpecRule):
    rule_id = "SR0011"
    rule_name = "Price Above Horizontal Resistance"


def evaluate_sr0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0011."""
    return run_spec_rule(SR0011PriceAboveHorizontalResistanceRule, df)

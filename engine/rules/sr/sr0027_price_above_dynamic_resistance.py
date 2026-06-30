"""SR0027 — Price Above Dynamic Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0027PriceAboveDynamicResistanceRule(SpecRule):
    rule_id = "SR0027"
    rule_name = "Price Above Dynamic Resistance"


def evaluate_sr0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0027."""
    return run_spec_rule(SR0027PriceAboveDynamicResistanceRule, df)

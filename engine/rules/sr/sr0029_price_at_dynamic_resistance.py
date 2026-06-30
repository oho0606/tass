"""SR0029 — Price At Dynamic Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0029PriceAtDynamicResistanceRule(SpecRule):
    rule_id = "SR0029"
    rule_name = "Price At Dynamic Resistance"


def evaluate_sr0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0029."""
    return run_spec_rule(SR0029PriceAtDynamicResistanceRule, df)

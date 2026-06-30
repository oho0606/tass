"""PA0049 — Price Above Last Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0049PriceAboveLastSwingHighRule(SpecRule):
    rule_id = "PA0049"
    rule_name = "Price Above Last Swing High"


def evaluate_pa0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0049."""
    return run_spec_rule(PA0049PriceAboveLastSwingHighRule, df)

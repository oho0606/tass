"""SR0037 — Price Above R1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0037PriceAboveR1Rule(SpecRule):
    rule_id = "SR0037"
    rule_name = "Price Above R1"


def evaluate_sr0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0037."""
    return run_spec_rule(SR0037PriceAboveR1Rule, df)

"""MO0011 — MACD Above Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0011MACDAboveZeroRule(SpecRule):
    rule_id = "MO0011"
    rule_name = "MACD Above Zero"


def evaluate_mo0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0011."""
    return run_spec_rule(MO0011MACDAboveZeroRule, df)

"""MO0010 — RSI Cross Below 30. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0010RSICrossBelow30Rule(SpecRule):
    rule_id = "MO0010"
    rule_name = "RSI Cross Below 30"


def evaluate_mo0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0010."""
    return run_spec_rule(MO0010RSICrossBelow30Rule, df)

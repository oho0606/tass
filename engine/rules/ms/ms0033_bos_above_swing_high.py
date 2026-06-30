"""MS0033 — BOS Above Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0033BOSAboveSwingHighRule(SpecRule):
    rule_id = "MS0033"
    rule_name = "BOS Above Swing High"


def evaluate_ms0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0033."""
    return run_spec_rule(MS0033BOSAboveSwingHighRule, df)

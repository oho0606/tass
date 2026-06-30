"""MS0007 — Higher Low Confirmed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0007HigherLowConfirmedRule(SpecRule):
    rule_id = "MS0007"
    rule_name = "Higher Low Confirmed"


def evaluate_ms0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0007."""
    return run_spec_rule(MS0007HigherLowConfirmedRule, df)

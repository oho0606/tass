"""MS0008 — Higher Low Exceeds Prior. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0008HigherLowExceedsPriorRule(SpecRule):
    rule_id = "MS0008"
    rule_name = "Higher Low Exceeds Prior"


def evaluate_ms0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0008."""
    return run_spec_rule(MS0008HigherLowExceedsPriorRule, df)

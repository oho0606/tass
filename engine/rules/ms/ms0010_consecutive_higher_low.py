"""MS0010 — Consecutive Higher Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0010ConsecutiveHigherLowRule(SpecRule):
    rule_id = "MS0010"
    rule_name = "Consecutive Higher Low"


def evaluate_ms0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0010."""
    return run_spec_rule(MS0010ConsecutiveHigherLowRule, df)

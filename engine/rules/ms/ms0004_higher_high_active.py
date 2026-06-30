"""MS0004 — Higher High Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0004HigherHighActiveRule(SpecRule):
    rule_id = "MS0004"
    rule_name = "Higher High Active"


def evaluate_ms0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0004."""
    return run_spec_rule(MS0004HigherHighActiveRule, df)

"""MS0012 — Lower High Confirmed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0012LowerHighConfirmedRule(SpecRule):
    rule_id = "MS0012"
    rule_name = "Lower High Confirmed"


def evaluate_ms0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0012."""
    return run_spec_rule(MS0012LowerHighConfirmedRule, df)

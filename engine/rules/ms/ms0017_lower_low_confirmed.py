"""MS0017 — Lower Low Confirmed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0017LowerLowConfirmedRule(SpecRule):
    rule_id = "MS0017"
    rule_name = "Lower Low Confirmed"


def evaluate_ms0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0017."""
    return run_spec_rule(MS0017LowerLowConfirmedRule, df)

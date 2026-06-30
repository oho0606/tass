"""DQ0054 — Current Bar Absent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0054CurrentBarAbsentRule(SpecRule):
    rule_id = "DQ0054"
    rule_name = "Current Bar Absent"


def evaluate_dq0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0054."""
    return run_spec_rule(DQ0054CurrentBarAbsentRule, df)

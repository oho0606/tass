"""DQ0052 — Required History Absent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0052RequiredHistoryAbsentRule(SpecRule):
    rule_id = "DQ0052"
    rule_name = "Required History Absent"


def evaluate_dq0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0052."""
    return run_spec_rule(DQ0052RequiredHistoryAbsentRule, df)

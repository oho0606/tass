"""MS0054 — Swing Overlap Absent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0054SwingOverlapAbsentRule(SpecRule):
    rule_id = "MS0054"
    rule_name = "Swing Overlap Absent"


def evaluate_ms0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0054."""
    return run_spec_rule(MS0054SwingOverlapAbsentRule, df)

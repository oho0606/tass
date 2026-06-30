"""MS0026 — Swing Low Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0026SwingLowActiveRule(SpecRule):
    rule_id = "MS0026"
    rule_name = "Swing Low Active"


def evaluate_ms0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0026."""
    return run_spec_rule(MS0026SwingLowActiveRule, df)

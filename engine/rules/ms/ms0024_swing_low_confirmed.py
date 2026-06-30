"""MS0024 — Swing Low Confirmed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0024SwingLowConfirmedRule(SpecRule):
    rule_id = "MS0024"
    rule_name = "Swing Low Confirmed"


def evaluate_ms0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0024."""
    return run_spec_rule(MS0024SwingLowConfirmedRule, df)

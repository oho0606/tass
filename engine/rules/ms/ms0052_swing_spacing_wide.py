"""MS0052 — Swing Spacing Wide. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0052SwingSpacingWideRule(SpecRule):
    rule_id = "MS0052"
    rule_name = "Swing Spacing Wide"


def evaluate_ms0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0052."""
    return run_spec_rule(MS0052SwingSpacingWideRule, df)

"""MS0051 — Swing Spacing Narrow. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0051SwingSpacingNarrowRule(SpecRule):
    rule_id = "MS0051"
    rule_name = "Swing Spacing Narrow"


def evaluate_ms0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0051."""
    return run_spec_rule(MS0051SwingSpacingNarrowRule, df)

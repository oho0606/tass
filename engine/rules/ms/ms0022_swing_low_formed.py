"""MS0022 — Swing Low Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0022SwingLowFormedRule(SpecRule):
    rule_id = "MS0022"
    rule_name = "Swing Low Formed"


def evaluate_ms0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0022."""
    return run_spec_rule(MS0022SwingLowFormedRule, df)

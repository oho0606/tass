"""MS0021 — Swing High Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0021SwingHighFormedRule(SpecRule):
    rule_id = "MS0021"
    rule_name = "Swing High Formed"


def evaluate_ms0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0021."""
    return run_spec_rule(MS0021SwingHighFormedRule, df)

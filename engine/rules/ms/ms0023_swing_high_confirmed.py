"""MS0023 — Swing High Confirmed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0023SwingHighConfirmedRule(SpecRule):
    rule_id = "MS0023"
    rule_name = "Swing High Confirmed"


def evaluate_ms0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0023."""
    return run_spec_rule(MS0023SwingHighConfirmedRule, df)

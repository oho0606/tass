"""PA0041 — Swing High Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0041SwingHighFormedRule(SpecRule):
    rule_id = "PA0041"
    rule_name = "Swing High Formed"


def evaluate_pa0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0041."""
    return run_spec_rule(PA0041SwingHighFormedRule, df)

"""PA0042 — Swing Low Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0042SwingLowFormedRule(SpecRule):
    rule_id = "PA0042"
    rule_name = "Swing Low Formed"


def evaluate_pa0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0042."""
    return run_spec_rule(PA0042SwingLowFormedRule, df)

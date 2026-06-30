"""BO0046 — Close Below Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0046CloseBelowPriorSwingLowRule(SpecRule):
    rule_id = "BO0046"
    rule_name = "Close Below Prior Swing Low"


def evaluate_bo0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0046."""
    return run_spec_rule(BO0046CloseBelowPriorSwingLowRule, df)

"""BO0008 — Close Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0008CloseBelowPriorLowRule(SpecRule):
    rule_id = "BO0008"
    rule_name = "Close Below Prior Low"


def evaluate_bo0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0008."""
    return run_spec_rule(BO0008CloseBelowPriorLowRule, df)

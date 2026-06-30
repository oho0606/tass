"""GP0012 — Gap Down Open Below Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0012GapDownOpenBelowPriorCloseRule(SpecRule):
    rule_id = "GP0012"
    rule_name = "Gap Down Open Below Prior Close"


def evaluate_gp0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0012."""
    return run_spec_rule(GP0012GapDownOpenBelowPriorCloseRule, df)

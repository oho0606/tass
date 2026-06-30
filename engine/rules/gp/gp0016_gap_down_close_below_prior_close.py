"""GP0016 — Gap Down Close Below Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0016GapDownCloseBelowPriorCloseRule(SpecRule):
    rule_id = "GP0016"
    rule_name = "Gap Down Close Below Prior Close"


def evaluate_gp0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0016."""
    return run_spec_rule(GP0016GapDownCloseBelowPriorCloseRule, df)

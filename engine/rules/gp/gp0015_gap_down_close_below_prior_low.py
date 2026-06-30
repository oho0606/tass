"""GP0015 — Gap Down Close Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0015GapDownCloseBelowPriorLowRule(SpecRule):
    rule_id = "GP0015"
    rule_name = "Gap Down Close Below Prior Low"


def evaluate_gp0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0015."""
    return run_spec_rule(GP0015GapDownCloseBelowPriorLowRule, df)

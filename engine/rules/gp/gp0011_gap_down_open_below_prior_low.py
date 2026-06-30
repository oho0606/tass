"""GP0011 — Gap Down Open Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0011GapDownOpenBelowPriorLowRule(SpecRule):
    rule_id = "GP0011"
    rule_name = "Gap Down Open Below Prior Low"


def evaluate_gp0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0011."""
    return run_spec_rule(GP0011GapDownOpenBelowPriorLowRule, df)

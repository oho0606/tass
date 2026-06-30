"""GP0014 — Gap Down High Below Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0014GapDownHighBelowPriorCloseRule(SpecRule):
    rule_id = "GP0014"
    rule_name = "Gap Down High Below Prior Close"


def evaluate_gp0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0014."""
    return run_spec_rule(GP0014GapDownHighBelowPriorCloseRule, df)

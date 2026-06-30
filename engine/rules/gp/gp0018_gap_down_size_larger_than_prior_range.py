"""GP0018 — Gap Down Size Larger Than Prior Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0018GapDownSizeLargerThanPriorRangeRule(SpecRule):
    rule_id = "GP0018"
    rule_name = "Gap Down Size Larger Than Prior Range"


def evaluate_gp0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0018."""
    return run_spec_rule(GP0018GapDownSizeLargerThanPriorRangeRule, df)

"""GP0008 — Gap Up Size Larger Than Prior Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0008GapUpSizeLargerThanPriorRangeRule(SpecRule):
    rule_id = "GP0008"
    rule_name = "Gap Up Size Larger Than Prior Range"


def evaluate_gp0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0008."""
    return run_spec_rule(GP0008GapUpSizeLargerThanPriorRangeRule, df)

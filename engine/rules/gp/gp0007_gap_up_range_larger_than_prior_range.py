"""GP0007 — Gap Up Range Larger Than Prior Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0007GapUpRangeLargerThanPriorRangeRule(SpecRule):
    rule_id = "GP0007"
    rule_name = "Gap Up Range Larger Than Prior Range"


def evaluate_gp0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0007."""
    return run_spec_rule(GP0007GapUpRangeLargerThanPriorRangeRule, df)

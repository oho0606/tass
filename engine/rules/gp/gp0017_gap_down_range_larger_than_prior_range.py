"""GP0017 — Gap Down Range Larger Than Prior Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0017GapDownRangeLargerThanPriorRangeRule(SpecRule):
    rule_id = "GP0017"
    rule_name = "Gap Down Range Larger Than Prior Range"


def evaluate_gp0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0017."""
    return run_spec_rule(GP0017GapDownRangeLargerThanPriorRangeRule, df)

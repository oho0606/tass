"""GP0013 — Gap Down High Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0013GapDownHighBelowPriorLowRule(SpecRule):
    rule_id = "GP0013"
    rule_name = "Gap Down High Below Prior Low"


def evaluate_gp0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0013."""
    return run_spec_rule(GP0013GapDownHighBelowPriorLowRule, df)

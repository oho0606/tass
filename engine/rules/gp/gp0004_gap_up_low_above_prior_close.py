"""GP0004 — Gap Up Low Above Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0004GapUpLowAbovePriorCloseRule(SpecRule):
    rule_id = "GP0004"
    rule_name = "Gap Up Low Above Prior Close"


def evaluate_gp0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0004."""
    return run_spec_rule(GP0004GapUpLowAbovePriorCloseRule, df)

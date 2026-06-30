"""GP0055 — Gap Unfilled At Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0055GapUnfilledAtCloseRule(SpecRule):
    rule_id = "GP0055"
    rule_name = "Gap Unfilled At Close"


def evaluate_gp0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0055."""
    return run_spec_rule(GP0055GapUnfilledAtCloseRule, df)

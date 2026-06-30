"""GP0053 — Gap Size Exceeds Prior Gap Size. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0053GapSizeExceedsPriorGapSizeRule(SpecRule):
    rule_id = "GP0053"
    rule_name = "Gap Size Exceeds Prior Gap Size"


def evaluate_gp0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0053."""
    return run_spec_rule(GP0053GapSizeExceedsPriorGapSizeRule, df)

"""GP0054 — Gap Size Below Prior Gap Size. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0054GapSizeBelowPriorGapSizeRule(SpecRule):
    rule_id = "GP0054"
    rule_name = "Gap Size Below Prior Gap Size"


def evaluate_gp0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0054."""
    return run_spec_rule(GP0054GapSizeBelowPriorGapSizeRule, df)

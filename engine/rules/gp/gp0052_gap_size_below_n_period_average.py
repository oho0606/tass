"""GP0052 — Gap Size Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0052GapSizeBelowNPeriodAverageRule(SpecRule):
    rule_id = "GP0052"
    rule_name = "Gap Size Below N-Period Average"


def evaluate_gp0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0052."""
    return run_spec_rule(GP0052GapSizeBelowNPeriodAverageRule, df)

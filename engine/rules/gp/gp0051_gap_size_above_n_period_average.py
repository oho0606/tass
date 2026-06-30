"""GP0051 — Gap Size Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0051GapSizeAboveNPeriodAverageRule(SpecRule):
    rule_id = "GP0051"
    rule_name = "Gap Size Above N-Period Average"


def evaluate_gp0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0051."""
    return run_spec_rule(GP0051GapSizeAboveNPeriodAverageRule, df)

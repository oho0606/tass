"""VO0013 — True Range Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0013TrueRangeAboveNPeriodAverageRule(SpecRule):
    rule_id = "VO0013"
    rule_name = "True Range Above N-Period Average"


def evaluate_vo0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0013."""
    return run_spec_rule(VO0013TrueRangeAboveNPeriodAverageRule, df)

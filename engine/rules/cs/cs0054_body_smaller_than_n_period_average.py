"""CS0054 — Body Smaller Than N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0054BodySmallerThanNPeriodAverageRule(SpecRule):
    rule_id = "CS0054"
    rule_name = "Body Smaller Than N-Period Average"


def evaluate_cs0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0054."""
    return run_spec_rule(CS0054BodySmallerThanNPeriodAverageRule, df)

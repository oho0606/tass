"""CS0056 — Range Smaller Than N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0056RangeSmallerThanNPeriodAverageRule(SpecRule):
    rule_id = "CS0056"
    rule_name = "Range Smaller Than N-Period Average"


def evaluate_cs0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0056."""
    return run_spec_rule(CS0056RangeSmallerThanNPeriodAverageRule, df)

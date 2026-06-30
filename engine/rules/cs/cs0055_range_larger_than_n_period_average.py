"""CS0055 — Range Larger Than N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0055RangeLargerThanNPeriodAverageRule(SpecRule):
    rule_id = "CS0055"
    rule_name = "Range Larger Than N-Period Average"


def evaluate_cs0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0055."""
    return run_spec_rule(CS0055RangeLargerThanNPeriodAverageRule, df)

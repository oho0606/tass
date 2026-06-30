"""CS0053 — Body Larger Than N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0053BodyLargerThanNPeriodAverageRule(SpecRule):
    rule_id = "CS0053"
    rule_name = "Body Larger Than N-Period Average"


def evaluate_cs0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0053."""
    return run_spec_rule(CS0053BodyLargerThanNPeriodAverageRule, df)

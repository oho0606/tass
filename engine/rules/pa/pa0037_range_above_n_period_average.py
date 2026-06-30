"""PA0037 — Range Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0037RangeAboveNPeriodAverageRule(SpecRule):
    rule_id = "PA0037"
    rule_name = "Range Above N-Period Average"


def evaluate_pa0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0037."""
    return run_spec_rule(PA0037RangeAboveNPeriodAverageRule, df)

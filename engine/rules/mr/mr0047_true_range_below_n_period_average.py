"""MR0047 — True Range Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0047TrueRangeBelowNPeriodAverageRule(SpecRule):
    rule_id = "MR0047"
    rule_name = "True Range Below N-Period Average"


def evaluate_mr0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0047."""
    return run_spec_rule(MR0047TrueRangeBelowNPeriodAverageRule, df)

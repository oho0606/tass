"""MT0031 — Weekly Daily Close Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0031WeeklyDailyCloseAboveNPeriodHighRule(SpecRule):
    rule_id = "MT0031"
    rule_name = "Weekly Daily Close Above N-Period High"


def evaluate_mt0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0031."""
    return run_spec_rule(MT0031WeeklyDailyCloseAboveNPeriodHighRule, df)

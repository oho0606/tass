"""MT0035 — Weekly Daily Resistance Break. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0035WeeklyDailyResistanceBreakRule(SpecRule):
    rule_id = "MT0035"
    rule_name = "Weekly Daily Resistance Break"


def evaluate_mt0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0035."""
    return run_spec_rule(MT0035WeeklyDailyResistanceBreakRule, df)

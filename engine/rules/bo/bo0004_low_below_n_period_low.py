"""BO0004 — Low Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0004LowBelowNPeriodLowRule(SpecRule):
    rule_id = "BO0004"
    rule_name = "Low Below N-Period Low"


def evaluate_bo0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0004."""
    return run_spec_rule(BO0004LowBelowNPeriodLowRule, df)

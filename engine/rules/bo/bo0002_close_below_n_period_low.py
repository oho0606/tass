"""BO0002 — Close Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0002CloseBelowNPeriodLowRule(SpecRule):
    rule_id = "BO0002"
    rule_name = "Close Below N-Period Low"


def evaluate_bo0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0002."""
    return run_spec_rule(BO0002CloseBelowNPeriodLowRule, df)

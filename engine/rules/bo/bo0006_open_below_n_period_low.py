"""BO0006 — Open Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0006OpenBelowNPeriodLowRule(SpecRule):
    rule_id = "BO0006"
    rule_name = "Open Below N-Period Low"


def evaluate_bo0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0006."""
    return run_spec_rule(BO0006OpenBelowNPeriodLowRule, df)

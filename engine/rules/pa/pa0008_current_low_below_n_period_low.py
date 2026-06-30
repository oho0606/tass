"""PA0008 — Current Low Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0008CurrentLowBelowNPeriodLowRule(SpecRule):
    rule_id = "PA0008"
    rule_name = "Current Low Below N-Period Low"


def evaluate_pa0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0008."""
    return run_spec_rule(PA0008CurrentLowBelowNPeriodLowRule, df)

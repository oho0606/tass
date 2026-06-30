"""PA0010 — Current Low At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0010CurrentLowAtNPeriodLowRule(SpecRule):
    rule_id = "PA0010"
    rule_name = "Current Low At N-Period Low"


def evaluate_pa0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0010."""
    return run_spec_rule(PA0010CurrentLowAtNPeriodLowRule, df)

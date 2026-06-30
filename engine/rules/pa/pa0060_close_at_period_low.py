"""PA0060 — Close At Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0060CloseAtPeriodLowRule(SpecRule):
    rule_id = "PA0060"
    rule_name = "Close At Period Low"


def evaluate_pa0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0060."""
    return run_spec_rule(PA0060CloseAtPeriodLowRule, df)

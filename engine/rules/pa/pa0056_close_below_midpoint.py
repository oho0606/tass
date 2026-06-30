"""PA0056 — Close Below Midpoint. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0056CloseBelowMidpointRule(SpecRule):
    rule_id = "PA0056"
    rule_name = "Close Below Midpoint"


def evaluate_pa0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0056."""
    return run_spec_rule(PA0056CloseBelowMidpointRule, df)

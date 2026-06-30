"""PA0058 — Close Below Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0058CloseBelowPriorCloseRule(SpecRule):
    rule_id = "PA0058"
    rule_name = "Close Below Prior Close"


def evaluate_pa0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0058."""
    return run_spec_rule(PA0058CloseBelowPriorCloseRule, df)

"""PA0054 — Close Near Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0054CloseNearLowRule(SpecRule):
    rule_id = "PA0054"
    rule_name = "Close Near Low"


def evaluate_pa0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0054."""
    return run_spec_rule(PA0054CloseNearLowRule, df)

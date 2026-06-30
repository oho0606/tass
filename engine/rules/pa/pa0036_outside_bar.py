"""PA0036 — Outside Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0036OutsideBarRule(SpecRule):
    rule_id = "PA0036"
    rule_name = "Outside Bar"


def evaluate_pa0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0036."""
    return run_spec_rule(PA0036OutsideBarRule, df)

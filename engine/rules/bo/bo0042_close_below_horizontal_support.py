"""BO0042 — Close Below Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0042CloseBelowHorizontalSupportRule(SpecRule):
    rule_id = "BO0042"
    rule_name = "Close Below Horizontal Support"


def evaluate_bo0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0042."""
    return run_spec_rule(BO0042CloseBelowHorizontalSupportRule, df)

"""EX0053 — Exit Close Near Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0053ExitCloseNearBarLowRule(SpecRule):
    rule_id = "EX0053"
    rule_name = "Exit Close Near Bar Low"


def evaluate_ex0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0053."""
    return run_spec_rule(EX0053ExitCloseNearBarLowRule, df)

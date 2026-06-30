"""EX0031 — Exit Close Below Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0031ExitCloseBelowPriorSwingLowRule(SpecRule):
    rule_id = "EX0031"
    rule_name = "Exit Close Below Prior Swing Low"


def evaluate_ex0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0031."""
    return run_spec_rule(EX0031ExitCloseBelowPriorSwingLowRule, df)

"""EX0021 — Exit Close Below Pullback Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0021ExitCloseBelowPullbackLowRule(SpecRule):
    rule_id = "EX0021"
    rule_name = "Exit Close Below Pullback Low"


def evaluate_ex0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0021."""
    return run_spec_rule(EX0021ExitCloseBelowPullbackLowRule, df)

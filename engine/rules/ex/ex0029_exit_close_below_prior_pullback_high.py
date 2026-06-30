"""EX0029 — Exit Close Below Prior Pullback High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0029ExitCloseBelowPriorPullbackHighRule(SpecRule):
    rule_id = "EX0029"
    rule_name = "Exit Close Below Prior Pullback High"


def evaluate_ex0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0029."""
    return run_spec_rule(EX0029ExitCloseBelowPriorPullbackHighRule, df)

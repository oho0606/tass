"""EX0028 — Exit Bar Following Pullback Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0028ExitBarFollowingPullbackLowRule(SpecRule):
    rule_id = "EX0028"
    rule_name = "Exit Bar Following Pullback Low"


def evaluate_ex0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0028."""
    return run_spec_rule(EX0028ExitBarFollowingPullbackLowRule, df)

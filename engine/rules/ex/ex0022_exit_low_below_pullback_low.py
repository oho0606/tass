"""EX0022 — Exit Low Below Pullback Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0022ExitLowBelowPullbackLowRule(SpecRule):
    rule_id = "EX0022"
    rule_name = "Exit Low Below Pullback Low"


def evaluate_ex0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0022."""
    return run_spec_rule(EX0022ExitLowBelowPullbackLowRule, df)

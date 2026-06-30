"""RK0027 — Gap Up Filled Same Session. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0027GapUpFilledSameSessionRule(SpecRule):
    rule_id = "RK0027"
    rule_name = "Gap Up Filled Same Session"


def evaluate_rk0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0027."""
    return run_spec_rule(RK0027GapUpFilledSameSessionRule, df)

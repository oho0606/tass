"""RK0028 — Gap Down Filled Same Session. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0028GapDownFilledSameSessionRule(SpecRule):
    rule_id = "RK0028"
    rule_name = "Gap Down Filled Same Session"


def evaluate_rk0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0028."""
    return run_spec_rule(RK0028GapDownFilledSameSessionRule, df)

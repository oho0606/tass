"""RK0029 — Gap Up From Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0029GapUpFromPriorHighRule(SpecRule):
    rule_id = "RK0029"
    rule_name = "Gap Up From Prior High"


def evaluate_rk0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0029."""
    return run_spec_rule(RK0029GapUpFromPriorHighRule, df)

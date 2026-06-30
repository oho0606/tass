"""RK0007 — ATR Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0007ATRExpandingRule(SpecRule):
    rule_id = "RK0007"
    rule_name = "ATR Expanding"


def evaluate_rk0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0007."""
    return run_spec_rule(RK0007ATRExpandingRule, df)

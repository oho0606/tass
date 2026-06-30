"""RK0010 — True Range Below ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0010TrueRangeBelowATRRule(SpecRule):
    rule_id = "RK0010"
    rule_name = "True Range Below ATR"


def evaluate_rk0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0010."""
    return run_spec_rule(RK0010TrueRangeBelowATRRule, df)

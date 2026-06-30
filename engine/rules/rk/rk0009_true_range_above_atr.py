"""RK0009 — True Range Above ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0009TrueRangeAboveATRRule(SpecRule):
    rule_id = "RK0009"
    rule_name = "True Range Above ATR"


def evaluate_rk0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0009."""
    return run_spec_rule(RK0009TrueRangeAboveATRRule, df)

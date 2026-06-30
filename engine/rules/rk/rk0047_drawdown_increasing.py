"""RK0047 — Drawdown Increasing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0047DrawdownIncreasingRule(SpecRule):
    rule_id = "RK0047"
    rule_name = "Drawdown Increasing"


def evaluate_rk0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0047."""
    return run_spec_rule(RK0047DrawdownIncreasingRule, df)

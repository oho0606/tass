"""RK0023 — Gap Size Above ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0023GapSizeAboveATRRule(SpecRule):
    rule_id = "RK0023"
    rule_name = "Gap Size Above ATR"


def evaluate_rk0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0023."""
    return run_spec_rule(RK0023GapSizeAboveATRRule, df)

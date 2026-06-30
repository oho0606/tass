"""PB0015 — Pullback Duration Greater Than N Bars. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0015PullbackDurationGreaterThanNBarsRule(SpecRule):
    rule_id = "PB0015"
    rule_name = "Pullback Duration Greater Than N Bars"


def evaluate_pb0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0015."""
    return run_spec_rule(PB0015PullbackDurationGreaterThanNBarsRule, df)

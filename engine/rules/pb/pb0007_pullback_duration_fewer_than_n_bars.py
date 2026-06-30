"""PB0007 — Pullback Duration Fewer Than N Bars. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0007PullbackDurationFewerThanNBarsRule(SpecRule):
    rule_id = "PB0007"
    rule_name = "Pullback Duration Fewer Than N Bars"


def evaluate_pb0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0007."""
    return run_spec_rule(PB0007PullbackDurationFewerThanNBarsRule, df)

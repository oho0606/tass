"""PB0050 — Pullback Within Down Trend Channel. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0050PullbackWithinDownTrendChannelRule(SpecRule):
    rule_id = "PB0050"
    rule_name = "Pullback Within Down Trend Channel"


def evaluate_pb0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0050."""
    return run_spec_rule(PB0050PullbackWithinDownTrendChannelRule, df)

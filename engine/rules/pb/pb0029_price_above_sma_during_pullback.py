"""PB0029 — Price Above SMA During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0029PriceAboveSMADuringPullbackRule(SpecRule):
    rule_id = "PB0029"
    rule_name = "Price Above SMA During Pullback"


def evaluate_pb0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0029."""
    return run_spec_rule(PB0029PriceAboveSMADuringPullbackRule, df)

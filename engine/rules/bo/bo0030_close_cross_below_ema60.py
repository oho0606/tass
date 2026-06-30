"""BO0030 — Close Cross Below EMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0030CloseCrossBelowEMA60Rule(SpecRule):
    rule_id = "BO0030"
    rule_name = "Close Cross Below EMA60"


def evaluate_bo0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0030."""
    return run_spec_rule(BO0030CloseCrossBelowEMA60Rule, df)

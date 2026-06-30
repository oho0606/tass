"""BO0028 — Close Cross Below EMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0028CloseCrossBelowEMA20Rule(SpecRule):
    rule_id = "BO0028"
    rule_name = "Close Cross Below EMA20"


def evaluate_bo0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0028."""
    return run_spec_rule(BO0028CloseCrossBelowEMA20Rule, df)

"""BO0024 — Close Cross Below SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0024CloseCrossBelowSMA20Rule(SpecRule):
    rule_id = "BO0024"
    rule_name = "Close Cross Below SMA20"


def evaluate_bo0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0024."""
    return run_spec_rule(BO0024CloseCrossBelowSMA20Rule, df)

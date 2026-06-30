"""BO0026 — Close Cross Below SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0026CloseCrossBelowSMA60Rule(SpecRule):
    rule_id = "BO0026"
    rule_name = "Close Cross Below SMA60"


def evaluate_bo0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0026."""
    return run_spec_rule(BO0026CloseCrossBelowSMA60Rule, df)

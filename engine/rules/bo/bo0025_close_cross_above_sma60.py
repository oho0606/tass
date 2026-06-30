"""BO0025 — Close Cross Above SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0025CloseCrossAboveSMA60Rule(SpecRule):
    rule_id = "BO0025"
    rule_name = "Close Cross Above SMA60"


def evaluate_bo0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0025."""
    return run_spec_rule(BO0025CloseCrossAboveSMA60Rule, df)

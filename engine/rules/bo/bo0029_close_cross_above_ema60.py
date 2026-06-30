"""BO0029 — Close Cross Above EMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0029CloseCrossAboveEMA60Rule(SpecRule):
    rule_id = "BO0029"
    rule_name = "Close Cross Above EMA60"


def evaluate_bo0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0029."""
    return run_spec_rule(BO0029CloseCrossAboveEMA60Rule, df)

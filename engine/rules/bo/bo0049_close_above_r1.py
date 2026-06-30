"""BO0049 — Close Above R1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0049CloseAboveR1Rule(SpecRule):
    rule_id = "BO0049"
    rule_name = "Close Above R1"


def evaluate_bo0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0049."""
    return run_spec_rule(BO0049CloseAboveR1Rule, df)

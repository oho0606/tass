"""BO0050 — Close Below S1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0050CloseBelowS1Rule(SpecRule):
    rule_id = "BO0050"
    rule_name = "Close Below S1"


def evaluate_bo0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0050."""
    return run_spec_rule(BO0050CloseBelowS1Rule, df)

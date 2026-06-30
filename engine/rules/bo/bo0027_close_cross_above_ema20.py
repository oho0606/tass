"""BO0027 — Close Cross Above EMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0027CloseCrossAboveEMA20Rule(SpecRule):
    rule_id = "BO0027"
    rule_name = "Close Cross Above EMA20"


def evaluate_bo0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0027."""
    return run_spec_rule(BO0027CloseCrossAboveEMA20Rule, df)

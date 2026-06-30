"""BO0023 — Close Cross Above SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0023CloseCrossAboveSMA20Rule(SpecRule):
    rule_id = "BO0023"
    rule_name = "Close Cross Above SMA20"


def evaluate_bo0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0023."""
    return run_spec_rule(BO0023CloseCrossAboveSMA20Rule, df)

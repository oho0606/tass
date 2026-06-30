"""BO0021 — Close Cross Above SMA5. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0021CloseCrossAboveSMA5Rule(SpecRule):
    rule_id = "BO0021"
    rule_name = "Close Cross Above SMA5"


def evaluate_bo0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0021."""
    return run_spec_rule(BO0021CloseCrossAboveSMA5Rule, df)

"""BO0001 — Close Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0001CloseAboveNPeriodHighRule(SpecRule):
    rule_id = "BO0001"
    rule_name = "Close Above N-Period High"


def evaluate_bo0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0001."""
    return run_spec_rule(BO0001CloseAboveNPeriodHighRule, df)

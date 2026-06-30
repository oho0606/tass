"""BO0007 — Close Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0007CloseAbovePriorHighRule(SpecRule):
    rule_id = "BO0007"
    rule_name = "Close Above Prior High"


def evaluate_bo0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0007."""
    return run_spec_rule(BO0007CloseAbovePriorHighRule, df)

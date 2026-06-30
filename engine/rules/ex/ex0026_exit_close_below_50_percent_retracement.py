"""EX0026 — Exit Close Below 50 Percent Retracement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0026ExitCloseBelow50PercentRetracementRule(SpecRule):
    rule_id = "EX0026"
    rule_name = "Exit Close Below 50 Percent Retracement"


def evaluate_ex0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0026."""
    return run_spec_rule(EX0026ExitCloseBelow50PercentRetracementRule, df)

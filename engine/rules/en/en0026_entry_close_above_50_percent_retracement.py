"""EN0026 — Entry Close Above 50 Percent Retracement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0026EntryCloseAbove50PercentRetracementRule(SpecRule):
    rule_id = "EN0026"
    rule_name = "Entry Close Above 50 Percent Retracement"


def evaluate_en0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0026."""
    return run_spec_rule(EN0026EntryCloseAbove50PercentRetracementRule, df)

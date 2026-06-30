"""EN0025 — Entry Close Above 38.2 Percent Retracement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0025EntryCloseAbove382PercentRetracementRule(SpecRule):
    rule_id = "EN0025"
    rule_name = "Entry Close Above 38.2 Percent Retracement"


def evaluate_en0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0025."""
    return run_spec_rule(EN0025EntryCloseAbove382PercentRetracementRule, df)

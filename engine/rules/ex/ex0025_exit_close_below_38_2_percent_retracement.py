"""EX0025 — Exit Close Below 38.2 Percent Retracement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0025ExitCloseBelow382PercentRetracementRule(SpecRule):
    rule_id = "EX0025"
    rule_name = "Exit Close Below 38.2 Percent Retracement"


def evaluate_ex0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0025."""
    return run_spec_rule(EX0025ExitCloseBelow382PercentRetracementRule, df)

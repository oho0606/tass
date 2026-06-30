"""PT0045 — Double Top Peaks Equal. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0045DoubleTopPeaksEqualRule(SpecRule):
    rule_id = "PT0045"
    rule_name = "Double Top Peaks Equal"


def evaluate_pt0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0045."""
    return run_spec_rule(PT0045DoubleTopPeaksEqualRule, df)

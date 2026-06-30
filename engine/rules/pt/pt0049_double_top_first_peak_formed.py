"""PT0049 — Double Top First Peak Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0049DoubleTopFirstPeakFormedRule(SpecRule):
    rule_id = "PT0049"
    rule_name = "Double Top First Peak Formed"


def evaluate_pt0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0049."""
    return run_spec_rule(PT0049DoubleTopFirstPeakFormedRule, df)

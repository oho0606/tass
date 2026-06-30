"""EN0031 — Entry Close Above Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0031EntryCloseAbovePriorSwingLowRule(SpecRule):
    rule_id = "EN0031"
    rule_name = "Entry Close Above Prior Swing Low"


def evaluate_en0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0031."""
    return run_spec_rule(EN0031EntryCloseAbovePriorSwingLowRule, df)

"""EN0021 — Entry Close Above Pullback Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0021EntryCloseAbovePullbackLowRule(SpecRule):
    rule_id = "EN0021"
    rule_name = "Entry Close Above Pullback Low"


def evaluate_en0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0021."""
    return run_spec_rule(EN0021EntryCloseAbovePullbackLowRule, df)

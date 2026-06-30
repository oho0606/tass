"""EN0029 — Entry Close Above Prior Pullback High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0029EntryCloseAbovePriorPullbackHighRule(SpecRule):
    rule_id = "EN0029"
    rule_name = "Entry Close Above Prior Pullback High"


def evaluate_en0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0029."""
    return run_spec_rule(EN0029EntryCloseAbovePriorPullbackHighRule, df)

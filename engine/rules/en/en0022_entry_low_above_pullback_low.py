"""EN0022 — Entry Low Above Pullback Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0022EntryLowAbovePullbackLowRule(SpecRule):
    rule_id = "EN0022"
    rule_name = "Entry Low Above Pullback Low"


def evaluate_en0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0022."""
    return run_spec_rule(EN0022EntryLowAbovePullbackLowRule, df)

"""EN0035 — Entry Close Above Support Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0035EntryCloseAboveSupportLevelRule(SpecRule):
    rule_id = "EN0035"
    rule_name = "Entry Close Above Support Level"


def evaluate_en0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0035."""
    return run_spec_rule(EN0035EntryCloseAboveSupportLevelRule, df)

"""EN0030 — Entry Low At Pullback Support Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0030EntryLowAtPullbackSupportLevelRule(SpecRule):
    rule_id = "EN0030"
    rule_name = "Entry Low At Pullback Support Level"


def evaluate_en0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0030."""
    return run_spec_rule(EN0030EntryLowAtPullbackSupportLevelRule, df)

"""EN0057 — Entry Bar Overlapping Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0057EntryBarOverlappingPriorBarRule(SpecRule):
    rule_id = "EN0057"
    rule_name = "Entry Bar Overlapping Prior Bar"


def evaluate_en0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0057."""
    return run_spec_rule(EN0057EntryBarOverlappingPriorBarRule, df)

"""EN0051 — Entry Bar Wide Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0051EntryBarWideRangeRule(SpecRule):
    rule_id = "EN0051"
    rule_name = "Entry Bar Wide Range"


def evaluate_en0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0051."""
    return run_spec_rule(EN0051EntryBarWideRangeRule, df)

"""EN0006 — Entry Low Above Prior Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0006EntryLowAbovePriorBarLowRule(SpecRule):
    rule_id = "EN0006"
    rule_name = "Entry Low Above Prior Bar Low"


def evaluate_en0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0006."""
    return run_spec_rule(EN0006EntryLowAbovePriorBarLowRule, df)

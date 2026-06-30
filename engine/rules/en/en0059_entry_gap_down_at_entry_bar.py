"""EN0059 — Entry Gap Down At Entry Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0059EntryGapDownAtEntryBarRule(SpecRule):
    rule_id = "EN0059"
    rule_name = "Entry Gap Down At Entry Bar"


def evaluate_en0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0059."""
    return run_spec_rule(EN0059EntryGapDownAtEntryBarRule, df)

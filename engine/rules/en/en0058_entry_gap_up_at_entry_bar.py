"""EN0058 — Entry Gap Up At Entry Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0058EntryGapUpAtEntryBarRule(SpecRule):
    rule_id = "EN0058"
    rule_name = "Entry Gap Up At Entry Bar"


def evaluate_en0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0058."""
    return run_spec_rule(EN0058EntryGapUpAtEntryBarRule, df)

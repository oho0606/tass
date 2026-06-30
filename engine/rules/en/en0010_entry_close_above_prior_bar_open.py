"""EN0010 — Entry Close Above Prior Bar Open. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0010EntryCloseAbovePriorBarOpenRule(SpecRule):
    rule_id = "EN0010"
    rule_name = "Entry Close Above Prior Bar Open"


def evaluate_en0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0010."""
    return run_spec_rule(EN0010EntryCloseAbovePriorBarOpenRule, df)

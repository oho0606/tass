"""EN0011 — Entry Close Above Prior Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0011EntryCloseAbovePriorSwingHighRule(SpecRule):
    rule_id = "EN0011"
    rule_name = "Entry Close Above Prior Swing High"


def evaluate_en0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0011."""
    return run_spec_rule(EN0011EntryCloseAbovePriorSwingHighRule, df)

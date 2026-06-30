"""EN0032 — Entry Close Below Prior Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0032EntryCloseBelowPriorSwingHighRule(SpecRule):
    rule_id = "EN0032"
    rule_name = "Entry Close Below Prior Swing High"


def evaluate_en0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0032."""
    return run_spec_rule(EN0032EntryCloseBelowPriorSwingHighRule, df)

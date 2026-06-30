"""SR0054 — Resistance Level First Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0054ResistanceLevelFirstTouchRule(SpecRule):
    rule_id = "SR0054"
    rule_name = "Resistance Level First Touch"


def evaluate_sr0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0054."""
    return run_spec_rule(SR0054ResistanceLevelFirstTouchRule, df)

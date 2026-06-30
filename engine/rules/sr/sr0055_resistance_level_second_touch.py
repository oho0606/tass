"""SR0055 — Resistance Level Second Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0055ResistanceLevelSecondTouchRule(SpecRule):
    rule_id = "SR0055"
    rule_name = "Resistance Level Second Touch"


def evaluate_sr0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0055."""
    return run_spec_rule(SR0055ResistanceLevelSecondTouchRule, df)

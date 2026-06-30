"""SR0056 — Resistance Level Multiple Touches. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0056ResistanceLevelMultipleTouchesRule(SpecRule):
    rule_id = "SR0056"
    rule_name = "Resistance Level Multiple Touches"


def evaluate_sr0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0056."""
    return run_spec_rule(SR0056ResistanceLevelMultipleTouchesRule, df)

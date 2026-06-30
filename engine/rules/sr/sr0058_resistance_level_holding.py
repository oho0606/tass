"""SR0058 — Resistance Level Holding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0058ResistanceLevelHoldingRule(SpecRule):
    rule_id = "SR0058"
    rule_name = "Resistance Level Holding"


def evaluate_sr0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0058."""
    return run_spec_rule(SR0058ResistanceLevelHoldingRule, df)

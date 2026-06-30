"""SR0018 — Swing High As Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0018SwingHighAsHorizontalResistanceRule(SpecRule):
    rule_id = "SR0018"
    rule_name = "Swing High As Horizontal Resistance"


def evaluate_sr0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0018."""
    return run_spec_rule(SR0018SwingHighAsHorizontalResistanceRule, df)

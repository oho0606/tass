"""SR0008 — Swing Low As Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0008SwingLowAsHorizontalSupportRule(SpecRule):
    rule_id = "SR0008"
    rule_name = "Swing Low As Horizontal Support"


def evaluate_sr0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0008."""
    return run_spec_rule(SR0008SwingLowAsHorizontalSupportRule, df)

"""MS0034 — BOS Below Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0034BOSBelowSwingLowRule(SpecRule):
    rule_id = "MS0034"
    rule_name = "BOS Below Swing Low"


def evaluate_ms0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0034."""
    return run_spec_rule(MS0034BOSBelowSwingLowRule, df)

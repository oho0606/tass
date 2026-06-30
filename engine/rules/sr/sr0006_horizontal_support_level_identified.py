"""SR0006 — Horizontal Support Level Identified. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0006HorizontalSupportLevelIdentifiedRule(SpecRule):
    rule_id = "SR0006"
    rule_name = "Horizontal Support Level Identified"


def evaluate_sr0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0006."""
    return run_spec_rule(SR0006HorizontalSupportLevelIdentifiedRule, df)

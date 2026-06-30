"""SR0016 — Horizontal Resistance Level Identified. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0016HorizontalResistanceLevelIdentifiedRule(SpecRule):
    rule_id = "SR0016"
    rule_name = "Horizontal Resistance Level Identified"


def evaluate_sr0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0016."""
    return run_spec_rule(SR0016HorizontalResistanceLevelIdentifiedRule, df)

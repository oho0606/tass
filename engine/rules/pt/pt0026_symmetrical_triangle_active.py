"""PT0026 — Symmetrical Triangle Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0026SymmetricalTriangleActiveRule(SpecRule):
    rule_id = "PT0026"
    rule_name = "Symmetrical Triangle Active"


def evaluate_pt0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0026."""
    return run_spec_rule(PT0026SymmetricalTriangleActiveRule, df)

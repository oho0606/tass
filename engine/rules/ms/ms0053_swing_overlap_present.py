"""MS0053 — Swing Overlap Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0053SwingOverlapPresentRule(SpecRule):
    rule_id = "MS0053"
    rule_name = "Swing Overlap Present"


def evaluate_ms0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0053."""
    return run_spec_rule(MS0053SwingOverlapPresentRule, df)

"""MS0025 — Swing High Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0025SwingHighActiveRule(SpecRule):
    rule_id = "MS0025"
    rule_name = "Swing High Active"


def evaluate_ms0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0025."""
    return run_spec_rule(MS0025SwingHighActiveRule, df)

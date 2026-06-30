"""DQ0046 — Tick Size Violation. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0046TickSizeViolationRule(SpecRule):
    rule_id = "DQ0046"
    rule_name = "Tick Size Violation"


def evaluate_dq0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0046."""
    return run_spec_rule(DQ0046TickSizeViolationRule, df)

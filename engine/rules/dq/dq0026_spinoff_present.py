"""DQ0026 — Spinoff Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0026SpinoffPresentRule(SpecRule):
    rule_id = "DQ0026"
    rule_name = "Spinoff Present"


def evaluate_dq0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0026."""
    return run_spec_rule(DQ0026SpinoffPresentRule, df)

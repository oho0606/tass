"""DQ0017 — Duplicate Timestamp. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0017DuplicateTimestampRule(SpecRule):
    rule_id = "DQ0017"
    rule_name = "Duplicate Timestamp"


def evaluate_dq0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0017."""
    return run_spec_rule(DQ0017DuplicateTimestampRule, df)

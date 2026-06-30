"""DQ0036 — Low Volume Session. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0036LowVolumeSessionRule(SpecRule):
    rule_id = "DQ0036"
    rule_name = "Low Volume Session"


def evaluate_dq0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0036."""
    return run_spec_rule(DQ0036LowVolumeSessionRule, df)

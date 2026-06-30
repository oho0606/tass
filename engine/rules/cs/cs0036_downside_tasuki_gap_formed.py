"""CS0036 — Downside Tasuki Gap Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0036DownsideTasukiGapFormedRule(SpecRule):
    rule_id = "CS0036"
    rule_name = "Downside Tasuki Gap Formed"


def evaluate_cs0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0036."""
    return run_spec_rule(CS0036DownsideTasukiGapFormedRule, df)

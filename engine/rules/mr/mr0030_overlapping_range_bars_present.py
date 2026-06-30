"""MR0030 — Overlapping Range Bars Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0030OverlappingRangeBarsPresentRule(SpecRule):
    rule_id = "MR0030"
    rule_name = "Overlapping Range Bars Present"


def evaluate_mr0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0030."""
    return run_spec_rule(MR0030OverlappingRangeBarsPresentRule, df)

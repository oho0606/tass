"""CS0013 — Bearish Marubozu Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0013BearishMarubozuFormedRule(SpecRule):
    rule_id = "CS0013"
    rule_name = "Bearish Marubozu Formed"


def evaluate_cs0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0013."""
    return run_spec_rule(CS0013BearishMarubozuFormedRule, df)

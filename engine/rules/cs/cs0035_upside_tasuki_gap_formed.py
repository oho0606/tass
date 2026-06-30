"""CS0035 — Upside Tasuki Gap Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0035UpsideTasukiGapFormedRule(SpecRule):
    rule_id = "CS0035"
    rule_name = "Upside Tasuki Gap Formed"


def evaluate_cs0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0035."""
    return run_spec_rule(CS0035UpsideTasukiGapFormedRule, df)

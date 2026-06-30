"""CS0018 — Bearish Harami Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0018BearishHaramiFormedRule(SpecRule):
    rule_id = "CS0018"
    rule_name = "Bearish Harami Formed"


def evaluate_cs0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0018."""
    return run_spec_rule(CS0018BearishHaramiFormedRule, df)

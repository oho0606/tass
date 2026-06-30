"""CS0020 — Bearish Kicker Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0020BearishKickerFormedRule(SpecRule):
    rule_id = "CS0020"
    rule_name = "Bearish Kicker Formed"


def evaluate_cs0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0020."""
    return run_spec_rule(CS0020BearishKickerFormedRule, df)

"""CS0021 — Tweezer Bottom Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0021TweezerBottomFormedRule(SpecRule):
    rule_id = "CS0021"
    rule_name = "Tweezer Bottom Formed"


def evaluate_cs0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0021."""
    return run_spec_rule(CS0021TweezerBottomFormedRule, df)

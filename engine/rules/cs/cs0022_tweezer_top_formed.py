"""CS0022 — Tweezer Top Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0022TweezerTopFormedRule(SpecRule):
    rule_id = "CS0022"
    rule_name = "Tweezer Top Formed"


def evaluate_cs0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0022."""
    return run_spec_rule(CS0022TweezerTopFormedRule, df)

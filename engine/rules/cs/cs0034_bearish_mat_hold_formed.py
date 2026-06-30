"""CS0034 — Bearish Mat Hold Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0034BearishMatHoldFormedRule(SpecRule):
    rule_id = "CS0034"
    rule_name = "Bearish Mat Hold Formed"


def evaluate_cs0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0034."""
    return run_spec_rule(CS0034BearishMatHoldFormedRule, df)

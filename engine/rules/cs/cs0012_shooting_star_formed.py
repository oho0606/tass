"""CS0012 — Shooting Star Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0012ShootingStarFormedRule(SpecRule):
    rule_id = "CS0012"
    rule_name = "Shooting Star Formed"


def evaluate_cs0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0012."""
    return run_spec_rule(CS0012ShootingStarFormedRule, df)

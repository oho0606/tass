"""CS0047 — Spinning Top Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0047SpinningTopFormedRule(SpecRule):
    rule_id = "CS0047"
    rule_name = "Spinning Top Formed"


def evaluate_cs0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0047."""
    return run_spec_rule(CS0047SpinningTopFormedRule, df)

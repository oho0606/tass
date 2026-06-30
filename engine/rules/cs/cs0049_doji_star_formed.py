"""CS0049 — Doji Star Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0049DojiStarFormedRule(SpecRule):
    rule_id = "CS0049"
    rule_name = "Doji Star Formed"


def evaluate_cs0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0049."""
    return run_spec_rule(CS0049DojiStarFormedRule, df)

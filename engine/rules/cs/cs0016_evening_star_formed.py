"""CS0016 — Evening Star Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0016EveningStarFormedRule(SpecRule):
    rule_id = "CS0016"
    rule_name = "Evening Star Formed"


def evaluate_cs0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0016."""
    return run_spec_rule(CS0016EveningStarFormedRule, df)

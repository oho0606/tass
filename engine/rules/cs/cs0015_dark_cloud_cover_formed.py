"""CS0015 — Dark Cloud Cover Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0015DarkCloudCoverFormedRule(SpecRule):
    rule_id = "CS0015"
    rule_name = "Dark Cloud Cover Formed"


def evaluate_cs0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0015."""
    return run_spec_rule(CS0015DarkCloudCoverFormedRule, df)

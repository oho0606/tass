"""CS0030 — Evening Doji Star Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0030EveningDojiStarFormedRule(SpecRule):
    rule_id = "CS0030"
    rule_name = "Evening Doji Star Formed"


def evaluate_cs0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0030."""
    return run_spec_rule(CS0030EveningDojiStarFormedRule, df)

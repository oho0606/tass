"""CS0029 — Morning Doji Star Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0029MorningDojiStarFormedRule(SpecRule):
    rule_id = "CS0029"
    rule_name = "Morning Doji Star Formed"


def evaluate_cs0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0029."""
    return run_spec_rule(CS0029MorningDojiStarFormedRule, df)

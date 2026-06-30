"""EX0047 — Exit Bar Bearish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0047ExitBarBearishRule(SpecRule):
    rule_id = "EX0047"
    rule_name = "Exit Bar Bearish"


def evaluate_ex0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0047."""
    return run_spec_rule(EX0047ExitBarBearishRule, df)

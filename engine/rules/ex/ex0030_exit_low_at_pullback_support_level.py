"""EX0030 — Exit Low At Pullback Support Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0030ExitLowAtPullbackSupportLevelRule(SpecRule):
    rule_id = "EX0030"
    rule_name = "Exit Low At Pullback Support Level"


def evaluate_ex0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0030."""
    return run_spec_rule(EX0030ExitLowAtPullbackSupportLevelRule, df)

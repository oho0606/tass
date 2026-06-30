"""EX0020 — Exit Close Above S1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0020ExitCloseAboveS1Rule(SpecRule):
    rule_id = "EX0020"
    rule_name = "Exit Close Above S1"


def evaluate_ex0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0020."""
    return run_spec_rule(EX0020ExitCloseAboveS1Rule, df)

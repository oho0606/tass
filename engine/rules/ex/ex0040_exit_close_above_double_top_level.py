"""EX0040 — Exit Close Above Double Top Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0040ExitCloseAboveDoubleTopLevelRule(SpecRule):
    rule_id = "EX0040"
    rule_name = "Exit Close Above Double Top Level"


def evaluate_ex0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0040."""
    return run_spec_rule(EX0040ExitCloseAboveDoubleTopLevelRule, df)

"""EX0058 — Exit Gap Down At Exit Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0058ExitGapDownAtExitBarRule(SpecRule):
    rule_id = "EX0058"
    rule_name = "Exit Gap Down At Exit Bar"


def evaluate_ex0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0058."""
    return run_spec_rule(EX0058ExitGapDownAtExitBarRule, df)

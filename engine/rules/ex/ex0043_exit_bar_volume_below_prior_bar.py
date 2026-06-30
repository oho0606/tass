"""EX0043 — Exit Bar Volume Below Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0043ExitBarVolumeBelowPriorBarRule(SpecRule):
    rule_id = "EX0043"
    rule_name = "Exit Bar Volume Below Prior Bar"


def evaluate_ex0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0043."""
    return run_spec_rule(EX0043ExitBarVolumeBelowPriorBarRule, df)

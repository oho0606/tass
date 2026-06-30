"""EX0012 — Exit Close Above Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0012ExitCloseAbovePriorSwingLowRule(SpecRule):
    rule_id = "EX0012"
    rule_name = "Exit Close Above Prior Swing Low"


def evaluate_ex0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0012."""
    return run_spec_rule(EX0012ExitCloseAbovePriorSwingLowRule, df)

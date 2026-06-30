"""EX0034 — Exit High At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0034ExitHighAtNPeriodHighRule(SpecRule):
    rule_id = "EX0034"
    rule_name = "Exit High At N-Period High"


def evaluate_ex0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0034."""
    return run_spec_rule(EX0034ExitHighAtNPeriodHighRule, df)

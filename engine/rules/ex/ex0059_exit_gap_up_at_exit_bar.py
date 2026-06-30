"""EX0059 — Exit Gap Up At Exit Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0059ExitGapUpAtExitBarRule(SpecRule):
    rule_id = "EX0059"
    rule_name = "Exit Gap Up At Exit Bar"


def evaluate_ex0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0059."""
    return run_spec_rule(EX0059ExitGapUpAtExitBarRule, df)

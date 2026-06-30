"""EX0035 — Exit Close Below Support Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0035ExitCloseBelowSupportLevelRule(SpecRule):
    rule_id = "EX0035"
    rule_name = "Exit Close Below Support Level"


def evaluate_ex0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0035."""
    return run_spec_rule(EX0035ExitCloseBelowSupportLevelRule, df)

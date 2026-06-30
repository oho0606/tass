"""BO0044 — Low Below Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0044LowBelowHorizontalSupportRule(SpecRule):
    rule_id = "BO0044"
    rule_name = "Low Below Horizontal Support"


def evaluate_bo0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0044."""
    return run_spec_rule(BO0044LowBelowHorizontalSupportRule, df)

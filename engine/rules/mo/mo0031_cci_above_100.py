"""MO0031 — CCI Above 100. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0031CCIAbove100Rule(SpecRule):
    rule_id = "MO0031"
    rule_name = "CCI Above 100"


def evaluate_mo0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0031."""
    return run_spec_rule(MO0031CCIAbove100Rule, df)

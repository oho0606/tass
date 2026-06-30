"""MO0032 — CCI Below Negative 100. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0032CCIBelowNegative100Rule(SpecRule):
    rule_id = "MO0032"
    rule_name = "CCI Below Negative 100"


def evaluate_mo0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0032."""
    return run_spec_rule(MO0032CCIBelowNegative100Rule, df)

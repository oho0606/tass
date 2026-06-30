"""MO0039 — CCI Cross Above 100. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0039CCICrossAbove100Rule(SpecRule):
    rule_id = "MO0039"
    rule_name = "CCI Cross Above 100"


def evaluate_mo0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0039."""
    return run_spec_rule(MO0039CCICrossAbove100Rule, df)

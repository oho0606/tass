"""MO0037 — CCI Cross Above Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0037CCICrossAboveZeroRule(SpecRule):
    rule_id = "MO0037"
    rule_name = "CCI Cross Above Zero"


def evaluate_mo0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0037."""
    return run_spec_rule(MO0037CCICrossAboveZeroRule, df)

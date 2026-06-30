"""MO0038 — CCI Cross Below Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0038CCICrossBelowZeroRule(SpecRule):
    rule_id = "MO0038"
    rule_name = "CCI Cross Below Zero"


def evaluate_mo0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0038."""
    return run_spec_rule(MO0038CCICrossBelowZeroRule, df)

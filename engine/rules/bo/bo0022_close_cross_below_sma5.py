"""BO0022 — Close Cross Below SMA5. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0022CloseCrossBelowSMA5Rule(SpecRule):
    rule_id = "BO0022"
    rule_name = "Close Cross Below SMA5"


def evaluate_bo0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0022."""
    return run_spec_rule(BO0022CloseCrossBelowSMA5Rule, df)

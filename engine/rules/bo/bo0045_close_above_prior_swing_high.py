"""BO0045 — Close Above Prior Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0045CloseAbovePriorSwingHighRule(SpecRule):
    rule_id = "BO0045"
    rule_name = "Close Above Prior Swing High"


def evaluate_bo0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0045."""
    return run_spec_rule(BO0045CloseAbovePriorSwingHighRule, df)

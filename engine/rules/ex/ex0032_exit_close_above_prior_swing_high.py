"""EX0032 — Exit Close Above Prior Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0032ExitCloseAbovePriorSwingHighRule(SpecRule):
    rule_id = "EX0032"
    rule_name = "Exit Close Above Prior Swing High"


def evaluate_ex0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0032."""
    return run_spec_rule(EX0032ExitCloseAbovePriorSwingHighRule, df)

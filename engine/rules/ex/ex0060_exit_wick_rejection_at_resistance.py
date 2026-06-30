"""EX0060 — Exit Wick Rejection At Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0060ExitWickRejectionAtResistanceRule(SpecRule):
    rule_id = "EX0060"
    rule_name = "Exit Wick Rejection At Resistance"


def evaluate_ex0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0060."""
    return run_spec_rule(EX0060ExitWickRejectionAtResistanceRule, df)

"""PB0058 — Pullback Wick Rejection At Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0058PullbackWickRejectionAtSupportRule(SpecRule):
    rule_id = "PB0058"
    rule_name = "Pullback Wick Rejection At Support"


def evaluate_pb0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0058."""
    return run_spec_rule(PB0058PullbackWickRejectionAtSupportRule, df)

"""PT0017 — Rounding Top Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0017RoundingTopActiveRule(SpecRule):
    rule_id = "PT0017"
    rule_name = "Rounding Top Active"


def evaluate_pt0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0017."""
    return run_spec_rule(PT0017RoundingTopActiveRule, df)

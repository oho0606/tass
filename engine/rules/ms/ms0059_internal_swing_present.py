"""MS0059 — Internal Swing Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0059InternalSwingPresentRule(SpecRule):
    rule_id = "MS0059"
    rule_name = "Internal Swing Present"


def evaluate_ms0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0059."""
    return run_spec_rule(MS0059InternalSwingPresentRule, df)

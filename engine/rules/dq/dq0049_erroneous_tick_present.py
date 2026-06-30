"""DQ0049 — Erroneous Tick Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0049ErroneousTickPresentRule(SpecRule):
    rule_id = "DQ0049"
    rule_name = "Erroneous Tick Present"


def evaluate_dq0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0049."""
    return run_spec_rule(DQ0049ErroneousTickPresentRule, df)

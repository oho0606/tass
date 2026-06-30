"""DQ0025 — Merger Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0025MergerPresentRule(SpecRule):
    rule_id = "DQ0025"
    rule_name = "Merger Present"


def evaluate_dq0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0025."""
    return run_spec_rule(DQ0025MergerPresentRule, df)

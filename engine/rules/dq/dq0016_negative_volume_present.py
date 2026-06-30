"""DQ0016 — Negative Volume Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0016NegativeVolumePresentRule(SpecRule):
    rule_id = "DQ0016"
    rule_name = "Negative Volume Present"


def evaluate_dq0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0016."""
    return run_spec_rule(DQ0016NegativeVolumePresentRule, df)

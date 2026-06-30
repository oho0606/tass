"""MO0050 — MFI Cross Below 20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0050MFICrossBelow20Rule(SpecRule):
    rule_id = "MO0050"
    rule_name = "MFI Cross Below 20"


def evaluate_mo0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0050."""
    return run_spec_rule(MO0050MFICrossBelow20Rule, df)

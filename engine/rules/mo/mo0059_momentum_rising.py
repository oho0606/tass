"""MO0059 — Momentum Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0059MomentumRisingRule(SpecRule):
    rule_id = "MO0059"
    rule_name = "Momentum Rising"


def evaluate_mo0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0059."""
    return run_spec_rule(MO0059MomentumRisingRule, df)

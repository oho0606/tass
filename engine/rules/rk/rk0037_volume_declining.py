"""RK0037 — Volume Declining. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0037VolumeDecliningRule(SpecRule):
    rule_id = "RK0037"
    rule_name = "Volume Declining"


def evaluate_rk0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0037."""
    return run_spec_rule(RK0037VolumeDecliningRule, df)

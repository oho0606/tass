"""CF0014 — Down Bar Volume Confirms Downtrend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0014DownBarVolumeConfirmsDowntrendRule(SpecRule):
    rule_id = "CF0014"
    rule_name = "Down Bar Volume Confirms Downtrend"


def evaluate_cf0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0014."""
    return run_spec_rule(CF0014DownBarVolumeConfirmsDowntrendRule, df)

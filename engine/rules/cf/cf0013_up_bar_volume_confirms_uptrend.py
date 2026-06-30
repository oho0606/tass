"""CF0013 — Up Bar Volume Confirms Uptrend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0013UpBarVolumeConfirmsUptrendRule(SpecRule):
    rule_id = "CF0013"
    rule_name = "Up Bar Volume Confirms Uptrend"


def evaluate_cf0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0013."""
    return run_spec_rule(CF0013UpBarVolumeConfirmsUptrendRule, df)

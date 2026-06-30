"""MT0005 — Daily 4H Uptrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0005Daily4HUptrendMatchRule(SpecRule):
    rule_id = "MT0005"
    rule_name = "Daily 4H Uptrend Match"


def evaluate_mt0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0005."""
    return run_spec_rule(MT0005Daily4HUptrendMatchRule, df)

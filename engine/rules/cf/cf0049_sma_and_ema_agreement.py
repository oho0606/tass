"""CF0049 — SMA And EMA Agreement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0049SMAAndEMAAgreementRule(SpecRule):
    rule_id = "CF0049"
    rule_name = "SMA And EMA Agreement"


def evaluate_cf0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0049."""
    return run_spec_rule(CF0049SMAAndEMAAgreementRule, df)

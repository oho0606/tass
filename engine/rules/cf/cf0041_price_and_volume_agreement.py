"""CF0041 — Price And Volume Agreement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0041PriceAndVolumeAgreementRule(SpecRule):
    rule_id = "CF0041"
    rule_name = "Price And Volume Agreement"


def evaluate_cf0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0041."""
    return run_spec_rule(CF0041PriceAndVolumeAgreementRule, df)

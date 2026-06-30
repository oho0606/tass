"""VL0048 — Price Down Volume Up. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import PriceVolumeAgreementRule, run_confirmation_rule


class VL0048PriceDownVolumeUpRule(PriceVolumeAgreementRule):
    rule_id = "VL0048"
    rule_name = "Price Down Volume Up"
    mode = "down_up"


def evaluate_vl0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0048."""
    return run_confirmation_rule(VL0048PriceDownVolumeUpRule, df)

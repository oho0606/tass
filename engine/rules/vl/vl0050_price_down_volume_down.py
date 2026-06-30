"""VL0050 — Price Down Volume Down. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import PriceVolumeAgreementRule, run_confirmation_rule


class VL0050PriceDownVolumeDownRule(PriceVolumeAgreementRule):
    rule_id = "VL0050"
    rule_name = "Price Down Volume Down"
    mode = "down_down"


def evaluate_vl0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0050."""
    return run_confirmation_rule(VL0050PriceDownVolumeDownRule, df)

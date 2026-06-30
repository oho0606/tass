"""VL0049 — Price Up Volume Down. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import PriceVolumeAgreementRule, run_confirmation_rule


class VL0049PriceUpVolumeDownRule(PriceVolumeAgreementRule):
    rule_id = "VL0049"
    rule_name = "Price Up Volume Down"
    mode = "up_down"


def evaluate_vl0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0049."""
    return run_confirmation_rule(VL0049PriceUpVolumeDownRule, df)

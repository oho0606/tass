"""CCS004 — Continuation Candle Group. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCS004",
    rule_name="Continuation Candle Group",
    atomic_prefix="CS",
    mode="bullish",
)


def evaluate_ccs004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCS004 from atomic rule results."""
    return _RULE.evaluate(atomic)

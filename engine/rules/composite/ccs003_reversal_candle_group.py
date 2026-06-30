"""CCS003 — Reversal Candle Group. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCS003",
    rule_name="Reversal Candle Group",
    atomic_prefix="CS",
    mode="bullish",
)


def evaluate_ccs003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCS003 from atomic rule results."""
    return _RULE.evaluate(atomic)

"""CCS001 — Bullish Candle Group. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCS001",
    rule_name="Bullish Candle Group",
    atomic_prefix="CS",
    mode="bullish",
)


def evaluate_ccs001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCS001 from atomic rule results."""
    return _RULE.evaluate(atomic)

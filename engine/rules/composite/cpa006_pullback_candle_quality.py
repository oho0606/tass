"""CPA006 — Pullback Candle Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA006",
    rule_name="Pullback Candle Quality",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa006(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA006 from atomic rule results."""
    return _RULE.evaluate(atomic)

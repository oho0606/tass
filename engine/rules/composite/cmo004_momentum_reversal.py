"""CMO004 — Momentum Reversal. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO004",
    rule_name="Momentum Reversal",
    atomic_prefix="MO",
    mode="bullish",
)


def evaluate_cmo004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO004 from atomic rule results."""
    return _RULE.evaluate(atomic)

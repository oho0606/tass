"""CMO003 — Momentum Continuation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO003",
    rule_name="Momentum Continuation",
    atomic_prefix="MO",
    mode="bullish",
)


def evaluate_cmo003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO003 from atomic rule results."""
    return _RULE.evaluate(atomic)

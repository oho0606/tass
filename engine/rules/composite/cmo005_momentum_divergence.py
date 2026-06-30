"""CMO005 — Momentum Divergence. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO005",
    rule_name="Momentum Divergence",
    atomic_prefix="MO",
    mode="bullish",
)


def evaluate_cmo005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO005 from atomic rule results."""
    return _RULE.evaluate(atomic)

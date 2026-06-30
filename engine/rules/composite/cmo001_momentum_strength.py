"""CMO001 — Momentum Strength. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO001",
    rule_name="Momentum Strength",
    atomic_prefix="MO",
    mode="bullish",
)


def evaluate_cmo001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO001 from atomic rule results."""
    return _RULE.evaluate(atomic)

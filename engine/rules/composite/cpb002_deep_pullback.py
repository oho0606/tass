"""CPB002 — Deep Pullback. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPB002",
    rule_name="Deep Pullback",
    atomic_prefix="PB",
    mode="bullish",
)


def evaluate_cpb002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPB002 from atomic rule results."""
    return _RULE.evaluate(atomic)

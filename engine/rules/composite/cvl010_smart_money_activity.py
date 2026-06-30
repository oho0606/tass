"""CVL010 — Smart Money Activity. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL010",
    rule_name="Smart Money Activity",
    atomic_prefix="VL",
    mode="bullish",
)


def evaluate_cvl010(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL010 from atomic rule results."""
    return _RULE.evaluate(atomic)

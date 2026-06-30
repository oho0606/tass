"""CMT003 — Timeframe Conflict. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMT003",
    rule_name="Timeframe Conflict",
    atomic_prefix="MT",
    mode="bullish",
)


def evaluate_cmt003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMT003 from atomic rule results."""
    return _RULE.evaluate(atomic)

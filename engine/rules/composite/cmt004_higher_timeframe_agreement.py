"""CMT004 — Higher Timeframe Agreement. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMT004",
    rule_name="Higher Timeframe Agreement",
    atomic_prefix="MT",
    mode="quality",
)


def evaluate_cmt004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMT004 from atomic rule results."""
    return _RULE.evaluate(atomic)

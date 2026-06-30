"""CMT001 — Full Alignment. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMT001",
    rule_name="Full Alignment",
    atomic_prefix="MT",
    mode="quality",
)


def evaluate_cmt001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMT001 from atomic rule results."""
    return _RULE.evaluate(atomic)

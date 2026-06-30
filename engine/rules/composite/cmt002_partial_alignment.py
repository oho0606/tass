"""CMT002 — Partial Alignment. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMT002",
    rule_name="Partial Alignment",
    atomic_prefix="MT",
    mode="quality",
)


def evaluate_cmt002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMT002 from atomic rule results."""
    return _RULE.evaluate(atomic)

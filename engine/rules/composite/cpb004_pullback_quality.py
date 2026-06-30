"""CPB004 — Pullback Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPB004",
    rule_name="Pullback Quality",
    atomic_prefix="PB",
    mode="quality",
)


def evaluate_cpb004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPB004 from atomic rule results."""
    return _RULE.evaluate(atomic)

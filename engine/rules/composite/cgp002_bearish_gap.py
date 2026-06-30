"""CGP002 — Bearish Gap. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CGP002",
    rule_name="Bearish Gap",
    atomic_prefix="GP",
    mode="bearish",
)


def evaluate_cgp002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CGP002 from atomic rule results."""
    return _RULE.evaluate(atomic)

"""CCF004 — Breakout Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCF004",
    rule_name="Breakout Confirmation",
    atomic_prefix="CF",
    mode="quality",
)


def evaluate_ccf004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCF004 from atomic rule results."""
    return _RULE.evaluate(atomic)

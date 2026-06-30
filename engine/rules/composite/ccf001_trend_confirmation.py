"""CCF001 — Trend Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCF001",
    rule_name="Trend Confirmation",
    atomic_prefix="CF",
    mode="quality",
)


def evaluate_ccf001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCF001 from atomic rule results."""
    return _RULE.evaluate(atomic)

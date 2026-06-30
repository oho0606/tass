"""CCS005 — Candle Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCS005",
    rule_name="Candle Quality",
    atomic_prefix="CS",
    mode="quality",
)


def evaluate_ccs005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCS005 from atomic rule results."""
    return _RULE.evaluate(atomic)

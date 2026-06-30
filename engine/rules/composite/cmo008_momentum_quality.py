"""CMO008 — Momentum Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO008",
    rule_name="Momentum Quality",
    atomic_prefix="MO",
    mode="quality",
)


def evaluate_cmo008(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO008 from atomic rule results."""
    return _RULE.evaluate(atomic)

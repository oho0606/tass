"""CPA007 — Swing Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA007",
    rule_name="Swing Quality",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa007(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA007 from atomic rule results."""
    return _RULE.evaluate(atomic)

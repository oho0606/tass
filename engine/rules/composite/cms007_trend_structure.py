"""CMS007 — Trend Structure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS007",
    rule_name="Trend Structure",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms007(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS007 from atomic rule results."""
    return _RULE.evaluate(atomic)

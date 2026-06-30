"""Recommendation reason generation from composite rules."""

from __future__ import annotations

from engine.core.types import ConfidenceResult, RiskResult, RuleResult, TrendEngineResult

_COMPOSITE_REASON_MAP: dict[str, str] = {
    "CTR001": "Strong Trend",
    "CTR002": "Strong Momentum",
    "CTR003": "Strong Trend",
    "CTR004": "Stable Volatility",
    "CTR005": "Strong Trend",
    "CTR008": "Strong Momentum",
    "CTR009": "Strong Trend",
    "CTR010": "Bullish Moving Average",
}

_RULE_NAME_REASONS: dict[str, str] = {
    "Trend Direction": "Strong Trend",
    "Trend Strength": "Strong Momentum",
    "Trend Quality": "Strong Trend",
    "Trend Stability": "Stable Volatility",
    "Trend Continuation": "Strong Trend",
    "Trend Acceleration": "Strong Momentum",
    "Trend Consistency": "Strong Trend",
    "Trend Confirmation": "Bullish Moving Average",
}


def _composite_payload(composites: dict[str, RuleResult]) -> dict[str, dict]:
    breakdown: dict[str, dict] = {}
    for rule_id, result in composites.items():
        breakdown[rule_id] = {
            "verdict": result.verdict,
            "reasons": list(result.reasons),
            "score": result.score,
        }
    return breakdown


def generate_recommendation_reasons(
    trend: TrendEngineResult,
    confidence: ConfidenceResult,
    risk: RiskResult,
) -> list[str]:
    reasons: list[str] = []
    seen: set[str] = set()

    for rule_id, result in trend.composite_results.items():
        if result.verdict != "PASS":
            continue
        label = _COMPOSITE_REASON_MAP.get(rule_id)
        if label and label not in seen:
            reasons.append(label)
            seen.add(label)

    for result in trend.composite_results.values():
        if result.verdict != "PASS":
            continue
        for text in result.reasons:
            mapped = _RULE_NAME_REASONS.get(text.split("—")[0].strip())
            if mapped and mapped not in seen:
                reasons.append(mapped)
                seen.add(mapped)

    if risk.risk_score <= 20.0 and "Low Risk" not in seen:
        reasons.append("Low Risk")
        seen.add("Low Risk")

    if confidence.confidence_score >= 90.0 and "High Confidence" not in seen:
        reasons.append("High Confidence")
        seen.add("High Confidence")

    if not reasons:
        reasons.append("Composite signals evaluated")

    return reasons


def build_composite_breakdown(trend: TrendEngineResult) -> dict[str, dict]:
    return _composite_payload(trend.composite_results)

from __future__ import annotations

from engine.core.types import RuleResult, RuleStatus


def _status_of(result: RuleResult) -> RuleStatus:
    return result.status


def evaluate_trend_structure(atomic: dict[str, RuleResult]) -> RuleResult:
    """TREND-C001: Trend Structure from atomic rule statuses."""
    hh = atomic["TREND-001"].status
    hl = atomic["TREND-002"].status
    lh = atomic["TREND-003"].status
    ll = atomic["TREND-004"].status

    structure_scores = {
        ("PASS", "PASS", "FAIL", "FAIL"): (50.0, "PASS", "Strong Up Trend", "강한 상승 구조"),
        ("PASS", "PASS", "WARN", "FAIL"): (40.0, "PASS", "Up Trend", "상승 추세"),
        ("PASS", "WARN", "WARN", "FAIL"): (30.0, "WARN", "Weak Up Trend", "약한 상승"),
        ("FAIL", "PASS", "PASS", "WARN"): (20.0, "WARN", "Sideways", "횡보 구조"),
        ("FAIL", "FAIL", "PASS", "PASS"): (0.0, "FAIL", "Down Trend", "하락 구조"),
    }

    key = (hh, hl, lh, ll)
    if key in structure_scores:
        score, status, state, reason = structure_scores[key]
    elif all(s == "WARN" for s in key):
        score, status, state, reason = 20.0, "WARN", "Neutral", "중립 구조"
    else:
        bullish = sum(1 for s in (hh, hl) if s == "PASS")
        bearish = sum(1 for s in (lh, ll) if s == "FAIL")
        if bullish >= 1 and bearish >= 1:
            score, status, state, reason = 25.0, "WARN", "Mixed", "혼합 구조"
        elif bullish >= 2:
            score, status, state, reason = 35.0, "PASS", "Up Trend", "상승 우세"
        else:
            score, status, state, reason = 10.0, "WARN", "Weak Down Trend", "약한 하락"

    return RuleResult(
        rule_id="TREND-C001",
        status=status,  # type: ignore[arg-type]
        score=score,
        confidence_delta=3.0 if status == "PASS" else -2.0,
        risk_delta=-2.0 if "Up" in state else 2.0,
        reasons=[reason],
        metadata={"trend_state": state},
    )


def evaluate_trend_quality(atomic: dict[str, RuleResult]) -> RuleResult:
    """TREND-C002: Average atomic quality."""
    scores = [atomic[k].score for k in ("TREND-001", "TREND-002", "TREND-003", "TREND-004")]
    avg = sum(scores) / len(scores)
    composite = min(50.0, avg * 2.5)

    if composite >= 40:
        status, reason = "PASS", "추세 품질 우수"
    elif composite >= 25:
        status, reason = "WARN", "추세 품질 보통"
    else:
        status, reason = "FAIL", "추세 품질 저하"

    return RuleResult(
        rule_id="TREND-C002",
        status=status,  # type: ignore[arg-type]
        score=composite,
        reasons=[reason],
        metadata={"avg_atomic_score": avg},
    )


def evaluate_trend_continuation(atomic: dict[str, RuleResult]) -> RuleResult:
    """TREND-C003: Trend continuation based on HH + HL."""
    hh_score = atomic["TREND-001"].score
    hl_score = atomic["TREND-002"].score
    lh_penalty = max(0, 20 - atomic["TREND-003"].score)

    raw = (hh_score + hl_score) / 2 - lh_penalty * 0.3
    score = max(0.0, min(50.0, raw * 2.5))

    if score >= 35:
        status, reason = "PASS", "추세 지속 신호"
    elif score >= 20:
        status, reason = "WARN", "추세 지속 불확실"
    else:
        status, reason = "FAIL", "추세 지속 실패"

    return RuleResult(
        rule_id="TREND-C003",
        status=status,  # type: ignore[arg-type]
        score=score,
        reasons=[reason],
    )


def evaluate_trend_failure(atomic: dict[str, RuleResult]) -> RuleResult:
    """TREND-C004: Trend failure detection — high score when failure absent."""
    lh = atomic["TREND-003"]
    ll = atomic["TREND-004"]

    failure_signal = (20 - lh.score) + (20 - ll.score)
    score = max(0.0, min(50.0, 50 - failure_signal * 1.25))

    if lh.status == "FAIL" or ll.status == "FAIL":
        status, reason = "FAIL", "추세 실패 감지"
    elif score >= 35:
        status, reason = "PASS", "추세 실패 없음"
    else:
        status, reason = "WARN", "추세 실패 경고"

    return RuleResult(
        rule_id="TREND-C004",
        status=status,  # type: ignore[arg-type]
        score=score,
        reasons=[reason],
        metadata={"failure_signal": failure_signal},
    )

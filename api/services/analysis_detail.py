"""Build analysis detail view model for Explainable AI screen."""

from __future__ import annotations

from api.schemas.analyze import AnalysisDetailResponse, PenaltyItem, RuleAccordionItem
from api.services.state import TassApiState, domain_views_from_pick
from engine.core.types import PickResult


def _build_summary(pick: PickResult) -> str:
    reasons = pick.recommendation_reason or pick.reasons or []
    if reasons:
        return " ".join(reasons[:3])
    return "백엔드 Rule Engine이 통과한 조건을 기반으로 선정된 종목입니다."


def _build_rules(pick: PickResult) -> list[RuleAccordionItem]:
    items: list[RuleAccordionItem] = []
    composite = pick.composite_breakdown or {}
    composite_details: dict[str, str] = {}

    for rule_id, data in composite.items():
        if not isinstance(data, dict) or data.get("verdict") != "PASS":
            continue
        reasons = data.get("reasons") or []
        detail = reasons[0] if reasons else f"{rule_id} 조건을 충족했습니다."
        composite_details[rule_id] = detail
        score = data.get("score")
        items.append(
            RuleAccordionItem(
                title=rule_id,
                score_delta=float(score) if score is not None else None,
                detail=detail,
                passed=True,
            )
        )

    for cond in pick.passed_conditions or []:
        if any(item.title == cond for item in items):
            continue
        items.append(
            RuleAccordionItem(
                title=cond,
                detail=composite_details.get(cond, f"{cond} 조건을 통과했습니다."),
                passed=True,
            )
        )

    return items


def _build_penalties(pick: PickResult) -> list[PenaltyItem]:
    penalties: list[PenaltyItem] = []
    for gate in pick.gate_report or []:
        if not isinstance(gate, dict):
            continue
        status = str(gate.get("status", "")).upper()
        deduction = gate.get("deduction")
        if status not in ("WARNING", "FAIL") and not deduction:
            continue
        title = str(gate.get("gate_name") or gate.get("gate_key") or "Gate")
        detail = str(gate.get("reason") or "리스크 요인이 감지되었습니다.")
        delta = -float(deduction) if deduction else None
        penalties.append(PenaltyItem(title=title, score_delta=delta, detail=detail))

    for cond in pick.failed_conditions or []:
        penalties.append(
            PenaltyItem(
                title=cond,
                detail="조건 미충족 또는 경고 상태입니다.",
            )
        )

    return penalties


def build_analysis_detail(state: TassApiState, ticker: str) -> AnalysisDetailResponse:
    pick = state.get_pick(ticker)
    if pick is None:
        raise KeyError(f"Stock not in analysis results: {ticker}")

    views, radar = domain_views_from_pick(pick)
    return AnalysisDetailResponse(
        symbol=pick.symbol,
        name=pick.name,
        rank=pick.rank,
        total_score=pick.total_score,
        max_score=pick.max_score,
        recommendation=pick.recommendation,
        summary=_build_summary(pick),
        radar=radar,
        domains=views,
        rules=_build_rules(pick),
        penalties=_build_penalties(pick),
    )

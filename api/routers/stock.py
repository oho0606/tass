"""Stock detail routers."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query

from api.deps import get_api_state
from api.schemas.common import GateReportItem
from api.schemas.stock import DomainsResponse, IndicatorsResponse, RulesResponse, StockMetaResponse
from api.services.state import TassApiState, domain_views_from_pick, pick_detail_from_result
from api.services.stock_data import get_indicators, get_stock_meta
from engine.core.exceptions import DataException

router = APIRouter(prefix="/stock", tags=["stock"])


@router.get("/{code}", response_model=StockMetaResponse)
def stock_meta(code: str, state: TassApiState = Depends(get_api_state)) -> StockMetaResponse:
    """Return stock metadata for detail header."""
    try:
        return get_stock_meta(state, code)
    except DataException as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{code}/indicators", response_model=IndicatorsResponse)
def stock_indicators(
    code: str,
    limit: int = Query(120, ge=30, le=500),
    state: TassApiState = Depends(get_api_state),
) -> IndicatorsResponse:
    """Return OHLCV + indicator time series for charting."""
    try:
        return get_indicators(state, code, limit=limit)
    except DataException as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{code}/domains", response_model=DomainsResponse)
def stock_domains(code: str, state: TassApiState = Depends(get_api_state)) -> DomainsResponse:
    """Return domain scores formatted for radar chart."""
    pick = state.get_pick(code)
    if pick is None:
        raise HTTPException(status_code=404, detail=f"Stock not in today's picks: {code}")
    views, radar = domain_views_from_pick(pick)
    return DomainsResponse(symbol=pick.symbol, name=pick.name, domains=views, radar=radar)


@router.get("/{code}/rules", response_model=RulesResponse)
def stock_rules(code: str, state: TassApiState = Depends(get_api_state)) -> RulesResponse:
    """Return rule pass/fail and gate report for Explainable AI."""
    pick = state.get_pick(code)
    if pick is None:
        raise HTTPException(status_code=404, detail=f"Stock not in today's picks: {code}")
    detail = pick_detail_from_result(pick)
    gate_items = [GateReportItem.model_validate(g) for g in (detail.gate_report or [])]
    return RulesResponse(
        symbol=pick.symbol,
        name=pick.name,
        passed_conditions=detail.passed_conditions or [],
        failed_conditions=detail.failed_conditions or [],
        gate_report=gate_items,
        composite_breakdown=detail.composite_breakdown or {},
        recommendation_reason=detail.recommendation_reason or detail.reasons,
    )

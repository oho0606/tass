from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

import pandas as pd

from engine.core.types import GateResult as LegacyGateResult
from engine.core.types import GateStatus, MasterScoreResult, TrendEngineResult
from engine.gate.config import GateConfig
from engine.gate.config import load_gate_pipeline_yaml, merge_gate_config
from engine.gate.factory import build_gate_pipeline
from engine.gate.models import GateStatus as PipelineGateStatus
from engine.gate.models import PipelineResult
from engine.gate.pipeline import GatePipeline
from engine.gate.report import build_pipeline_gate_report
from engine.scoring.grades import grade_from_score, interpretation_from_score

GATE_LEGACY_NAMES = {
    "DataQualityGate": "DataQuality",
    "LiquidityGate": "Liquidity",
    "TrendGate": "TrendFloor",
    "MarketGate": "Market",
    "VolatilityGate": "Volatility",
}


@dataclass(frozen=True)
class SymbolGateEvaluation:
    pipeline_result: PipelineResult
    legacy_gate: LegacyGateResult
    gate_status: GateStatus
    gate_report: list[dict[str, Any]]
    adjusted_master: MasterScoreResult | None = None


def build_gate_data(
    df: pd.DataFrame,
    trend: TrendEngineResult,
    data_valid: bool,
    *,
    market_context: dict[str, Any] | None = None,
    listing_market: str | None = None,
) -> dict[str, Any]:
    """Build the data dict consumed by individual gate evaluators."""
    atr_percent = 0.0
    if "atr_14" in df.columns and "close" in df.columns:
        close = df["close"].iloc[-1]
        atr = df["atr_14"].iloc[-1]
        if pd.notna(close) and float(close) > 0 and pd.notna(atr):
            atr_percent = float(atr) / float(close)

    traded_value_ma20 = None
    if "traded_value_ma_20" in df.columns:
        traded_value_ma20 = df["traded_value_ma_20"].iloc[-1]

    data: dict[str, Any] = {
        "data_valid": data_valid,
        "bar_count": len(df),
        "traded_value_ma20": traded_value_ma20,
        "trend_score": trend.trend_score,
        "kospi_trend": "UP",
        "atr_percent": atr_percent,
    }
    if market_context:
        data.update(market_context)
    if listing_market is not None:
        data["listing_market"] = listing_market
    return data


def _to_legacy_gate_result(pipeline_result: PipelineResult) -> LegacyGateResult:
    failed: list[str] = []
    reasons: list[str] = []

    for result in pipeline_result.gate_results:
        legacy_name = GATE_LEGACY_NAMES.get(result.name, result.name)
        if result.status == PipelineGateStatus.FAIL:
            failed.append(legacy_name)
            reasons.append(result.reason)
        elif result.status == PipelineGateStatus.WARNING:
            reasons.append(result.reason)

    if failed:
        return LegacyGateResult(status="FAIL", reasons=reasons, failed_gates=failed)

    if pipeline_result.total_deduction > 0:
        return LegacyGateResult(status="WARN", reasons=reasons or ["Gate WARNING"])

    return LegacyGateResult(status="PASS", reasons=["Gate PASS"])


def apply_gate_deductions(
    master: MasterScoreResult,
    pipeline_result: PipelineResult,
) -> MasterScoreResult:
    """Apply WARNING deductions to master score when pipeline passes."""
    if not pipeline_result.is_passed or pipeline_result.total_deduction == 0:
        return master

    new_score = float(pipeline_result.final_score)
    grade = grade_from_score(new_score)
    return replace(
        master,
        total_score=new_score,
        grade=grade.code,
        grade_stars=grade.stars,
        interpretation=interpretation_from_score(new_score),
    )


def evaluate_symbol_gates(
    df: pd.DataFrame,
    trend: TrendEngineResult,
    data_valid: bool,
    gate_cfg: GateConfig | None = None,
    *,
    master: MasterScoreResult | None = None,
    pipeline: GatePipeline | None = None,
    pipeline_config_path: Path | None = None,
    market_context: dict[str, Any] | None = None,
    listing_market: str | None = None,
) -> SymbolGateEvaluation:
    """Run the full TASS-006 gate pipeline for one symbol."""
    cfg = gate_cfg or GateConfig()
    merged_config = merge_gate_config(
        load_gate_pipeline_yaml(pipeline_config_path),
        cfg,
    )
    active_pipeline = pipeline or build_gate_pipeline(merged_config)
    data = build_gate_data(
        df,
        trend,
        data_valid,
        market_context=market_context,
        listing_market=listing_market,
    )
    initial_score = int(master.total_score) if master is not None else 0

    pipeline_result = active_pipeline.evaluate_gate_pipeline(
        data,
        merged_config,
        initial_score=initial_score,
    )
    legacy_gate = _to_legacy_gate_result(pipeline_result)
    adjusted_master = apply_gate_deductions(master, pipeline_result) if master else None
    gate_report = build_pipeline_gate_report(
        pipeline_result,
        data=data,
        config=merged_config,
    )

    return SymbolGateEvaluation(
        pipeline_result=pipeline_result,
        legacy_gate=legacy_gate,
        gate_status=legacy_gate.status,
        gate_report=gate_report,
        adjusted_master=adjusted_master,
    )

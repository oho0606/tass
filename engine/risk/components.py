"""Risk component scorers for Risk Engine v1.0."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from engine.core.types import (
    GateResult,
    MasterScoreResult,
    ProbabilityResult,
    TrendEngineResult,
    TrendState,
)
from engine.risk.config import RiskThresholds
from engine.risk.mapping import clamp_risk_score, scale_linear


@dataclass(frozen=True)
class ComponentResult:
    key: str
    label: str
    score: float
    weight: int
    contribution: float
    reasons: tuple[str, ...]


def _last(df: pd.DataFrame, column: str) -> float | None:
    if column not in df.columns or df.empty:
        return None
    value = df[column].iloc[-1]
    if pd.isna(value):
        return None
    return float(value)


def _score_volatility(
    df: pd.DataFrame, thresholds: RiskThresholds
) -> tuple[float, tuple[str, ...]]:
    atr = _last(df, "atr_14")
    close = _last(df, "close")
    if atr is None or close is None or close <= 0:
        return 50.0, ("ATR data unavailable",)
    atr_pct = atr / close * 100.0
    score = scale_linear(
        atr_pct, thresholds.volatility_atr_pct_low, thresholds.volatility_atr_pct_high
    )
    return score, (f"ATR {atr_pct:.2f}% of price",)


def _score_gap(df: pd.DataFrame, thresholds: RiskThresholds) -> tuple[float, tuple[str, ...]]:
    if len(df) < 2:
        return 50.0, ("Insufficient bars for gap check",)
    prev_close = float(df["close"].iloc[-2])
    current_open = float(df["open"].iloc[-1])
    if prev_close <= 0:
        return 50.0, ("Invalid prior close",)
    gap_pct = abs(current_open - prev_close) / prev_close * 100.0
    score = scale_linear(gap_pct, thresholds.gap_pct_low, thresholds.gap_pct_high)
    return score, (f"Latest gap {gap_pct:.2f}%",)


def _score_liquidity(df: pd.DataFrame, thresholds: RiskThresholds) -> tuple[float, tuple[str, ...]]:
    traded_value = _last(df, "traded_value_ma_20")
    if traded_value is None:
        return 60.0, ("Liquidity data unavailable",)
    score = scale_linear(
        traded_value,
        thresholds.liquidity_value_low,
        thresholds.liquidity_value_high,
        invert=True,
    )
    return score, (f"20-day avg traded value {traded_value:,.0f}",)


def _score_trend(
    trend: TrendEngineResult, thresholds: RiskThresholds
) -> tuple[float, tuple[str, ...]]:
    normalized = 1.0 - (trend.trend_score / thresholds.trend_score_max)
    score = clamp_risk_score(normalized * 100.0)
    state_penalty = {
        TrendState.STRONG_UP: 0.0,
        TrendState.UP: 5.0,
        TrendState.SIDEWAYS: 15.0,
        TrendState.WEAK_DOWN: 35.0,
        TrendState.DOWN: 50.0,
    }.get(trend.trend_state, 20.0)
    score = clamp_risk_score(max(score, state_penalty))
    return score, (
        f"Trend score {trend.trend_score:.1f}/{thresholds.trend_score_max:.0f}",
        f"Trend state {trend.trend_state.value}",
    )


def _score_momentum(df: pd.DataFrame, thresholds: RiskThresholds) -> tuple[float, tuple[str, ...]]:
    rsi = _last(df, "rsi_14")
    macd_hist = _last(df, "macd_hist")
    reasons: list[str] = []
    score = 0.0
    if rsi is not None:
        if rsi >= thresholds.rsi_neutral_high:
            score = max(score, scale_linear(rsi, thresholds.rsi_neutral_high, 90.0))
            reasons.append(f"RSI overbought {rsi:.1f}")
        elif rsi <= thresholds.rsi_neutral_low:
            score = max(
                score,
                scale_linear(thresholds.rsi_neutral_low - rsi, 0.0, thresholds.rsi_neutral_low),
            )
            reasons.append(f"RSI oversold {rsi:.1f}")
        else:
            reasons.append(f"RSI neutral {rsi:.1f}")
    if macd_hist is not None and macd_hist < 0:
        score = max(score, scale_linear(abs(macd_hist), 0.0, 2.0))
        reasons.append(f"Negative MACD histogram {macd_hist:.2f}")
    if not reasons:
        return 30.0, ("Momentum data unavailable",)
    return score, tuple(reasons)


def _score_market(trend: TrendEngineResult) -> tuple[float, tuple[str, ...]]:
    fail_count = sum(1 for r in trend.composite_results.values() if r.verdict == "FAIL")
    unknown_count = sum(1 for r in trend.composite_results.values() if r.verdict == "UNKNOWN")
    score = clamp_risk_score(fail_count * 12.0 + unknown_count * 5.0)
    return score, (
        f"Composite FAIL count {fail_count}",
        f"Composite UNKNOWN count {unknown_count}",
    )


def _score_entry_timing(
    df: pd.DataFrame, thresholds: RiskThresholds
) -> tuple[float, tuple[str, ...]]:
    close = _last(df, "close")
    ma20 = _last(df, "ma_20")
    if close is None or ma20 is None or ma20 <= 0:
        return 40.0, ("MA20 unavailable for entry timing",)
    extension_pct = abs(close - ma20) / ma20 * 100.0
    score = scale_linear(extension_pct, thresholds.ma_extension_low, thresholds.ma_extension_high)
    return score, (f"Distance from MA20 {extension_pct:.2f}%",)


def _score_stop_loss_distance(
    df: pd.DataFrame, thresholds: RiskThresholds
) -> tuple[float, tuple[str, ...]]:
    atr = _last(df, "atr_14")
    close = _last(df, "close")
    if atr is None or close is None or close <= 0:
        return 40.0, ("ATR unavailable for stop distance",)
    stop_pct = atr * 2.0 / close * 100.0
    score = scale_linear(
        stop_pct, thresholds.volatility_atr_pct_low * 2, thresholds.volatility_atr_pct_high * 2
    )
    return score, (f"Estimated 2×ATR stop distance {stop_pct:.2f}%",)


def _score_atr(df: pd.DataFrame, thresholds: RiskThresholds) -> tuple[float, tuple[str, ...]]:
    if "atr_14" not in df.columns or len(df) < 20:
        return 40.0, ("Insufficient ATR history",)
    atr_series = df["atr_14"].dropna()
    if len(atr_series) < 10:
        return 40.0, ("Insufficient ATR history",)
    current = float(atr_series.iloc[-1])
    baseline = float(atr_series.tail(20).mean())
    if baseline <= 0:
        return 40.0, ("Invalid ATR baseline",)
    expansion = current / baseline
    score = scale_linear(expansion, 0.8, 1.8)
    return score, (f"ATR expansion ratio {expansion:.2f}",)


def _score_max_drawdown(
    df: pd.DataFrame, thresholds: RiskThresholds
) -> tuple[float, tuple[str, ...]]:
    if len(df) < 5:
        return 40.0, ("Insufficient bars for drawdown",)
    window = min(60, len(df))
    closes = df["close"].tail(window).astype(float)
    peak = closes.cummax()
    drawdown = (peak - closes) / peak.replace(0, np.nan) * 100.0
    current_dd = float(drawdown.iloc[-1])
    if np.isnan(current_dd):
        return 40.0, ("Drawdown unavailable",)
    score = scale_linear(current_dd, thresholds.drawdown_low, thresholds.drawdown_high)
    return score, (f"Current drawdown from {window}-bar peak {current_dd:.2f}%",)


def _score_price_extension(
    df: pd.DataFrame, thresholds: RiskThresholds
) -> tuple[float, tuple[str, ...]]:
    close = _last(df, "close")
    ma60 = _last(df, "ma_60")
    if close is None or ma60 is None or ma60 <= 0:
        return 30.0, ("MA60 unavailable for extension",)
    extension_pct = (close - ma60) / ma60 * 100.0
    score = scale_linear(
        max(extension_pct, 0.0), thresholds.ma_extension_low, thresholds.ma_extension_high
    )
    return score, (f"Extension above MA60 {extension_pct:.2f}%",)


def _score_false_breakout(df: pd.DataFrame) -> tuple[float, tuple[str, ...]]:
    if len(df) < 21:
        return 20.0, ("Insufficient bars for breakout check",)
    recent = df.tail(21)
    prior_high = float(recent["high"].iloc[:-1].max())
    last = recent.iloc[-1]
    close = float(last["close"])
    high = float(last["high"])
    ma20 = (
        float(last["ma_20"]) if "ma_20" in recent.columns and not pd.isna(last["ma_20"]) else None
    )
    if high > prior_high and ma20 is not None and close < ma20:
        return 85.0, ("High broke prior range but closed below MA20",)
    if high > prior_high:
        return 35.0, ("Recent range breakout without failure signal",)
    return 10.0, ("No false breakout pattern",)


def _score_data_quality(
    df: pd.DataFrame,
    data_valid: bool,
    gate: GateResult | None,
    thresholds: RiskThresholds,
) -> tuple[float, tuple[str, ...]]:
    reasons: list[str] = []
    score = 0.0
    if not data_valid:
        score = max(score, 80.0)
        reasons.append("Data validation failed")
    if len(df) < thresholds.min_bars:
        score = max(score, scale_linear(thresholds.min_bars - len(df), 0, thresholds.min_bars))
        reasons.append(f"History {len(df)} < {thresholds.min_bars} bars")
    if gate and gate.status == "FAIL":
        score = max(score, 70.0)
        reasons.append(f"Gate FAIL: {', '.join(gate.failed_gates)}")
    elif gate and gate.status == "WARN":
        score = max(score, 40.0)
        reasons.append("Gate WARN")
    required = ("close", "atr_14", "ma_20", "rsi_14")
    missing = [col for col in required if col not in df.columns or df[col].isna().all()]
    if missing:
        score = max(score, 50.0)
        reasons.append(f"Missing indicators: {', '.join(missing)}")
    if not reasons:
        return 5.0, ("Data quality acceptable",)
    return clamp_risk_score(score), tuple(reasons)


def _score_signal_conflict(trend: TrendEngineResult) -> tuple[float, tuple[str, ...]]:
    verdicts = [r.verdict for r in trend.atomic_results.values()]
    if not verdicts:
        return 20.0, ("No atomic signals",)
    pass_count = verdicts.count("PASS")
    fail_count = verdicts.count("FAIL")
    if pass_count > 0 and fail_count > 0:
        score = clamp_risk_score(40.0 + fail_count * 15.0)
        return score, (f"Conflicting atomics PASS={pass_count} FAIL={fail_count}",)
    unknown_count = verdicts.count("UNKNOWN")
    if unknown_count > 0:
        return clamp_risk_score(20.0 + unknown_count * 10.0), (
            f"UNKNOWN atomic signals {unknown_count}",
        )
    return 5.0, ("Atomic signals aligned",)


_COMPONENT_EVALUATORS = {
    "volatility_risk": lambda ctx: _score_volatility(ctx["df"], ctx["thresholds"]),
    "gap_risk": lambda ctx: _score_gap(ctx["df"], ctx["thresholds"]),
    "liquidity_risk": lambda ctx: _score_liquidity(ctx["df"], ctx["thresholds"]),
    "trend_risk": lambda ctx: _score_trend(ctx["trend"], ctx["thresholds"]),
    "momentum_risk": lambda ctx: _score_momentum(ctx["df"], ctx["thresholds"]),
    "market_risk": lambda ctx: _score_market(ctx["trend"]),
    "entry_timing_risk": lambda ctx: _score_entry_timing(ctx["df"], ctx["thresholds"]),
    "stop_loss_distance": lambda ctx: _score_stop_loss_distance(ctx["df"], ctx["thresholds"]),
    "atr_risk": lambda ctx: _score_atr(ctx["df"], ctx["thresholds"]),
    "maximum_drawdown_risk": lambda ctx: _score_max_drawdown(ctx["df"], ctx["thresholds"]),
    "price_extension_risk": lambda ctx: _score_price_extension(ctx["df"], ctx["thresholds"]),
    "false_breakout_risk": lambda ctx: _score_false_breakout(ctx["df"]),
    "data_quality_risk": lambda ctx: _score_data_quality(
        ctx["df"], ctx["data_valid"], ctx["gate"], ctx["thresholds"]
    ),
    "signal_conflict_risk": lambda ctx: _score_signal_conflict(ctx["trend"]),
}


def evaluate_components(
    df: pd.DataFrame,
    trend: TrendEngineResult,
    master: MasterScoreResult,
    probability: ProbabilityResult | None,
    gate: GateResult | None,
    data_valid: bool,
    component_weights: tuple,
    thresholds: RiskThresholds,
) -> list[ComponentResult]:
    """Evaluate all risk components. Master Score and Probability are context-only (not mixed in)."""
    _ = master, probability  # inputs per spec; reserved for future regime-aware calibration
    ctx = {
        "df": df,
        "trend": trend,
        "thresholds": thresholds,
        "data_valid": data_valid,
        "gate": gate,
    }
    results: list[ComponentResult] = []
    for comp in component_weights:
        evaluator = _COMPONENT_EVALUATORS.get(comp.key)
        if evaluator is None:
            score, reasons = 50.0, (f"Component {comp.key} not implemented",)
        else:
            score, reasons = evaluator(ctx)
        contribution = round(score * comp.weight / 100.0, 2)
        results.append(
            ComponentResult(
                key=comp.key,
                label=comp.label,
                score=round(score, 2),
                weight=comp.weight,
                contribution=contribution,
                reasons=reasons,
            )
        )
    return results

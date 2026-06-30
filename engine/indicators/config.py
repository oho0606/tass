from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml


@dataclass(frozen=True)
class IndicatorCriteria:
    """Chart criteria used by indicator calculations."""

    ma_periods: tuple[int, ...] = (5, 10, 20, 60, 120, 240)
    ema_periods: tuple[int, ...] = (5, 10, 20, 60, 120, 240)
    atr_period: int = 14
    hist_vol_period: int = 20
    bollinger_period: int = 20
    rsi_period: int = 14
    stochastic_period: int = 14
    cci_period: int = 20
    mfi_period: int = 14
    roc_period: int = 12
    momentum_period: int = 10
    adx_period: int = 14
    volume_ma_period: int = 20
    relative_volume_period: int = 20
    volume_high_period: int = 20
    volume_low_period: int = 20
    traded_value_ma_period: int = 20
    macd_fast: int = 12
    macd_slow: int = 26
    macd_signal: int = 9


def _as_positive_int(value: object, default: int) -> int:
    parsed = int(value) if value is not None else default
    return parsed if parsed > 0 else default


def _as_periods(value: object, default: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(value, list):
        return default
    parsed = tuple(sorted({int(v) for v in value if int(v) > 0}))
    return parsed or default


@lru_cache(maxsize=1)
def load_indicator_criteria(path: Path | None = None) -> IndicatorCriteria:
    """Load chart criteria from YAML with safe defaults."""
    if path is None:
        path = Path("config/chart_criteria_v1.yaml")
    if not path.exists():
        return IndicatorCriteria()

    with path.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    ma = raw.get("moving_average", {})
    vol = raw.get("volatility", {})
    mo = raw.get("momentum", {})
    vo = raw.get("volume", {})
    macd = raw.get("macd", {})

    return IndicatorCriteria(
        ma_periods=_as_periods(ma.get("periods"), IndicatorCriteria.ma_periods),
        ema_periods=_as_periods(ma.get("ema_periods"), IndicatorCriteria.ema_periods),
        atr_period=_as_positive_int(vol.get("atr_period"), IndicatorCriteria.atr_period),
        hist_vol_period=_as_positive_int(
            vol.get("hist_vol_period"), IndicatorCriteria.hist_vol_period
        ),
        bollinger_period=_as_positive_int(
            vol.get("bollinger_period"), IndicatorCriteria.bollinger_period
        ),
        rsi_period=_as_positive_int(mo.get("rsi_period"), IndicatorCriteria.rsi_period),
        stochastic_period=_as_positive_int(
            mo.get("stochastic_period"), IndicatorCriteria.stochastic_period
        ),
        cci_period=_as_positive_int(mo.get("cci_period"), IndicatorCriteria.cci_period),
        mfi_period=_as_positive_int(mo.get("mfi_period"), IndicatorCriteria.mfi_period),
        roc_period=_as_positive_int(mo.get("roc_period"), IndicatorCriteria.roc_period),
        momentum_period=_as_positive_int(
            mo.get("momentum_period"), IndicatorCriteria.momentum_period
        ),
        adx_period=_as_positive_int(mo.get("adx_period"), IndicatorCriteria.adx_period),
        volume_ma_period=_as_positive_int(
            vo.get("volume_ma_period"), IndicatorCriteria.volume_ma_period
        ),
        relative_volume_period=_as_positive_int(
            vo.get("relative_volume_period"), IndicatorCriteria.relative_volume_period
        ),
        volume_high_period=_as_positive_int(
            vo.get("volume_high_period"), IndicatorCriteria.volume_high_period
        ),
        volume_low_period=_as_positive_int(
            vo.get("volume_low_period"), IndicatorCriteria.volume_low_period
        ),
        traded_value_ma_period=_as_positive_int(
            vo.get("traded_value_ma_period"), IndicatorCriteria.traded_value_ma_period
        ),
        macd_fast=_as_positive_int(macd.get("fast"), IndicatorCriteria.macd_fast),
        macd_slow=_as_positive_int(macd.get("slow"), IndicatorCriteria.macd_slow),
        macd_signal=_as_positive_int(macd.get("signal"), IndicatorCriteria.macd_signal),
    )

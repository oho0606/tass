from __future__ import annotations

import pandas as pd

from engine.indicators.config import IndicatorCriteria, load_indicator_criteria
from engine.indicators.ma import compute_ema, compute_ma
from engine.indicators.momentum import (
    compute_adx,
    compute_cci,
    compute_macd,
    compute_mfi,
    compute_momentum,
    compute_roc,
    compute_rsi,
    compute_stochastic,
)
from engine.indicators.volatility import (
    compute_atr,
    compute_bollinger,
    compute_hist_volatility,
    compute_true_range,
)
from engine.indicators.volume import compute_money_flow, compute_obv, compute_relative_volume


DEFAULT_MA_PERIODS = (5, 10, 20, 60, 120, 240)
DEFAULT_EMA_PERIODS = (5, 10, 20, 60, 120, 240)


def compute_all(df: pd.DataFrame, criteria: IndicatorCriteria | None = None) -> pd.DataFrame:
    """Compute all indicators required by TASS-002 and catalog rules."""
    if df.empty:
        return df.copy()

    cfg = criteria or load_indicator_criteria()
    result = df.copy()
    ma_periods = sorted(set(DEFAULT_MA_PERIODS).union(cfg.ma_periods))
    ema_periods = sorted(set(DEFAULT_EMA_PERIODS).union(cfg.ema_periods))
    for period in ma_periods:
        result[f"ma_{period}"] = compute_ma(result["close"], period)
    for period in ema_periods:
        result[f"ema_{period}"] = compute_ema(result["close"], period)

    result["true_range"] = compute_true_range(result)
    result["atr_14"] = compute_atr(result, 14)
    result[f"atr_{cfg.atr_period}"] = compute_atr(result, cfg.atr_period)
    result["hist_vol_20"] = compute_hist_volatility(result["close"], 20)
    result[f"hist_vol_{cfg.hist_vol_period}"] = compute_hist_volatility(
        result["close"], cfg.hist_vol_period
    )
    bb = compute_bollinger(result["close"], 20)
    for col in bb.columns:
        result[col] = bb[col]
    if cfg.bollinger_period != 20:
        bb_custom = compute_bollinger(result["close"], cfg.bollinger_period)
        result[f"bb_mid_{cfg.bollinger_period}"] = bb_custom["bb_mid_20"]
        result[f"bb_upper_{cfg.bollinger_period}"] = bb_custom["bb_upper_20"]
        result[f"bb_lower_{cfg.bollinger_period}"] = bb_custom["bb_lower_20"]
        result[f"bb_width_{cfg.bollinger_period}"] = bb_custom["bb_width_20"]

    macd = compute_macd(
        result["close"],
        fast=cfg.macd_fast,
        slow=cfg.macd_slow,
        signal=cfg.macd_signal,
    )
    result["macd"] = macd["macd"]
    result["macd_signal"] = macd["signal"]
    result["macd_hist"] = macd["histogram"]
    result["rsi_14"] = compute_rsi(result["close"], 14)
    result[f"rsi_{cfg.rsi_period}"] = compute_rsi(result["close"], cfg.rsi_period)
    stoch = compute_stochastic(result, 14)
    result["stoch_k_14"] = stoch["stoch_k_14"]
    result["stoch_d_14"] = stoch["stoch_d_14"]
    stoch_custom = compute_stochastic(result, cfg.stochastic_period)
    result[f"stoch_k_{cfg.stochastic_period}"] = stoch_custom["stoch_k_14"]
    result[f"stoch_d_{cfg.stochastic_period}"] = stoch_custom["stoch_d_14"]
    result["cci_20"] = compute_cci(result, 20)
    result[f"cci_{cfg.cci_period}"] = compute_cci(result, cfg.cci_period)
    result["mfi_14"] = compute_mfi(result, 14)
    result[f"mfi_{cfg.mfi_period}"] = compute_mfi(result, cfg.mfi_period)
    result["roc_12"] = compute_roc(result["close"], 12)
    result[f"roc_{cfg.roc_period}"] = compute_roc(result["close"], cfg.roc_period)
    result["momentum_10"] = compute_momentum(result["close"], 10)
    result[f"momentum_{cfg.momentum_period}"] = compute_momentum(result["close"], cfg.momentum_period)
    result["adx_14"] = compute_adx(result, 14)
    result[f"adx_{cfg.adx_period}"] = compute_adx(result, cfg.adx_period)

    result["obv"] = compute_obv(result)
    result["volume_ma_20"] = result["volume"].rolling(20).mean()
    result[f"volume_ma_{cfg.volume_ma_period}"] = result["volume"].rolling(cfg.volume_ma_period).mean()
    result["relative_volume"] = compute_relative_volume(result["volume"], 20)
    result[f"relative_volume_{cfg.relative_volume_period}"] = compute_relative_volume(
        result["volume"], cfg.relative_volume_period
    )
    result["volume_high_20"] = result["volume"].rolling(20).max()
    result[f"volume_high_{cfg.volume_high_period}"] = result["volume"].rolling(
        cfg.volume_high_period
    ).max()
    result["volume_low_20"] = result["volume"].rolling(20).min()
    result[f"volume_low_{cfg.volume_low_period}"] = result["volume"].rolling(cfg.volume_low_period).min()
    result["money_flow"] = compute_money_flow(result)
    result["traded_value"] = result["close"] * result["volume"]
    result["traded_value_ma_20"] = result["traded_value"].rolling(20).mean()
    result[f"traded_value_ma_{cfg.traded_value_ma_period}"] = result["traded_value"].rolling(
        cfg.traded_value_ma_period
    ).mean()
    return result

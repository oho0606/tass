import pandas as pd

from engine.indicators.config import IndicatorCriteria
from engine.indicators.ma import compute_ma


def test_ma_constant_series():
    s = pd.Series([10.0] * 30)
    ma = compute_ma(s, 5)
    assert ma.iloc[-1] == 10.0


def test_ma_increasing():
    s = pd.Series(range(1, 31), dtype=float)
    ma = compute_ma(s, 5)
    assert ma.iloc[-1] == 28.0


def test_ema_increasing():
    from engine.indicators.ma import compute_ema

    s = pd.Series(range(1, 31), dtype=float)
    ema = compute_ema(s, 5)
    assert ema.iloc[-1] > 0


def test_registry_includes_ema_columns():
    from engine.indicators.registry import compute_all

    from tests.fixtures.ohlcv import make_uptrend_ohlcv

    df = compute_all(make_uptrend_ohlcv(n=80))
    assert "ema_20" in df.columns
    assert "ema_240" in df.columns


def test_registry_accepts_chart_criteria():
    from engine.indicators.registry import compute_all

    from tests.fixtures.ohlcv import make_uptrend_ohlcv

    criteria = IndicatorCriteria(
        ma_periods=(7, 20, 60),
        ema_periods=(9, 20, 60),
        rsi_period=21,
        stochastic_period=21,
        cci_period=30,
        mfi_period=21,
        roc_period=20,
        momentum_period=21,
        adx_period=21,
        volume_ma_period=30,
        relative_volume_period=30,
        volume_high_period=30,
        volume_low_period=30,
        traded_value_ma_period=30,
        atr_period=20,
        hist_vol_period=30,
        bollinger_period=30,
        macd_fast=8,
        macd_slow=21,
        macd_signal=5,
    )
    df = compute_all(make_uptrend_ohlcv(n=120), criteria=criteria)

    assert "ma_7" in df.columns
    assert "ema_9" in df.columns
    assert "rsi_21" in df.columns
    assert "stoch_k_21" in df.columns
    assert "volume_ma_30" in df.columns
    assert "traded_value_ma_30" in df.columns
    assert "atr_20" in df.columns
    assert "hist_vol_30" in df.columns
    assert "bb_mid_30" in df.columns

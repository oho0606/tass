import pandas as pd


def compute_true_range(df: pd.DataFrame) -> pd.Series:
    high = df["high"]
    low = df["low"]
    close = df["close"]
    prev_close = close.shift(1)
    return pd.concat(
        [(high - low), (high - prev_close).abs(), (low - prev_close).abs()],
        axis=1,
    ).max(axis=1)


def compute_atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    tr = compute_true_range(df)
    return tr.rolling(window=period, min_periods=period).mean()


def compute_hist_volatility(close: pd.Series, period: int = 20) -> pd.Series:
    returns = close.pct_change()
    return returns.rolling(period).std() * (252**0.5) * 100.0


def compute_bollinger(close: pd.Series, period: int = 20, std_dev: float = 2.0) -> pd.DataFrame:
    mid = close.rolling(period).mean()
    std = close.rolling(period).std()
    upper = mid + std_dev * std
    lower = mid - std_dev * std
    width = (upper - lower) / mid.replace(0, pd.NA) * 100.0
    return pd.DataFrame({"bb_mid_20": mid, "bb_upper_20": upper, "bb_lower_20": lower, "bb_width_20": width})

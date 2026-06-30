import pandas as pd





def compute_relative_volume(volume: pd.Series, period: int = 20) -> pd.Series:

    """Volume divided by N-period moving average."""

    avg = volume.rolling(period).mean()

    return volume / avg





def compute_money_flow(df: pd.DataFrame) -> pd.Series:

    """Typical price times volume (raw money flow per bar)."""

    typical = (df["high"] + df["low"] + df["close"]) / 3.0

    return typical * df["volume"]





def compute_obv(df: pd.DataFrame) -> pd.Series:

    direction = (df["close"].diff() > 0).astype(int) - (df["close"].diff() < 0).astype(int)

    return (direction * df["volume"]).fillna(0).cumsum()


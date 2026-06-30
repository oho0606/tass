import pandas as pd


def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    return 100 - (100 / (1 + rs))


def compute_macd(
    series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9
) -> pd.DataFrame:
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    sig = macd.ewm(span=signal, adjust=False).mean()
    return pd.DataFrame({"macd": macd, "signal": sig, "histogram": macd - sig})


def compute_stochastic(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    low_min = df["low"].rolling(period).min()
    high_max = df["high"].rolling(period).max()
    k = (df["close"] - low_min) / (high_max - low_min).replace(0, pd.NA) * 100.0
    d = k.rolling(3).mean()
    return pd.DataFrame({"stoch_k_14": k, "stoch_d_14": d})


def compute_cci(df: pd.DataFrame, period: int = 20) -> pd.Series:
    tp = (df["high"] + df["low"] + df["close"]) / 3.0
    sma = tp.rolling(period).mean()
    mad = tp.rolling(period).apply(lambda x: (abs(x - x.mean())).mean(), raw=True)
    return (tp - sma) / (0.015 * mad.replace(0, pd.NA))


def compute_mfi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    tp = (df["high"] + df["low"] + df["close"]) / 3.0
    raw = tp * df["volume"]
    delta = tp.diff()
    pos = raw.where(delta > 0, 0.0).rolling(period).sum()
    neg = raw.where(delta < 0, 0.0).rolling(period).sum()
    return 100 - (100 / (1 + pos / neg.replace(0, pd.NA)))


def compute_roc(series: pd.Series, period: int = 12) -> pd.Series:
    return series.pct_change(period) * 100.0


def compute_momentum(series: pd.Series, period: int = 10) -> pd.Series:
    return series.diff(period)


def compute_adx(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high = df["high"]
    low = df["low"]
    up = high.diff()
    down = -low.diff()
    plus_dm = up.where((up > down) & (up > 0), 0.0)
    minus_dm = down.where((down > up) & (down > 0), 0.0)
    tr = pd.concat(
        [(high - low), (high - df["close"].shift()).abs(), (low - df["close"].shift()).abs()],
        axis=1,
    ).max(axis=1)
    atr = tr.rolling(period).mean()
    plus_di = 100 * plus_dm.rolling(period).mean() / atr.replace(0, pd.NA)
    minus_di = 100 * minus_dm.rolling(period).mean() / atr.replace(0, pd.NA)
    dx = (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, pd.NA) * 100.0
    return dx.rolling(period).mean()

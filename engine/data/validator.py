from __future__ import annotations

import logging
from dataclasses import dataclass, field

import pandas as pd

_OHLCV_COLUMNS = ("open", "high", "low", "close", "volume")


@dataclass
class DataValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


class DataQualityValidator:
    """OHLCV data integrity checks (TASS data spec)."""

    def __init__(self, min_rows: int = 120):
        self.min_rows = min_rows
        self.logger = logging.getLogger("DataValidator")

    def validate(self, df: pd.DataFrame, symbol: str = "") -> bool:
        label = f"[{symbol}] " if symbol else ""

        if df is None or df.empty:
            self.logger.warning(f"{label}Data is empty.")
            return False

        normalized = _normalize_ohlcv_columns(df)
        if normalized is None:
            self.logger.warning(f"{label}Missing required OHLCV columns.")
            return False

        if len(normalized) < self.min_rows:
            self.logger.warning(
                f"{label}Insufficient data: {len(normalized)} < {self.min_rows}"
            )
            return False

        if normalized[list(_OHLCV_COLUMNS)].isnull().any().any():
            self.logger.warning(f"{label}NaN values detected.")
            return False

        if normalized.index.duplicated().any():
            self.logger.warning(f"{label}Duplicated dates detected.")
            return False

        if not normalized.index.is_monotonic_increasing:
            self.logger.warning(f"{label}Date order is not strictly increasing.")
            return False

        if (normalized[list(_OHLCV_COLUMNS)] < 0).any().any():
            self.logger.error(f"{label}Negative price or volume detected.")
            return False

        invalid_prices = normalized[
            (normalized["low"] > normalized["high"])
            | (normalized["low"] > normalized["open"])
            | (normalized["low"] > normalized["close"])
            | (normalized["high"] < normalized["open"])
            | (normalized["high"] < normalized["close"])
        ]
        if not invalid_prices.empty:
            self.logger.error(f"{label}Invalid OHLC logic detected.")
            return False

        return True


def _normalize_ohlcv_columns(df: pd.DataFrame) -> pd.DataFrame | None:
    rename = {col: col.lower() for col in df.columns if col.lower() in _OHLCV_COLUMNS}
    if len(rename) < len(_OHLCV_COLUMNS):
        return None
    out = df.rename(columns=rename)
    return out[list(_OHLCV_COLUMNS)].copy()


def sanitize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Expand high/low to envelope OHLC (fixes split-adjusted provider quirks)."""
    if df is None or df.empty:
        return df
    normalized = _normalize_ohlcv_columns(df)
    if normalized is None:
        return df
    out = normalized.copy()
    ohlc = out[["open", "high", "low", "close"]]
    out["high"] = ohlc.max(axis=1)
    out["low"] = ohlc.min(axis=1)
    if "volume" in df.columns:
        vol_col = next((c for c in df.columns if c.lower() == "volume"), None)
        if vol_col is not None:
            out["volume"] = df[vol_col].values
    out.index = df.index
    return out


def validate_ohlcv(df: pd.DataFrame, min_bars: int = 60) -> DataValidationResult:
    """Functional validator used by DataEngine (returns structured result)."""
    errors: list[str] = []
    warnings: list[str] = []

    if df is None or df.empty:
        return DataValidationResult(valid=False, errors=["empty_dataframe"])

    normalized = _normalize_ohlcv_columns(df)
    if normalized is None:
        return DataValidationResult(valid=False, errors=["missing_columns"])

    if len(normalized) < min_bars:
        errors.append(f"insufficient_bars:{len(normalized)}<{min_bars}")

    if normalized[list(_OHLCV_COLUMNS)].isna().any().any():
        errors.append("nan_in_price")

    if normalized.index.duplicated().any():
        errors.append("duplicated_dates")

    if not normalized.index.is_monotonic_increasing:
        errors.append("date_order_not_increasing")

    if (normalized[list(_OHLCV_COLUMNS)] < 0).any().any():
        errors.append("negative_price_or_volume")

    invalid_ohlc = (
        (normalized["high"] < normalized["low"])
        | (normalized["high"] < normalized["open"])
        | (normalized["high"] < normalized["close"])
        | (normalized["low"] > normalized["open"])
        | (normalized["low"] > normalized["close"])
    )
    if invalid_ohlc.any():
        errors.append("invalid_ohlc_relationship")

    zero_vol_ratio = (normalized["volume"] <= 0).mean()
    if zero_vol_ratio > 0.1:
        warnings.append(f"high_zero_volume_ratio:{zero_vol_ratio:.2f}")

    return DataValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)

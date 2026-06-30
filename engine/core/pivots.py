from __future__ import annotations

import numpy as np
import pandas as pd


def find_pivot_highs(high: pd.Series, strength: int = 3) -> list[int]:
    indices: list[int] = []
    values = high.values
    n = len(values)
    for i in range(strength, n - strength):
        window = values[i - strength : i + strength + 1]
        if values[i] == np.nanmax(window):
            indices.append(i)
    return indices


def find_pivot_lows(low: pd.Series, strength: int = 3) -> list[int]:
    indices: list[int] = []
    values = low.values
    n = len(values)
    for i in range(strength, n - strength):
        window = values[i - strength : i + strength + 1]
        if values[i] == np.nanmin(window):
            indices.append(i)
    return indices

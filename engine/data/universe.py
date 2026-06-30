from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from engine.data.providers.pykrx_provider import PyKRXProvider

_MARKET_TO_CSV = {
    "KOSPI": "KS",
    "KOSDAQ": "KQ",
    "KS": "KS",
    "KQ": "KQ",
}


@dataclass
class UniverseEntry:
    symbol: str
    name: str
    market: str = "KS"


class UniverseLoader:
    """Load KS/KQ universe from CSV (supports Code/Name/Market or symbol/name/market)."""

    def __init__(self, filepath: str | Path = "config/universe_krx_backtest.csv"):
        self.filepath = Path(filepath)

    def load_universe(self) -> list[dict]:
        df = pd.read_csv(self.filepath, dtype=str)
        df.columns = [col.strip() for col in df.columns]
        column_map = {
            "code": "Code",
            "symbol": "Code",
            "name": "Name",
            "market": "Market",
        }
        renamed = {col: column_map.get(col.lower(), col) for col in df.columns}
        df = df.rename(columns=renamed)

        if not {"Code", "Name", "Market"}.issubset(df.columns):
            raise ValueError("Universe CSV must contain Code, Name, and Market columns.")

        df["Code"] = df["Code"].str.strip().str.zfill(6)
        df["Market"] = df["Market"].str.strip().str.upper()
        return df[["Code", "Name", "Market"]].to_dict("records")


def load_universe(path: Path) -> list[UniverseEntry]:
    records = UniverseLoader(path).load_universe()
    return [
        UniverseEntry(
            symbol=row["Code"],
            name=row["Name"],
            market=row["Market"],
        )
        for row in records
    ]


def generate_universe_csv(
    output_path: Path | str,
    *,
    markets: tuple[str, ...] = ("KOSPI", "KOSDAQ"),
    target_date: str = "",
    meta_provider: PyKRXProvider | None = None,
) -> Path:
    """Build a TASS universe CSV from PyKRX listings (KOSPI/KOSDAQ)."""
    provider = meta_provider or PyKRXProvider()
    rows: list[dict[str, str]] = []

    for market in markets:
        for entry in provider.get_universe(market, target_date):
            rows.append(
                {
                    "Code": entry["code"],
                    "Name": entry["name"],
                    "Market": _MARKET_TO_CSV.get(entry["market"], entry["market"]),
                }
            )

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows, columns=["Code", "Name", "Market"]).to_csv(output, index=False)
    return output

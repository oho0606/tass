"""Integration tests for Application Service pipeline."""

from __future__ import annotations

from pathlib import Path

from engine.application import RecommendationService
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_application_daily_picks_pipeline(tmp_path: Path) -> None:
    """End-to-end daily picks through Application Service (offline)."""
    universe = tmp_path / "universe.csv"
    universe.write_text("symbol,name,market\n005930,삼성전자,KS\n", encoding="utf-8")

    settings_path = tmp_path / "settings.yaml"
    settings_path.write_text(
        "adapter: yahoo\n"
        "min_bars: 60\n"
        "min_traded_value_ma20: 0\n"
        "trend_floor_score: 0\n"
        "top_n: 20\n",
        encoding="utf-8",
    )

    service = RecommendationService(settings_path=settings_path)
    result = service.run_daily_picks(
        universe,
        use_cache=False,
        output_dir=tmp_path / "output",
        ohlcv_overrides={"005930": make_uptrend_ohlcv(n=260)},
    )

    assert result.output_path is not None
    assert result.output_path.exists()
    assert len(result.picks) >= 1
    assert result.picks[0].symbol == "005930"
    assert result.picks[0].recommendation is not None
    assert "moving_average" in result.picks[0].domains

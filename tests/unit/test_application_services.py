"""Unit tests for Application Service layer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.application import (
    BacktestService,
    RecommendationService,
    load_pipeline_settings,
    pick_to_dict,
)
from engine.core.exceptions import DataException, RecommendationException
from engine.core.types import PickResult
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv


class TestPipelineSettings:
    def test_load_defaults_when_missing(self, tmp_path: Path) -> None:
        settings = load_pipeline_settings(tmp_path / "missing.yaml")
        assert settings.top_n == 20
        assert settings.adapter == "yahoo"

    def test_to_gate_config(self) -> None:
        settings = load_pipeline_settings()
        gate = settings.to_gate_config()
        assert gate.min_bars == settings.min_bars


class TestRecommendationService:
    def test_generate_daily_picks_synthetic(self, tmp_path: Path) -> None:
        universe = tmp_path / "universe.csv"
        universe.write_text(
            "symbol,name,market\n005930,삼성전자,KS\n000660,SK하이닉스,KS\n",
            encoding="utf-8",
        )
        service = RecommendationService()
        result = service.generate_daily_picks(
            universe,
            use_cache=False,
            ohlcv_overrides={
                "005930": make_uptrend_ohlcv(n=80, start=100.0),
                "000660": make_uptrend_ohlcv(n=80, start=120.0),
            },
        )
        assert result.universe_size == 2
        assert result.candidates_evaluated == 2
        assert len(result.picks) <= 2
        assert all(isinstance(pick, PickResult) for pick in result.picks)

    def test_save_daily_picks_writes_json(self, tmp_path: Path) -> None:
        universe = tmp_path / "universe.csv"
        universe.write_text("symbol,name,market\n005930,삼성전자,KS\n", encoding="utf-8")
        service = RecommendationService()
        generated = service.generate_daily_picks(
            universe,
            use_cache=False,
            ohlcv_overrides={"005930": make_uptrend_ohlcv(n=80)},
        )
        saved = service.save_daily_picks(generated, output_dir=tmp_path / "output")
        assert saved.output_path is not None
        assert saved.output_path.exists()
        payload = json.loads(saved.output_path.read_text(encoding="utf-8"))
        assert "picks" in payload

    def test_missing_universe_raises(self, tmp_path: Path) -> None:
        service = RecommendationService()
        with pytest.raises(DataException):
            service.generate_daily_picks(tmp_path / "missing.csv")

    def test_empty_universe_raises(self, tmp_path: Path) -> None:
        path = tmp_path / "empty.csv"
        path.write_text("symbol,name,market\n", encoding="utf-8")
        service = RecommendationService()
        with pytest.raises(DataException):
            service.generate_daily_picks(path)

    def test_no_candidates_raises(self, tmp_path: Path) -> None:
        path = tmp_path / "universe.csv"
        path.write_text("symbol,name,market\n005930,삼성전자,KS\n", encoding="utf-8")
        import pandas as pd

        service = RecommendationService()
        empty = pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
        with pytest.raises(RecommendationException):
            service.generate_daily_picks(
                path,
                use_cache=False,
                ohlcv_overrides={"005930": empty},
            )


class TestBacktestService:
    def test_run_rule_backtest(self, tmp_path: Path) -> None:
        service = BacktestService()
        result = service.run_rule_backtest(
            ohlcv_by_symbol={
                "UP": make_uptrend_ohlcv(n=200),
                "DOWN": make_downtrend_ohlcv(n=200),
            },
            rule_ids=("TR0001",),
            output_dir=tmp_path,
        )
        assert result.report_path.exists()
        assert len(result.markdown_paths) >= 1

    def test_pick_to_dict_roundtrip_fields(self) -> None:
        pick = PickResult(
            rank=1,
            symbol="005930",
            name="삼성전자",
            total_score=450.0,
            max_score=1000.0,
            domains={},
            confidence=80.0,
            risk=30.0,
            reasons=["test"],
            gate="PASS",
        )
        payload = pick_to_dict(pick)
        assert payload["symbol"] == "005930"
        assert payload["rank"] == 1

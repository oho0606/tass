"""API integration tests (TASS-040)."""

from __future__ import annotations

from dataclasses import replace

import pytest
from fastapi.testclient import TestClient

fastapi = pytest.importorskip("fastapi")

from api.app import app  # noqa: E402
from api.deps import get_api_state  # noqa: E402
from api.services.state import PicksCache, TassApiState  # noqa: E402
from engine.core.types import PickResult  # noqa: E402


def _sample_pick(rank: int = 1) -> PickResult:
    return PickResult(
        rank=rank,
        symbol="005930",
        name="삼성전자",
        total_score=720.0,
        max_score=1000.0,
        domains={
            "trend": {"score": 80, "max": 100, "grade": "A", "state": "Up Trend"},
            "moving_average": {"score": 70, "max": 100, "grade": "B"},
            "volume": {"score": 60, "max": 100, "grade": "B"},
        },
        confidence=75.0,
        risk=25.0,
        reasons=["Strong trend alignment"],
        gate="PASS",
        grade="A",
        probability=0.62,
        recommendation="BUY",
        recommendation_grade="A",
        recommendation_reason=["Master score above threshold"],
        passed_conditions=["Trend gate passed"],
        failed_conditions=[],
        gate_report=[{"gate_name": "Liquidity", "status": "PASS", "reason": "OK"}],
        composite_breakdown={"TR0001": {"verdict": "PASS"}},
    )


@pytest.fixture
def mock_state() -> TassApiState:
    state = TassApiState(universe_path=__import__("pathlib").Path("config/universe_sample.csv"))
    pick = _sample_pick()
    state._cache = PicksCache(  # noqa: SLF001
        date="2026-06-19",
        generated_at="2026-06-19T12:00:00",
        mvp_mode=True,
        universe_size=10,
        candidates_evaluated=10,
        picks=[pick],
        all_ranked=[pick],
        market_context={"kospi_trend": "UP", "kosdaq_trend": "UP", "market_trend": "UP"},
    )
    return state


@pytest.fixture
def client(mock_state: TassApiState) -> TestClient:
    app.dependency_overrides[get_api_state] = lambda: mock_state
    yield TestClient(app)
    app.dependency_overrides.clear()


class TestHealth:
    def test_health_ok(self, client: TestClient) -> None:
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["picks_cached"] is True


class TestPicks:
    def test_today_picks(self, client: TestClient) -> None:
        response = client.get("/picks/today")
        assert response.status_code == 200
        data = response.json()
        assert data["date"] == "2026-06-19"
        assert len(data["picks"]) == 1
        assert data["picks"][0]["symbol"] == "005930"

    def test_picks_history(self, client: TestClient) -> None:
        response = client.get("/picks/history?limit=3")
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert isinstance(data["items"], list)


class TestRanking:
    def test_ranking_pagination(self, client: TestClient) -> None:
        response = client.get("/ranking?page=1&page_size=10")
        assert response.status_code == 200
        data = response.json()
        assert data["pagination"]["total"] == 1
        assert data["items"][0]["symbol"] == "005930"


class TestStock:
    def test_stock_meta(self, client: TestClient) -> None:
        response = client.get("/stock/005930")
        assert response.status_code == 200
        assert response.json()["name"] == "삼성전자"

    def test_stock_domains(self, client: TestClient) -> None:
        response = client.get("/stock/005930/domains")
        assert response.status_code == 200
        data = response.json()
        assert len(data["domains"]) == 3
        assert "Trend" in data["radar"]

    def test_stock_rules(self, client: TestClient) -> None:
        response = client.get("/stock/005930/rules")
        assert response.status_code == 200
        data = response.json()
        assert data["passed_conditions"] == ["Trend gate passed"]
        assert len(data["gate_report"]) == 1

    def test_stock_not_found(self, client: TestClient) -> None:
        response = client.get("/stock/999999/domains")
        assert response.status_code == 404


class TestBacktest:
    def test_backtest_summary(self, client: TestClient) -> None:
        response = client.get("/backtest/summary")
        assert response.status_code == 200
        assert "available" in response.json()

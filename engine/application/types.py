"""Application layer DTOs (TASS-030 §6)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from engine.backtest.types import BacktestRunResult
from engine.core.types import PickResult


@dataclass(frozen=True)
class DailyPicksResult:
    """Result of a Today's Picks generation run."""

    date: str
    generated_at: str
    mvp_mode: bool
    universe_size: int
    candidates_evaluated: int
    picks: tuple[PickResult, ...]
    gate_blocked: tuple[PickResult, ...] = field(default_factory=tuple)
    output_path: Path | None = None


@dataclass(frozen=True)
class BacktestServiceResult:
    """Result of an application-level backtest run."""

    run_result: BacktestRunResult
    report_path: Path
    markdown_paths: tuple[Path, ...] = field(default_factory=tuple)

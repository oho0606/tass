"""Repository layer for daily picks persistence (PostgreSQL)."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any

from engine.core.logging import get_logger

logger = get_logger(__name__)


class PicksRepository:
    """CRUD for the ``daily_picks`` and ``run_sessions`` tables."""

    def save_picks(
        self,
        session,
        pick_date: date,
        picks: list[dict[str, Any]],
        gate_blocked: list[dict[str, Any]],
    ) -> None:
        """Upsert all picks for *pick_date* in a single transaction.

        Existing rows for the date are deleted first to allow refreshes.
        """
        if session is None:
            return
        try:
            from api.db.models import DailyPickRow

            session.query(DailyPickRow).filter(
                DailyPickRow.pick_date == pick_date
            ).delete(synchronize_session=False)

            for pick in picks:
                row = DailyPickRow(
                    pick_date=pick_date,
                    symbol=str(pick.get("symbol", "")),
                    rank=int(pick.get("rank", 0)),
                    payload={**pick, "_source": "picks"},
                )
                session.add(row)

            for blocked in gate_blocked:
                row = DailyPickRow(
                    pick_date=pick_date,
                    symbol=str(blocked.get("symbol", "")),
                    rank=int(blocked.get("rank", 9999)),
                    payload={**blocked, "_source": "gate_blocked"},
                )
                session.add(row)

            logger.info(
                "DB: saved {} picks + {} blocked for {}",
                len(picks),
                len(gate_blocked),
                pick_date,
            )
        except Exception as exc:
            logger.warning("DB save_picks failed: {}", exc)
            raise

    def load_picks_for_date(
        self,
        session,
        pick_date: date,
    ) -> tuple[list[dict], list[dict]] | None:
        """Load (picks, gate_blocked) for *pick_date*. Returns None if not found."""
        if session is None:
            return None
        try:
            from api.db.models import DailyPickRow

            rows = (
                session.query(DailyPickRow)
                .filter(DailyPickRow.pick_date == pick_date)
                .order_by(DailyPickRow.rank)
                .all()
            )
            if not rows:
                return None

            picks = [r.payload for r in rows if r.payload.get("_source") != "gate_blocked"]
            blocked = [r.payload for r in rows if r.payload.get("_source") == "gate_blocked"]
            return picks, blocked
        except Exception as exc:
            logger.warning("DB load_picks_for_date failed: {}", exc)
            return None

    def load_latest_picks(
        self,
        session,
    ) -> tuple[date, list[dict], list[dict]] | None:
        """Load most recent pick_date rows. Returns (date, picks, blocked) or None."""
        if session is None:
            return None
        try:
            from api.db.models import DailyPickRow

            latest_date: date | None = (
                session.query(DailyPickRow.pick_date)
                .order_by(DailyPickRow.pick_date.desc())
                .first()
            )
            if latest_date is None:
                return None
            latest_date = latest_date[0]
            result = self.load_picks_for_date(session, latest_date)
            if result is None:
                return None
            picks, blocked = result
            return latest_date, picks, blocked
        except Exception as exc:
            logger.warning("DB load_latest_picks failed: {}", exc)
            return None

    def record_run_start(self, session, session_id: str, run_date: date) -> None:
        if session is None:
            return
        try:
            from api.db.models import RunSession

            row = RunSession(
                session_id=session_id,
                run_date=run_date,
                status="running",
            )
            session.add(row)
        except Exception as exc:
            logger.warning("DB record_run_start failed: {}", exc)

    def record_run_complete(
        self,
        session,
        session_id: str,
        *,
        universe_size: int,
        candidates_evaluated: int,
        picks_count: int,
        elapsed_seconds: float,
    ) -> None:
        if session is None:
            return
        try:
            from api.db.models import RunSession

            row = session.query(RunSession).filter_by(session_id=session_id).first()
            if row:
                row.status = "complete"
                row.universe_size = universe_size
                row.candidates_evaluated = candidates_evaluated
                row.picks_count = picks_count
                row.elapsed_seconds = elapsed_seconds
                row.finished_at = datetime.utcnow()
        except Exception as exc:
            logger.warning("DB record_run_complete failed: {}", exc)

    def record_run_error(self, session, session_id: str, error: str) -> None:
        if session is None:
            return
        try:
            from api.db.models import RunSession

            row = session.query(RunSession).filter_by(session_id=session_id).first()
            if row:
                row.status = "error"
                row.error_message = error
                row.finished_at = datetime.utcnow()
        except Exception as exc:
            logger.warning("DB record_run_error failed: {}", exc)


_repo: PicksRepository | None = None


def get_picks_repo() -> PicksRepository:
    global _repo
    if _repo is None:
        _repo = PicksRepository()
    return _repo
